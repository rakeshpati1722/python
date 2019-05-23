#swap two number without third variable
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num1,num2= num2,num1
print("after swaping first number",num1)
print("after swaping second number",num2)


#swap two number using third variable
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
temp = a
a=b
b=temp
print("after swaping first number",a)
print("after swaping first number",b)