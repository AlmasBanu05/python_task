print("1. Create a tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
print(t)

print("2. Find size of a tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
print(len(t))

print("3. Sort tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
print(tuple(sorted(t)))

print("4. Tuple with different data types")
s=input("Enter string: ")
i=int(input("Enter integer: "))
f=float(input("Enter float: "))
t=(s,i,f)
print(t)

print("5. Unpack tuple")
l=[input("Enter first: "),input("Enter second: "),input("Enter third: ")]
t=tuple(l)
a,b,c=t
print(a,b,c)

print("6. Tuple to string")
n=int(input("Enter number of characters: "))
l=[]
for i in range(n):
    e=input("Enter character: ")
    l.append(e)
t=tuple(l)
s=''.join(t)
print(s)

print("7. 4th element and 4th from last")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
if len(t)>=4:
    print("4th element:",t[3])
    print("4th from last:",t[-4])
else:
    print("Less than 4 elements")

print("8. Repeated items in tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
r=[]
for i in t:
    if t.count(i)>1 and i not in r:
        r.append(i)
print(r)

print("9. Check element exists in tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
x=input("Enter element to check: ")
print(x in t)

print("10. Convert list to tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
print(t)

print("11. Remove item from tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
x=input("Enter item to remove: ")
l=list(t)
if x in l:
    l.remove(x)
t=tuple(l)
print(t)

print("12. Slice tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
a=int(input("Enter start index: "))
b=int(input("Enter end index: "))
print(t[a:b])

print("13. Index of item in tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
x=input("Enter element to find index: ")
if x in t:
    print(t.index(x))
else:
    print("Not found")

print("14. Length of tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
print(len(t))

print("15. Reverse tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter element: ")
    l.append(e)
t=tuple(l)
print(t[::-1])

print("16. Convert string list to tuple")
n=int(input("Enter number of elements: "))
l=[]
for i in range(n):
    e=input("Enter string element: ")
    l.append(e)
t=tuple(l)
print(t)
