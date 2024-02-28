import re

#ex1
string = input()
x = re.search(r'ab*',string)
if x:
    print ("success")
else:
    print ("fail")

#ex2
string = input()
x = re.search(r'ab{2,3}',string)
if x:
    print ("success")
else:
    print ("fail")

#ex3
string = input()
x = re.findall(r'[a-z]+_[a-z]+',string)
print(x)

#ex4
string = input()
x = re.findall(r'[A-Z][a-z]+',string)
print(x)

#ex5
string = input()
x = re.findall(r'a.*b$',string)
print(x)

#ex6
string = input()
x = re.sub('[ ,.]', ':',string)
print(x)

#ex7
string = input()
x = re.findall('_[a-z]', string)
y = x.copy()

for i in range(len(x)):
    x[i] = x[i][1:]
upx = [i.upper() for i in x]

for i in range(len(x)):
    index = string.find(y[i])
    string = string[:index] + upx[i] + string[index + 1:]
print (string)

#ex8
string = input()
x = re.findall('[A-Z][^A-Z]*', string)
print(x)

#ex9
string = input()
x = re.sub(r'(?<=[a-z])([A-Z])', r' \1', string)
print(x)

#ex10
string = input()
x = re.findall('[A-Z]', string)
y = x.copy()
lowx = [i.lower() for i in x]

for i in range(len(x)-1):
    lowx[i+1] = '_' + lowx[i+1]

for i in range(len(x)):
    index = string.find(y[i])
    string = string[:index] + lowx[i] + string[index + 1:]
print (string)