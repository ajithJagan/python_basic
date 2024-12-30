
file = open(r"D:\POC\python_basic\python\File\ajith.txt", "w")  # w is used to write the file

file.write("Hello Ajith")

file.close()

file = open(r"D:\POC\python_basic\python\File\ajith.txt", "a")  # a is used to append the file

file.write(" Hello Akil")

file.close()


file = open(r"D:\POC\python_basic\python\File\ajith.txt", "r")

print(file.read())

file.close()

