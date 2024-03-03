#ex1
import os

path = input()

print("only directories:")
[print(i) for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]

print("\nonly files")
[print(i) for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]

print("\nall directories, files:")
for root, directories, files in os.walk(path):
    print("Catalogs in", root)
    [print(os.path.join(root, dir)) for dir in directories]
    print("Files in", root)
    [print(os.path.join(root, file)) for file in files]
    print()


#ex2
path = input()

if os.path.exists(path):
    print(f"Path {path} exists.")
    print(f"Path {path} {'is readable.' if os.access(path, os.R_OK) else 'is not readable.'}")
    print(f"Path {path} {'is writable.' if os.access(path, os.W_OK) else 'is not writable.'}")
    print(f"Path {path} {'is executable.' if os.access(path, os.X_OK) else 'is not executable.'}")
else:
    print(f"Path {path} does not exist.")

#ex3
path = input()

if os.path.exists(path):
    print("Path exists")
    print("Filename:", os.path.basename(path))
    print("Directory:", os.path.dirname(path))
else:
    print("Path does not exist.")

#ex4
number_of_lines = 0

with open("text.txt", 'r') as file:
    for line in file:
        number_of_lines += 1

print("Number of lines in the file:", number_of_lines)

#ex5
list1 = list(input().split())
with open('file.txt', 'w') as file:
    for i in list1:
        file.write(str(i) + " ")

#ex6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        pass

#ex7
with open("text.txt", 'r') as file:
    with open("copy.txt", 'w') as file2:
        for line in file:
            file2.write(line)

#ex8
path = input()

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("No access")
else:
    print("File doesn't exist")


