print("=========check whether a number is positive, negative, or zero.=========")
a=int(input("enter a no1:"))
if a>0:
    print("a is postive number",a)
elif a<0:
    print("a is a negative number",a)
else:
    print("a is a zero",a)

print("===========check whether a number is even or odd.==============")
if a%2==0:
    print("even number",a)
else:
    print("odd number",a)
print("===============check if a person is eligible to vote (age ≥ 18).===============")
age=int(input("enter a number:"))
if age>=18:
    print("you are eligible for voting")
    
else:
    y=18-age
    print("you are eligible for voting after",y)
print("=======check if a student passed or failed based on marks.=======")
sname=input("enter a stuname:")
m1=int(input("enter a m1:"))
m2=int(input("enter a m2:"))
m3=int(input("enter a m3:"))
m4=int(input("enter a m4:"))
m5=int(input("enter a m5:"))
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35:
    print("you are passed")
else:
    print("you are failed")
print("=========find the largest of two numbers.===============")
x=int(input("enter a no1:"))
z=int(input("enter a no2:"))
if x>z:
    print(x," is a largest number")
else:
    print(z," is a largest number")
print("===========display grade (A, B, C, D, Fail) based on marks.============")
sname=input("enter a stuname:")
m1=int(input("enter a m1:"))
m2=int(input("enter a m2:"))
m3=int(input("enter a m3:"))
m4=int(input("enter a m4:"))
m5=int(input("enter a m5:"))
tot=m1+m2+m3+m4+m5
avg=tot/5
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35:
    print("you are pass")
    if avg>80 and avg<=100:
        print("A Grade")
    elif avg>60 and avg<=80:
        print("B Grade")
    elif avg>35 and avg<=60:
        print("C Grade")
    else:
        print("D Grade")
else:
    print("you are fail")
print("==========print the day name based on a number (1–7)=========")
day=int(input("enter a daynumber:"))
if day==1:
   print("sunday")
elif day==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print("wednesday")
elif day==5:
    print("thursday")
elif day==6:
    print("friday")
elif day==7:
    print("saturday")
print("==========whether a character is an alphabet, digit, or special character.==============")
char = input("Enter a character: ")
if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
    print("Alphabet")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special Character")
print("==========find the largest among three numbers.==========")
b=int(input("enter a no1:"))
c=int(input("enter a no2:"))
d=int(input("enter a no3:"))
if b>c and b>d:
    print(b,"is a largest number")
elif c>b and c>d:
    print(c,"is a largest number")
else:
    print(d,"is a largest number")
print("==========temperature (e.g., Hot, Warm, Cool, Cold).===========")
temperature = float(input("Enter the temperature in °C: "))

if temperature >= 35:
    print("Hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")
print("=========check whether a number is positive and even using nested if========")
s=int(input("enter a no1:"))
if s>0:
    print(s,"is a positive number")
    if s%2==0:
        print(s,"is a even number")
    else:
        print(s,"is odd number")
else:
    print(s,"is negative number")
print("=======to simulate a login system that checks username and password using nested if.=======")
correct_username = "Almas"
correct_password = "Almas123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username:
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")   
print("=======to check if a person is eligible for a job======")
age = int(input("Enter your age: "))
experience = input("Do you have experience? (yes/no): ")

if age > 18:
    if experience == "yes":
        print("You are eligible for the job.")
    else:
        print("You must have experience.")
else:
    print("You must be above 18.")
print("=========to check if a year is leap year or not using if-else=========")
year=int(input("enter a year:"))
if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
print("========== to check whether a student qualifies for a scholarship==========")
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))
if marks >= 85:
    if attendance >= 90:
        print("You qualify for the scholarship")
    else:
        print("You need at least 90percentage attendance")
else:
    print("You need at least 85 marks")