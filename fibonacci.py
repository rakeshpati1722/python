a = 0
b= 1
for i in range (0,10):
    print(a)
    a,b =b, a+b
    
#Recursion 
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
print(Fibonacci(9)) 


#Dynamic Programming
FibArray = [0,1] 
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif:
        n <=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
print(fibonacci(9)) 


#space optimised
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
print(fibonacci(9)) 
    
