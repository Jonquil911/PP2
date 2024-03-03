#ex1
a = [1,2,3,4,5,6,7]
b = 1
for i in range(len(a)):
    b *= a[i]
print (b)

#ex2
string = "QaZwSxEdC"
upper = sum(1 for i in string if i.isupper())
lower = sum(1 for i in string if i.islower())
print("Number of upper case:", upper, "\nLower case letters:", lower)

#ex3
string = input()
if string == string[::-1]:
    print("Palindrom")
else:
    print("Not palindrom")


#ex4
import math
num = int(input())
ms = int(input())
print (f"Square root of {num} after {ms} miliseconds is {math.sqrt(num)}")

#ex5
tuple = (0,1,2,3,4,5,True,"word")
print (all(tuple))