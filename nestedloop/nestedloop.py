print("Write a program to print Right Triangle")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

print("Write a program to print Left Triangle")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

print("Write a program to print Square")
n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

print("Write a program to print 8")
n=int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("Write a program to print Hollow square")
n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("Write a program to print Hollow Right Triangle")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("Write a Program to Print Inverse Left Triangle")
n=int(input("Enter number of rows: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

print("Write a Program to Print Inverse Right Triangle")
n=int(input("Enter number of rows: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print("Write a program to Print the patterns as shown below")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
