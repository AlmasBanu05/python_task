# print("=========Reverse a given list in Python==========")
# l=[100,200,300,400,500]
# print("reverse given list:",l[::-1])
# print("=========Concatenate two lists==========")
# l1=["hello","madam"]
# l2=["dear","sir"]
# l3=l1+l2
# print(l3)
# print("=======3. Remove empty strings from the list of strings=======")
# l4 = ["Pen", "", "Pencil", "Eraser", "", "Scale"]
# l5=[]
# for i in l4:
#     if i!="":
#         l5.append(i)
# print(l5)
# print("========Write a Python program to convert a string to a list==========")
# n=input("enter a string:")
# res=list(n)
# print(res)
# print("=========Check if a list contains an element=========")
# l = [1,2,3,'a','b','c']
# if l!="":
#         print("list contain element")
# else:
#         print("list does not element")
# print("=====Remove all elements from a list=====")
# n=int(input("enter a range:"))
# l=[]
# for i in range(0,n):
#     e=input("enter a elements:")
#     l.insert(i,e)
# print(l)
# l1=l.clear()
# print("after remove:",l1)
# print("===== Count the occurrence of a specific object in a list =====")
# pets = ['dog', 'cat', 'fish', 'fish', 'cat']
# element = input("Enter the element to count: ")
# count = 0
# for item in pets:
#     if item == element:
#         count += 1
# print(f"{element} occurs {count} times in the list.")
# print("=========Return the length of a list=========")
# n=int(input("enter a range:"))
# l=[]
# for i in range(0,n):
#     e=input("enter a elements:")
#     l.insert(i,e)
# print(l)
# l2=len(l)
# print(l2)
# print("=========Insert a value at a specific index in an existing list========")
# l=[1,"almas",34.5,"banu"]
# l.insert(2,"abees")
# print(l)
# print("10. Clone or copy a list")
# d=[5,10,15,20]
# e=d.copy()
# print(e)

# print("11. Extend a list without append")
# f=[1,2,3]
# g=[4,5,6]
# f.extend(g)
# print(f)
print("1. Create a list of 5 numbers and print it")
a=[]
for i in range(5):
    n=(input("Enter number: "))
    a.append(n)
print(a)

print("2. Find the length of a list using len()")
b=[]
x=int(input("How many elements: "))
for i in range(x):
    b.append(input("Enter element: "))
print(len(b))

print("3. Access elements using positive and negative indexes")
c=[]
y=int(input("How many elements: "))
for i in range(y):
    c.append(input("Enter element: "))
i1=int(input("Enter positive index: "))
i2=int(input("Enter negative index: "))
print(c[i1], c[i2])

print("4. Update the 3rd element of a list")
d=[]
for i in range(5):
    d.append(input("Enter element: "))
val=input("Enter new value for 3rd element: ")
d[2]=val
print(d)

print("5. Delete an element from a list using del")
e=[]
n=(input("How many elements: "))
for i in range(n):
    e.append(input("Enter element: "))
idx=int(input("Enter index to delete: "))
del e[idx]
print(e)

print("6. Append a new element to the list using append()")
f=[]
n=int(input("How many elements: "))
for i in range(n):
    f.append(input("Enter element: "))
val=input("Enter element to append: ")
f.append(val)
print(f)

print("7. Insert an element at a specific position using insert()")
g=[]
n=int(input("How many elements: "))
for i in range(n):
    g.append(input("Enter element: "))
pos=int(input("Enter position: "))
val=input("Enter value: ")
g.insert(pos,val)
print(g)

print("8. Remove an element using remove()")
h=[]
n=int(input("How many elements: "))
for i in range(n):
    h.append(input("Enter element: "))
val=input("Enter value to remove: ")
if val in h:
    h.remove(val)
print(h)

print("9. Remove the last element using pop()")
i=[]
n=int(input("How many elements: "))
for x in range(n):
    i.append(input("Enter element: "))
i.pop()
print(i)

print("10. Clear all elements using clear()")
j=[]
n=int(input("How many elements: "))
for x in range(n):
    j.append(input("Enter element: "))
j.clear()
print(j)

print("11. Print all elements of a list using for loop")
k=[]
n=int(input("How many elements: "))
for x in range(n):
    k.append(input("Enter element: "))
for x in k:
    print(x)

print("12. Find the sum of all elements using sum()")
l=[]
n=int(input("How many numbers: "))
for x in range(n):
    l.append(int(input("Enter number: ")))
print(sum(l))

print("13. Find the maximum and minimum values using max() and min()")
m=[]
n=int(input("How many numbers: "))
for x in range(n):
    m.append(int(input("Enter number: ")))
print(max(m),min(m))

print("14. Check if an element is not in a list")
n1=[]
n=int(input("How many numbers: "))
for x in range(n):
    n1.append(int(input("Enter number: ")))
x=int(input("Enter element to check: "))
print(x not in n1)

