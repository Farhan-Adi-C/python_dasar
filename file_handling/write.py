f = open("demofile.txt", "at")
f.write("\n Farhan Adi Chandra")

with open("demofile.txt") as f:
    print(f.read())

# override 

fl = open("demofile.txt", "w")
fl.write("hehehehe")
with open("demofile.txt") as f:
    print(f.read())


new = open("pesan.txt", "x")
new.write("coba")