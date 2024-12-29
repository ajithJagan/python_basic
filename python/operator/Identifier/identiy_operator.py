
a =[1,2]
b =[1,2]

print(id(a))  # id is memory address
print(id(b))  # id is memory address

print(a is b) # is is check the memory address
print(a is not b) # is not is check the memory address is not same


print(a == b) # == is check the value is same
print(a != b) # != is check the value

# == is suitable for dynamic values


input_from_user = input("Enter the value : ")

print(input_from_user)

if input_from_user == "1":
    print("Its one")
else:
    print("Its not a one")

