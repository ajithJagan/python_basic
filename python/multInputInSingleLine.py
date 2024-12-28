name1,name2 = input("Enter your full name : ").split()
print("Your first name is : ",name1)
print("Your last name is : ",name2)

print(type(name1))

empty_list = []

while True:
    user_input = input("Enter a paragraph : ")
    if user_input:
        empty_list.append(user_input)
    else: 
        break
    # join the list of strings into a single string with spaces between each string

print(empty_list)

print(" ".join(empty_list))


