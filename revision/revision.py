print("=========1.	Create 5 variables of different data types (int, float, str, bool, list)=========")
sname="almas"
sage=20
height=143.7
is_student=False
hobbies=["playing","reading","cooking"]
print("name:",sname)
print(type(sname))
print("age:",sage)
print(type(sage))
print("height:",height)
print(type(height))
print("is_student:",is_student)
print(type(is_student))
print("name:",hobbies[1])
print(type(hobbies))
print("=========Print a sentence using variables=======")
name=input("enter a name:")
age=int(input("enter a age:"))
print("my name is",name,"and my age is",age)
print("=========print their sum, difference, product, and quotient======")
a=int(input("enter a n01:"))
b=int(input("enter a no2:"))
print("Sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("quotient",a/b)
print("=========combining string and integer properly using f-string (avoid type error)========")
s=input("enter a string:")
b=int(input("enter a n01:"))
print(f"string and integer{s}{b}")
print("========Use arithmetic operators to find=========")
x=int(input("enter a no1:"))
y=int(input("enter a no2:"))
z=int(input("enter a no3:"))
print("Square of a number:",x**2)
print("cube of another number:",y**3)
tot=x+y+z
avg=tot/3
print("average of three number",avg)
print("========relational operators========")
x=int(input("enter a no1:"))
y=int(input("enter a no2:"))
z=int(input("enter a no3:"))
print("greater:",x>y)
print("lesser:",x<y)
print("greater than or equal to:",z>=y)
print("lesser than or equal to:",z<=y)
print("equal to equalto:",z==y)
print("not equal to:",x!=y)
print("==========logical operator==========")
number = int(input("enter a number:"))
if number > 0 and number % 2 == 0:
    print("The number is positive and even")
elif number<0 or number==0:
    print("The number is negative or zero ")
else:
    print("enter a proper input")
print("=========to swap two variables without using a third variable ==========")
a = 5
b = 10
print("Before swapping: a =", a, "b =", b)
a = a + b  
b = a - b  
a = a - b  
print("After swapping: a =", a, "b =", b)
print("=========comparsion=========")
x=int(input("enter a no1:"))
y=int(input("enter a no2:"))
if x>b:
    print(x,"is a greater")
elif y>x:
    print(y,"is a greater")
else:
    print(x,"and",y,"both are equal")
print("=========odd or even==========")
number = int(input("enter a number:"))
if number%2==0:
    print(number,"is a even number")
else:
    print(number,"is a odd number")
print("=========positive, negative, or zero (use elif)============")
x=int(input("enter a no1:"))
if x>0:
    print(x,"is a positive number")
elif x<0:
    print(x,"is negative number")
else:
    print(x,"is a zero")
print("==========student's mark============")
m1=int(input("enter a m1:"))
m2=int(input("enter a m2:"))
m3=int(input("enter a m3:"))
m4=int(input("enter a m4:"))
m5=int(input("enter a m5:"))
total=m1+m2+m3+m4+m5
average=total/5
if average>=90 and average<=100:
    print("A Grade")
elif average>=75 and average<90:
    print("B Grade")
elif average>=50 and average<75:
    print("C Grade")
else:
    print("fail")
print("==========leapyaer or not==========")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
print("=======vote eligiblity=========")
age=int(input("enter a number:"))
if age>=18:
    print("you are eligible for voting")
    
else:
    res=18-age
    print("you are eligible for voting after",res)
print("===========three numbers and prints which one is the largest============")
b=int(input("enter a no1:"))
c=int(input("enter a no2:"))
d=int(input("enter a no3:"))
if b>c and b>d:
    print(b,"is a largest number")
elif c>b and c>d:
    print(c,"is a largest number")
else:
    print(d,"is a largest number")
print("==========nested if pos or neg or zero")
if s>0:
    print(s,"is a positive number")
    if s%2==0:
        print(s,"is a even number")
    else:
        print(s,"is odd number")
elif s<0:
     print(s,"is a negative number")
else:
    print(s,"is a zero")
print("==========nested if ==========")
age=int(input("enter a age:"))
if age>0:
    if age<13:
        print("child")
    elif age >=13 and age<=19:
        print("Teen")
    elif age>=20 and age<60:
        print("adult")
    else:
        print("senior citizen")
else:
    print("please enter a proper age!!!")
print("==========checks whether a character is a vowel or consonant===========")
letter = input("Enter a single alphabet letter: ")
letter = letter.lower()
if len(letter) != 1 or not letter.isalpha():
    print("Invalid input. Please enter a single alphabet letter.")
elif letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
print("======three subject marks =======")
m1=int(input("enter a m1:"))
m2=int(input("enter a m2:"))
m3=int(input("enter a m3:"))
tmark=m1+m2+m3
amark=tmark/3
if m1>=40 and m2>=40 and m3>=40:
    print("pass")
    if amark>=90 and amark<=100:
        print("A Grade")
    elif amark>=70 and amark<90:
        print("B Grade")
    elif amark>=40 and amark<70:
        print("C Grade")
    else:
        print("D Grade")
else:
    print("fail")