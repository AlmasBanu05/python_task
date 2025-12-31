print("================create new dictiionary===============")
student={"name":"almas","age":20,"marks":98}
print("==============Print the value of the key 'name'===========")
print("Name:",student["name"])
print("==============Add a new key 'grade' with value ============")
student["grade"]="A"
print("after add new key values",student)
print("==============Update the value of 'marks'=============")
s1={"marks":99}
student.update(s1)
print("after updating students",student)
print("============Remove the key 'age'===============")
student.pop("age")
print("after removing age:",student)
print("===============Check whether the key 'email' exists==================")
if "email" in student:
    print("email exist")
else:
    print("email does not exist")
print("Keys:", student.keys())
print("values:",student.values())
print("================all key-values using for loop======================")
for key,value in student.items():
    print(key,":",value)

print("=================all key-values using for loop==================")
students={}
num=int(input("enter a range:"))
for i in range(num):
    k=input("enter a key:")
    v=input("enter a values:")
    students[k]=v
print("dictionary elements:",students)
print("================Dictionary with 5 subjects and find total marks================")
subjects = {
    "Maths": 80,
    "Science": 85,
    "English": 75,
    "Computer": 90,
    "Tamil": 88
}
total_marks = sum(subjects.values())
print("Total Marks:", total_marks)
print("============Find the maximum value=============")
print("Maximum Marks:", max(subjects.values()))
print("================== Copy a dictionary==============")
print("count no of dictionary key",len(subjects))
s2=subjects.copy()
print(s2)
print("================Convert two lists into a dictionary=================")
l1=[1,2,3,4]
l2=["almas","banu","abees","yasin"]
new_dict = dict(zip(l1, l2))
print(new_dict)


print("===============Increase each salary by 10%=============")
emp={"almas":40000,"abees":60000,"yasin":100000}
print(emp)

for e in emp:
    emp[e] = emp[e] * 1.10

print("Updated Salaries:", emp)
