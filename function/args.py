# args allow function to accept any number of positional arguments

def namaOrang(*name):
    return f"{name[0]}"

print(namaOrang("Farhan", "Adi", "Chandra"))
