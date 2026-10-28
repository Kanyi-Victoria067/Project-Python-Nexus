##1. While Loop: A program that displays numbers from 10-15.

#Step 1: Initialize:
loop = 10

#Step 2: Set a condition.
while loop <= 15:
    print(loop)
    loop += 1  # OR loop = loop + 1 (Increment by 1)

#Example 2: Displays numbers from 100-90.
number = 100

while number >= 90:
    print(number)
    number -= 1


##For Loop: Print numbers from 1-5.
for y in range(1, 6,): #Always start with the first number you want displayed, followed by the last number + 1, and finally the increment you want.
    print(y)

for x in range(100, 89, -2):
    print(x)


