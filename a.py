#pattern program for A
for row in range(7):
    for col in  range(5):
        if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
            print("#",end="")
        else:
            print(end=" ")
    print()



#Factorial of a number using recursion method
num = 5 
def rec(n):
    if n == 1:
        return (n)
    else:
        return n*rec(n-1)
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",rec(num))




#Generating password

import random
def strong():
    upper = "ABCDEFGHIJKLMNOPQRSTUVW"
    lower = 'abcdefghijkl,mnopqrst'
    special = "!@#$%^&**"
    password = ''
    password += random.choice(upper)
    password += random.choice(lower)
    password += random.choice(special)
    password += random.choice (upper)
    return password

def weak():
    a = ['1234','abcd']
    return random.choice(a)

b = input("strong or weak ")
if b == 'strong':
    print(strong())
elif b == 'weak':
    print(weak())
else:
    print("error")



#copy one file to other
import shutil,os
os.chdir('D:\\')
shutil.copy("D:\\h.html","D:\\basic\\test1.py")
print('done')




test_string = "Geeksforgeeks is best Computer Science Portal"
  
# printing original string 
print ("The original string is : " +  test_string) 
  
# using split()  to extract words from string 
res = test_string.split() 
  
# printing result 
print ("The list of words is : " +  str(res)) 






#split at specific position
b = [a[i:i+1] for i in range(0,len(a),1)]
#no of words in string
b=a.split()
print(b)
c=dict()
for abc in b:
    if abc in c:
        c[abc]+=1
    else:
        c[abc]=1
print(c)
