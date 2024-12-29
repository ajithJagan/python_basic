

number = 1
while number <= 10:
    print(number,end=" , ")
    number += 1
else:
    print("Loop is over")
    
    
print("============================================")
number1 = 1
while number1 <= 10:
    print(number1,end=" , ")
    number1 += 1
    if number1 == 5:
        break
else:
    print("Loop is over")
    
    
print("============================================")

for i in range(1,11):
    print(i,end=" , ")
else:
    print("Loop is over")


print("============================================")

for i in range(1,11):
    print(i,end=" , ")
    if i == 5:
        break
else:
    print("Loop is over")
