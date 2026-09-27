# f = open("demofile.txt", "rt")
# print(f.read())
# f.close()

with open("demofile.txt", "rt") as f:
    # print(f.read(40))
    print(f.readline())