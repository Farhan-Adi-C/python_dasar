"""
Hand Magic Brush
=================
Program deteksi tangan via webcam yang mengubah jari telunjuk kamu jadi
"kuas cahaya" (seperti efek api/neon trail) di layar.

Gestur yang didukung:
- Telunjuk terangkat sendiri     -> menggambar trail cahaya mengikuti ujung jari
- Pinch (jempol dekat telunjuk)  -> toggle mode HAPUS (eraser) di titik tersebut
- Kepalan tangan (fist)          -> membersihkan seluruh canvas
- Jumlah jari yang terbuka (1-5) -> mengganti warna kuas secara real-time

Catatan versi: mediapipe 0.10.30+ / 1.x menghapus API lama "mp.solutions".
Script ini sudah pakai API baru "mediapipe.tasks" (HandLandmarker), jadi
kompatibel dengan mediapipe versi terbaru.

Instalasi (jalankan sekali di terminal):
    pip install opencv-python mediapipe numpy

Jalankan:
    python hand_magic_brush.py

Model deteksi tangan (hand_landmarker.task) akan otomatis diunduh ke folder
yang sama saat pertama kali dijalankan (butuh koneksi internet sekali saja).

Tekan 'q' untuk keluar, 's' untuk menyimpan screenshot canvas ke file PNG.
"""

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision as mp_vision
from mediapipe.tasks.python import BaseOptions
import time
import math
import os
import urllib.request
from collections import deque

# ----------------------------------------------------------------------
# KONFIGURASI
# ----------------------------------------------------------------------
CAM_INDEX = 0
FRAME_W, FRAME_H = 960, 720
TRAIL_MAX_LEN = 40    
PINCH_THRESHOLD = 40 
BRUSH_THICKNESS_BASE = 14

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hand_landmarker.task")
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"


COLOR_MAP = {
    1: (60, 60, 255),    
    2: (60, 220, 255),   
    3: (60, 255, 120),   
    4: (255, 200, 60),   
    5: (255, 60, 220),  
}
DEFAULT_COLOR = (255, 255, 255)

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),         
    (0, 5), (5, 6), (6, 7), (7, 8),         
    (5, 9), (9, 10), (10, 11), (11, 12),    
    (9, 13), (13, 14), (14, 15), (15, 16),  
    (13, 17), (17, 18), (18, 19), (19, 20), 
    (0, 17),                                
]

FINGER_TIPS = [4, 8, 12, 16, 20]  


def pastikan_model_ada():
    """Unduh file model hand_landmarker.task jika belum ada di folder ini."""
    if not os.path.exists(MODEL_PATH):
        print("Mengunduh model hand_landmarker.task (sekali saja)...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Model berhasil diunduh ke", MODEL_PATH)


def hitung_jari_terbuka(landmarks, handedness_label):
    """Mengembalikan jumlah jari yang sedang terangkat (0-5).
    `landmarks` adalah list NormalizedLandmark dari hasil HandLandmarker."""
    jari_terbuka = 0

    
    if handedness_label == "Right":
        if landmarks[FINGER_TIPS[0]].x < landmarks[FINGER_TIPS[0] - 1].x:
            jari_terbuka += 1
    else:
        if landmarks[FINGER_TIPS[0]].x > landmarks[FINGER_TIPS[0] - 1].x:
            jari_terbuka += 1

    for tip_id in FINGER_TIPS[1:]:
        if landmarks[tip_id].y < landmarks[tip_id - 2].y:
            jari_terbuka += 1

    return jari_terbuka


def gambar_rangka_tangan(frame, pts_px, color):
    """Gambar titik & garis rangka tangan manual (pengganti mp_draw.draw_landmarks)."""
    for a, b in HAND_CONNECTIONS:
        cv2.line(frame, pts_px[a], pts_px[b], (200, 200, 200), 1, cv2.LINE_AA)
    for x, y in pts_px:
        cv2.circle(frame, (x, y), 3, color, -1, cv2.LINE_AA)


