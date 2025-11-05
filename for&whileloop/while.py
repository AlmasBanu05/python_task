print("=========print numbers from 10 down to 1=========")
i=10
while i>=1:
    print(i)
    i=i-1
print("========sum of even digits in a numbers=========")
n=int(input("enter number for for even digits sum:"))
s=0
while n>0:
    d=n%10
    if d%2==0:
        s=s+d
    n//=10
print("sum of even digits:",s)
   
print("=====count how many digits are in a number======")
n=int(input("enter a number:"))
c=0
while n>0:
    c=c+1
    n//=10
print("count:",c)
print("========palindrome or not========")
p=int(input("enter a number:"))
t=p
r=0
while p>0:
    d=p%10
    r=r*10+d
    p//=10
if(t==r):
    print(t,"is a palindrome number")
else:
    print(t,"is not a palindrome number")
print("========find a reverse number=========")
x=int(input("enter a number:"))
t=x
r=0
while x>0:
    d=x%10
    r=r*10+d
    x//=10
print("reverse a number",r)
print("===========fibonacci===========")
print("fibonacci upto 100")
a=0
b=1
while a<=100:
    print(a)
    c=a+b
    a=b
    b=c
print("==========power manually==========")
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
r = 1
i = 0
while i < e:
    r *= b
    i += 1
print("Power result:", r)
print("=========digits of a numbers from last to frist=========")   
z=int(input("enter a number:"))
t=z
r=0
while z>0:
    d=z%10
    z//=10
    print("digits from last to first",d)
print("=========== Keep dividing a number by 2 until it becomes less than 1============")
n = float(input("Enter number to divide by 2: "))
c = 0
while n >= 1:
    n /= 2
    c += 1
print("Divisions:", c)
print("=======sum of squares of digits====")
n=int(input("enter a number:"))
s=0
while n>0:
    d=n%10
    s+=d*d
    n//=10
print("sum of squares",s)