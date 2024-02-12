#ex1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    print (ounces)

weight_in_grams = int(input())
grams_to_ounces(weight_in_grams)


#ex2
def centigrade (F):
    C = (5 / 9) * (F - 32)
    print (C)

Fahrenheit_temperature = int(input())
centigrade(Fahrenheit_temperature)


#ex3
def solve(numheads, numlegs):
    rabbits = (2*numheads) - (numlegs/2)
    chickens = numheads - rabbits
    print ("Numbers of rabbits =", int(rabbits))
    print ("Numbers of chickens =", int(chickens))

numheads = int(input("Enter the number of heads: "))
numlegs = int(input("Enter the number of legs: "))
solve(numheads, numlegs)


#ex4
def filter_prime(numbers):
    Numbers = numbers.split()
    for i in range(len(Numbers)):
        if int(Numbers[i])%2!=0 and int(Numbers[i])%3!=0 and int(Numbers[i])%5!=0 and int(Numbers[i])%7!=0:
            print (Numbers[i], end=" ")

numbers = input()
filter_prime(numbers)

#ex5
def permutations(string,prefix=''):
    if len(string)==0:
        print(prefix)
    else:
        for i in range(len(string)):
            permutations(string[:i]+string[i+1:],prefix+string[i])

string=input()
permutations(string)

#ex6
def reverse(string):
    Str = string.split()
    Str1 = ""
    for i in Str:
        Str1 = i + " " + Str1
    print (Str1)

str = input()
reverse(str)

#ex7
def has_33(nums):
    for i in range(len(nums)):
        if nums[i] == 3:
            if nums[i+1] == 3:
                print (True)
                break
            else:
                print (False)
                break

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])

#ex8
def spy_game(nums):
    contain = [0,0,7]
    index = 0
    for i in nums:
        if i==contain[index]:
            index+=1
            if index==3:
                return True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#ex9
import math
def volume_of_a_sphere(R):
    V = (4 * math.pi * R**2)/3
    print (V)
r = int(input())
volume_of_a_sphere(r)

#ex10
def unique(list):
    list1=[]
    for i in list:
        if i in list1:
            continue
        else:
            list1.append(i)
    print(list1)

lis=[1,2,2,2,3,5,3,2,6,7,6,7]
unique(lis)

#ex11
def palindrom(word):
    if word[::-1] == word:
        print("Palindrom")
    else:
        print("Not palindrom")

word = str(input())
palindrom(word)

#ex12
def histogram(list):
    for i in list:
        print ("*"*i)

histogram([4, 9, 7])

#ex13
import random
number = random.randint(1,20)
name = input("Hello! What is your name?")
print (f"Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.")
guesses=1
while(True):
    n=int(input())
    if n==number:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        break
    elif n<number:
        print("Your guess is too low.\nTake a guess.")
        guesses+=1
    else:
        print("Your guess is too high.\nTake a guess.")
        guesses += 1