def jarak_piksel(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

class GlowTrail:
    """Menyimpan titik-titik terakhir dan menggambarnya dengan efek fade + glow."""

    def __init__(self, maxlen=TRAIL_MAX_LEN):
        self.points = deque(maxlen=maxlen)   
    def tambah(self, x, y, color):
        self.points.append((x, y, color))

    def kosongkan(self):
        self.points.clear()

    def gambar(self, canvas_glow):
        n = len(self.points)
        if n < 2:
            return
        for i in range(1, n):
            x1, y1, c1 = self.points[i - 1]
            x2, y2, c2 = self.points[i]
            
            fade = i / n
            thickness = max(1, int(BRUSH_THICKNESS_BASE * fade))
            cv2.line(canvas_glow, (x1, y1), (x2, y2), c2, thickness, cv2.LINE_AA)


def terapkan_efek_glow(canvas):
    """Blur berlapis supaya garis kelihatan menyala seperti neon/api."""
    blur1 = cv2.GaussianBlur(canvas, (0, 0), sigmaX=6, sigmaY=6)
    blur2 = cv2.GaussianBlur(canvas, (0, 0), sigmaX=16, sigmaY=16)
    glow = cv2.addWeighted(blur1, 0.6, blur2, 0.4, 0)
    hasil = cv2.addWeighted(canvas, 1.0, glow, 0.8, 0)
    return hasil

 
def main():
    pastikan_model_ada()

    cap = cv2.VideoCapture(CAM_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)

    if not cap.isOpened():
        print("Tidak bisa membuka webcam. Cek CAM_INDEX atau izin kamera.")
        return

    options = mp_vision.HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=MODEL_PATH),
        running_mode=mp_vision.RunningMode.VIDEO,
        num_hands=1,
        min_hand_detection_confidence=0.6,
        min_tracking_confidence=0.6,
    )
    landmarker = mp_vision.HandLandmarker.create_from_options(options)
 
    canvas = np.zeros((FRAME_H, FRAME_W, 3), dtype=np.uint8)
    trail = GlowTrail()

    mode_hapus = False
    last_fist_time = 0
    fps_prev_time = time.time()
    frame_idx = 0
    t_mulai = time.time()

    print("Hand Magic Brush berjalan. Tekan 'q' untuk keluar, 's' untuk screenshot.")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        frame = cv2.resize(frame, (FRAME_W, FRAME_H))
        frame = cv2.flip(frame, 1)   
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

        timestamp_ms = int((time.time() - t_mulai) * 1000)
        frame_idx += 1
        hasil = landmarker.detect_for_video(mp_image, timestamp_ms)

        warna_aktif = DEFAULT_COLOR
        status_text = "Tidak ada tangan terdeteksi"

        if hasil.hand_landmarks and hasil.handedness:
            lm = hasil.hand_landmarks[0]
            label_tangan = hasil.handedness[0][0].category_name

            pts_px = [(int(p.x * FRAME_W), int(p.y * FRAME_H)) for p in lm]
            jari = hitung_jari_terbuka(lm, label_tangan)
            warna_aktif = COLOR_MAP.get(jari, DEFAULT_COLOR)

            ujung_telunjuk = pts_px[8]
            ujung_jempol = pts_px[4]
            jarak_pinch = jarak_piksel(ujung_telunjuk, ujung_jempol)
 
            if jari == 0:
                status_text = "Kepalan terdeteksi -> membersihkan canvas"
                if time.time() - last_fist_time > 1.0:
                    canvas[:] = 0
                    trail.kosongkan()
                    last_fist_time = time.time()
 
            elif jarak_pinch < PINCH_THRESHOLD:
                mode_hapus = True
                status_text = f"Mode HAPUS aktif (pinch, jari={jari})"
                cv2.circle(canvas, ujung_telunjuk, 30, (0, 0, 0), -1)
                trail.kosongkan()
 
            else:
                mode_hapus = False
                status_text = f"Menggambar - {jari} jari terangkat"
                trail.tambah(ujung_telunjuk[0], ujung_telunjuk[1], warna_aktif)
                trail.gambar(canvas)

            gambar_rangka_tangan(frame, pts_px, warna_aktif)
        else:
            trail.kosongkan()
 
        canvas_glow = terapkan_efek_glow(canvas)
        mask = cv2.cvtColor(canvas_glow, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
        fg = cv2.bitwise_and(canvas_glow, canvas_glow, mask=mask)
        output = cv2.add(bg, fg)
 
        fps = 1.0 / max(1e-6, (time.time() - fps_prev_time))
        fps_prev_time = time.time()
        cv2.rectangle(output, (0, 0), (FRAME_W, 40), (20, 20, 20), -1)
        cv2.putText(output, status_text, (10, 27), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(output, f"FPS: {fps:.0f}", (FRAME_W - 110, 27),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1, cv2.LINE_AA)

        cv2.imshow("Hand Magic Brush", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            nama_file = f"hand_magic_capture_{int(time.time())}.png"
            cv2.imwrite(nama_file, canvas_glow)
            print(f"Canvas disimpan sebagai {os.path.abspath(nama_file)}")

    cap.release()
    landmarker.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()