import os
if(os.path.exists("pesan.txt")):
    os.remove("pesan.txt")
else:
    print("the file does not exist")

if(os.path.exists("coba_folder")): 
    print("hello")
    os.rmdir("coba_folder")