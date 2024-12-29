number = int (input("enter the number : "))
class_name = input ("Enter your class : ")

if number==10 :
    print("Its ten")
elif number ==12 :
    print("Its twelve")
    if class_name == "A" :
        print("You are in A class")
    else :
        print("You are not in A class")
    
else :
    print("Its not a ten ")