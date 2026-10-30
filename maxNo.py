#A program to find the largest number among three.

#1. Method 1:
print("----The program requires you to enter 3 numbers which will be compared and you will be given the largest number among the three----")
digits = []
num1 = int(input("Enter the first digit: "))
digits.append(num1)

num2 = int(input("Enter the second digit: "))
digits.append(num2)

num3 = int(input("Enter the third digit: "))
digits.append(num3)

if num1 >num2> num3:
    print("The largest number is", num1)

elif num2> num1> num3:
    print("The largest number is", num2)

else:
    print("The largest number is", num3)

#2. Method 2:
print("----The program requires you to enter 3 numbers which will be compared and you will be given the largest number among the three----")
digits = []
print("Enter three digits:")

for i in range(1,4):
    nums = int(input(f"{i}: "))
    digits.append(nums)

print("The largest digit is ", max(digits))