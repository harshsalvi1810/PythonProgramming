# concept of print function

# f-string

name = "Harsh"
age = 23
salary = 50000

print(f"Hii my name is {name} and my age is {age} and salary is {salary}")

#concept of .format method
print("Hii my name is {} and my age is {} and salary is {}".format(name,age,salary))

#conept of list: only square bracket[]

lst1 = []
lst2 = [1,2,3,56.78,"hii","world",True,False,[10,20,30],(10,20),{1,2,3},{"india":1000},None]

# if condition
name = input("Enter the name: ")

if name == "Harsh":
    print(f"Your name is {name}")

coin_side = input("Enter coin side: ")

# if (coin_side.lower() == "head") :
#     print("Won the game")
# else :
#     print("lose the game")

if (coin_side.lower() == "head") :
    print("You win the game")
elif (coin_side.lower() == "tail") :
    print("I win the game")
else :
    print("Enter the correct value")


#concept of indexing and slicing

# # str = "Welcome to the world of python programming" 
str1 = "Hello World"
print(str1[4])
print(str1[-5])
print(str1[:])
print(str1[3:-1])
print(str1[-6:-1])

str[start:stop:step]
print(str1[::2])

string = input("Enter a string: ")
string1 = string[::-1]

if (string == string1):
    print(f"String in pallindrome")
else :
    print(f"String is not pallindrome")
# 90 exc 80 good 70 mod 60 pass 50 fail