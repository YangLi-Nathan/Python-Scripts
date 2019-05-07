"""
Input. Read a line from the terminal and echo it to the user.
"""
print("Enter something here: ")
user_input=input()
print("you entered: " +user_input)

"""
Integer input. Read a line and convert it to an integer.
"""

print("Enter Integer here: ")
user_input=input()
print("you entered: ", int(user_input))

"""
leap year a leap year is divisible by 4, 
except when its divisible by 100 and not by 400.
Write a program to tell if a year is a leap year.
"""

print("Enter a year here: ")
year = int(input())

if (year % 4 == 0) & (year % 400 == 0):
    print("This is a leap year")
else:
    print ("This is not a leap year")

"""
sum all the integers below 1000 that are multiples of 3 or 5
"""
sum=0

for i in range (0,1000):
    if (i%3 == 0 or i %5 ==0):
        sum =sum+i

print (sum)