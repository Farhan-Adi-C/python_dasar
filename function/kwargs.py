# kwargs allow to recieve any number of keyword arguments

def personalData(**data):
    return f"Nama: {data["nama"]}, Umur: {data["umur"]}"

print(personalData(nama = "Farhan", umur = 20))

hehe = None
print(hehe or "data lain")