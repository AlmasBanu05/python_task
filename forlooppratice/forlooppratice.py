print("========Write a Python program to find and print all prime numbers between 1 and 100 using a for loop.=======")
count = 0
for i in range(1, 101):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
print("Total prime numbers:", count)

print("======Write a program to print the following pyramid pattern using nested for loops======")
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print("======= Write a Python program to calculate the electricity bill based on the following conditions======")
u = int(input("Enter units consumed:"))
if u <= 100:
    amount = u * 1.5
elif u <= 200:
    amount = 100 * 1.5 + (u - 100) * 2.5
elif u <= 300:
    amount = 100 * 1.5 + 100 * 2.5 + (u - 200) * 4.0
else:
    amount = 100 * 1.5 + 100 * 2.5 + 100 * 4.0 + (u - 300) * 5.0
if amount > 1000:
    amount += amount * 0.10
print("Total Bill:", amount)
print("=======Write a program to print this pattern using nested for loops========")
n = 5
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()
print("=========Multiplication Table 1-10")
for i in range(1, 11):          
    for j in range(1, 11):    
        print(f"{i*j:4}", end="")  
    print() 
print("=======Write a Python program to print Pascal’s Triangle up to n rows.=======")
n = 5
for i in range(n):
    print(' ' * (n - i - 1), end='')
    value = 1
    for j in range(i + 1):
        print(value, end=' ')
        value = value * (i - j) // (j + 1)
    print()

