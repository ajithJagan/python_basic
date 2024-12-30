file_read = open(r"D:\POC\python_basic\python\File\ajith.txt", "r")  # r is used to read the file

# print(file_read.read())

# print(file_read.readlines())
# print(file_read.readline())
# print(file_read.readline())


print(f"f is used for file name {file_read}") # f is used for file name


for line in file_read:
    print(line)


file_read.close()