import os 

if os.path.exists(r"D:\POC\python_basic\python\File\dummy.txt"):
    print("Its present")
    os.remove("D:\POC\python_basic\python\File\dummy.txt")
else:
    print("Its not present")
