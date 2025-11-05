print(" Print all numbers between 1 and 100 that are divisible by 6 but not by 9")
for i in range(1, 101):
    if i % 6 == 0 and i % 9 != 0:
        print(i, end=' ')
print("\n")

print(" Find the sum of all odd numbers from 1 to 50")
s = 0
for i in range(1, 51):
    if i % 2 != 0:
        s = s + i
print("Sum of odd numbers:", s)
print("\n")

print(" Count how many numbers between 1 and 200 are divisible by both 4 and 6")
count = 0
for i in range(1, 201):
    if i % 4 == 0 and i % 6 == 0:
        count = count + 1
print("Count:", count)
print("\n")

print(" Print the multiplication table of a given number (1 to 10)")
n = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
print("\n")

print(" Find the factorial of a given number")
n = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial:", fact)
print("\n")

print(" Print all prime numbers between 1 and 50")
for num in range(2, 51):
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 0:
        print(num, end=' ')
print("\n")

print(" Calculate the sum of digits of a number")
n = int(input("Enter a number: "))
s = 0
temp = n
while temp > 0:
    d = temp % 10
    s = s + d
    temp = temp // 10
print("Sum of digits:", s)
print("\n")

print(" Count how many numbers between 1 and 500 are perfect cubes")
count = 0
for i in range(1, 501):
    a = 1
    while a * a * a <= i:
        if a * a * a == i:
            count = count + 1
            break
        a = a + 1
print("Perfect cubes count:", count)
print("\n")

print("Print the reverse of a number")
n = int(input("Enter a number to reverse: "))
rev = 0
temp = n
while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp = temp // 10
print("Reverse:", rev)
print("\n")

print(" Print numbers from 1 to 100 but skip numbers ending with digit 5")
for i in range(1, 101):
    if i % 10 == 5:
        continue
    print(i, end=' ')
print()