print("15. Count how many times an element appears using count()")
o=[]
n=int(input("How many elements: "))
for x in range(n):
    o.append(input("Enter element: "))
val=input("Enter value to count: ")
print(o.count(val))

print("16. Find the index of a specific element using index()")
p=[]
n=int(input("How many elements: "))
for x in range(n):
    p.append(input("Enter element: "))
val=input("Enter value to find index: ")
if val in p:
    print(p.index(val))
else:
    print("Not found")

print("17. Reverse a list using reverse()")
q=[]
n=int(input("How many elements: "))
for x in range(n):
    q.append(input("Enter element: "))
q.reverse()
print(q)

print("18. Sort a list in ascending and descending order using sort()")
r=[]
n=int(input("How many numbers: "))
for x in range(n):
    r.append(int(input("Enter number: ")))
r.sort()
print(r)
r.sort(reverse=True)
print(r)

print("19. Copy one list to another using copy()")
s=[]
n=int(input("How many elements: "))
for x in range(n):
    s.append(input("Enter element: "))
t=s.copy()
print(t)

print("20. Print only even numbers from a list")
u=[]
n=int(input("How many numbers: "))
for x in range(n):
    u.append(int(input("Enter number: ")))
for x in u:
    if x%2==0:
        print(x)

print("21. Print only odd numbers from a list")
v=[]
n=int(input("How many numbers: "))
for x in range(n):
    v.append(int(input("Enter number: ")))
for x in v:
    if x%2!=0:
        print(x)
print("21. Add two lists using + operator")
a=[]
b=[]
n=int(input("Enter size of first list: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
m=int(input("Enter size of second list: "))
for i in range(m):
    b.append(int(input("Enter number: ")))
print(a+b)

print("22. Repeat list elements using * operator")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
t=int(input("Enter number of times to repeat: "))
print(a*t)

print("23. Check if an element exists in a list using in")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
x=input("Enter element to check: ")
print(x in a)

print("24. Slice a list (first 3 and last 3 elements)")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
print(a[:3])
print(a[-3:])

print("25. Find the largest 2 numbers in a list")
a=[]
n=int(input("Enter how many numbers: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
a.sort()
print(a[-1], a[-2])

print("26. Find duplicate elements in a list")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
dup=[]
for i in a:
    if a.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)

print("27. Remove duplicate elements from a list")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

print("28. Merge two sorted lists into one sorted list")
a=[]
b=[]
n=int(input("Enter size of first sorted list: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
m=int(input("Enter size of second sorted list: "))
for i in range(m):
    b.append(int(input("Enter number: ")))
c=a+b
c.sort()
print(c)

print("29. Create a list of squares of numbers from 1 to 10")
a=[]
for i in range(1,11):
    a.append(i*i)
print(a)

print("30. Separate even and odd numbers into two lists")
a=[]
n=int(input("Enter how many numbers: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

print("31. Create a nested list (list inside a list)")
a=[]
for i in range(2):
    b=[]
    for j in range(2):
        b.append(input("Enter element: "))
    a.append(b)
print(a)

print("32. Access elements from a nested list")
a=[[1,2],[3,4],[5,6]]
r=int(input("Enter row index: "))
c=int(input("Enter column index: "))
print(a[r][c])

print("33. Flatten a nested list")
a=[]
for i in range(2):
    b=[]
    for j in range(2):
        b.append(int(input("Enter number: ")))
    a.append(b)
flat=[]
for i in a:
    for j in i:
        flat.append(j)
print(flat)

print("34. Find common elements between two lists")
a=[]
b=[]
n=int(input("Enter size of first list: "))
for i in range(n):
    a.append(input("Enter element: "))
m=int(input("Enter size of second list: "))
for i in range(m):
    b.append(input("Enter element: "))
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

print("35. Find elements present in one list but not in another")
a=[]
b=[]
n=int(input("Enter size of first list: "))
for i in range(n):
    a.append(input("Enter element: "))
m=int(input("Enter size of second list: "))
for i in range(m):
    b.append(input("Enter element: "))
diff=[]
for i in a:
    if i not in b:
        diff.append(i)
print(diff)

print("36. Remove all occurrences of a specific element from a list")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
x=input("Enter element to remove: ")
while x in a:
    a.remove(x)
print(a)

print("37. Convert a list into a tuple")
a=[]
n=int(input("Enter size of list: "))
for i in range(n):
    a.append(input("Enter element: "))
t=tuple(a)
print(t)

print("38. Find the average of list elements")
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
avg=sum(a)/len(a)
print(avg)

print("39. Count positive, negative, and zero numbers in a list")
a=[]
n=int(input("Enter how many numbers: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
pos=neg=zero=0
for i in a:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1
print(pos,neg,zero)
print("40. Find product of all elements in a list")
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    a.append(int(input("Enter number: ")))
p=1
for i in a:
    p=p*i
print(p)

