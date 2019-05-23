a = str(input('enter the string:'))
c = len(a)
#print(c)
for i in range(c//2):
    if (a[i]==a[-1-i]):
        print("palindrome")
else:
    print("not")

#2nd method
a=input("enter sequence")
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("Not a Palindrome")
    