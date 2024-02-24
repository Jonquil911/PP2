#ex1
def squares(n):
    for i in range(1,n+1):
        yield i**2
print(*squares(int(input("n = "))))

#ex2
def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i
print(*even(int(input("n = "))), sep=", ")

#ex3
def div_3and4 (n):
    for i in range(1,n+1):
        if i%4==0 and i%3==0:
            yield i

print (*div_3and4(int(input("n = "))))

#ex4
def squares_from_a_to_b(a,b):
    for i in range(a,b+1):
        yield i**2

a, b =int(input("a = ")), int(input("b = "))
for i in squares_from_a_to_b(a,b):
    print(i)

#ex5
def from_n_to_0(n):
    for i in range(n+1):
        yield n-i
print(*from_n_to_0(int(input("n = "))))