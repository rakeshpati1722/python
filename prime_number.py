n = int(input("enter the no:"))
if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("not")
            break
    else:
        print("yes")
        
else:
    print("not")