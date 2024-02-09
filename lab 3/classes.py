#ex1
class SS:
    def getString(self,string):
        self.string=string
    def printString(self):
        print(self.string.upper())

s1=SS()
s1.getString(input())
s1.printString()

#ex2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return length**2

s=Square(int(input()))
print(s.area())

#ex3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

r=Rectangle(int(input()), int(input()))
print(r.area())

#ex4
import math
class Point:
    def __init__(self,x0,y0):
        self.x=x0
        self.y=y0
    def show(self):
        print (f"({self.x},{self.y})")
    def move(self,x1,y1):
        self.x=x1
        self.y=y1
    def dist(self,x2,y2):
        self.x2=x2
        self.y2=y2
        dist = math.sqrt((self.x2-self.x)**2+(self.y2-self.y)**2)
        print(dist)

p1=Point(1,1)
p1.show()
p1.move(2,2)
p1.show()
p1.dist(4,4)

#ex5
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,rep):
        self.rep=rep
        self.balance+=self.rep
    def withdraw(self,wit):
        self.wit=wit
        if self.wit>self.balance:
            print("Withdrawals may not exceed the available balance!")
        else:
            self.balance-=wit
    def show_balance(self):
        print(f"Balance: {self.balance}")


owner1=Account("owner1",10000)
owner1.deposite(2000)
owner1.withdraw(15000)
owner1.withdraw(9000)
owner1.show_balance()

#ex6
numbers=[1,2,3,4,5,6,7,7,8,12,11,43]

prime=filter(lambda x:all(x%i!=0 for i in range(4, 7)),numbers)
print(list(prime))