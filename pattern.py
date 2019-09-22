#pattern programing using python

    *
   ***
  *****
 *******
*********

for row in range(5):
    for col in range(9):
        if ((row == 4)or (row == 3 and (col > 0 and col < 8)) or (row == 2 and (col > 1 and col < 7)) or (row == 1 and (col > 2 and col < 6)) or (row == 0 and col == 4)):
            print("*", end="")
        else:
            print(end = " ")
    print() 


1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

a = "12345"
b = len(a)
for row in range(b):
    for col in range(row + 1):
        print(a[row],end =' ')
    print()

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

a = "12345"
b = len(a)
for row in range(b):
    for col in range(row + 1):
        print(a[col],end =' ')
    print()