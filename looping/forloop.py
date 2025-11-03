print("===========print numbers from 1 to 20===========")
for i in range(1,21):
     print(i)
print("==========print all even numbers===========")
for i in range(2,51,2):
     print(i)
print("=========print all odd numbers=========")
for i in range(1,51,2):
     print(i)
print("square of numbers")
for i in range(1,15):
     print("square:",i,"=",i**2)
print("=======cube of numbersfrom 1 to 10")
for i in range(1,11):
     print("cube of number:",i,"=",i**3)
print("=========print number from 10 down to 1======")
for i in range(10,0,-1):
     print(i)
print("======multiplication table==========")
for i in range(1,11):
     print("5*",i,"=",5*i)
print("all character of the string one by one=========")
a="hello"
for i in a:
     print(i)
print("========number divisible by 3 between 1 to 30====")
for i in range(1,31):
     if(i%3==0):
          print(i)