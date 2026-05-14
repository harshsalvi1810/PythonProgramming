
# celsius = float(input("enter value of celsius: "))

# fahrenheit = ((9 * celsius)/5)+32

# print(fahrenheit)

#  a = float(input("Enter a number: "))

# if (a == 0):
#     print("Number is zero")
# elif (a > 0):
#     print("Number is positive")
# elif (a < 0):
#     print("Number is negative")

# if (a % 3 == 0):
#     if (a % 5 == 0):
#         print ("Number is divisible by 3 and 5")
#     else:
#        print("divisible by 3 only")
# else:
#     ("Not divisible by 3")

# if (a % 4 == 0):
#     print("Year is leap ")

# if (a >= 90):
#     print("A")
# elif (75 <= a <= 89):
#     print("B")
# elif (50 <= a <= 74):
#     print("C")
# elif (a < 50):
#     print("Fail")

# for i in range (1,11):
#     print(i)

a = int(input("Enter the number: "))

#  for i in range (a):
#     a = a + i
# print(a)

# for i in range(1,11):
#     i = a * i 
#     print(i)
num = 0
while (a > 0):
    b = a % 10
    num = (num * 10) + b
    a = a // 10 
print(num)