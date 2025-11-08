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
print("9. Various Number and Alphabet Patterns")

print("Pattern 9.1 Number Triangle")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("Pattern 9.2 Inverse Number Triangle")
n=int(input("Enter number of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("Pattern 9.3 Left Number Triangle")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("Pattern 9.4 Alphabet Increasing Block")
n=int(input("Enter number of rows: "))
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
    print()
    ch+=1

print("Pattern 9.5 Continuous Alphabet Triangle")
n=int(input("Enter number of rows: "))
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
        ch+=1
    print()

print("Pattern 9.6 Repeated Alphabet Triangle")
n=int(input("Enter number of rows: "))
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
    print()
    ch+=1

print("Pattern 9.7 Alphabet Pyramid")
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()