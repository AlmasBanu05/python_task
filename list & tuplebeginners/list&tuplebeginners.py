print("========1.Create a list of 5 of your favorite fruits.=========")
l=["apple","mango","pineapple","orange","strawberry"]
print(l)
print("=========2.Add a new fruit to the list using a list method=========")
l.append("cherry")
print(l)
print("=======3.Remove one fruit from the list========")
l.remove("strawberry")
print("Remove one fruit from the list",l)
print("========4.Print the number of fruits in your list=========")
print("Print the number of fruits in your list:",l)
print("=========5.Print all the fruits one by one using a for loop========")
l=["apple","mango","pineapple","orange","strawberry"]
for i in l:
   print(i)
print("=======6.Reverse the list and print it======")
print("Reverse the list and print it",l[::-1])
print("=========7.	Sort the list alphabetically and print it===========")
l1=["apple","Mango","pineapple","Orange","strawberry"]
l1.sort()
print("sort:",l1)
print("========8 Check if a particular fruit (like Apple) is in the list========")
l1=["Mango","pineapple","Orange","strawberry"]
for i in l1:
    if i=="Apple":
        print("list contain Apple")
else:
        print("list does not contain Apple")
print(l1)
print("=======Create a tuple of 5 of your favorite colors==========")
t=("red","blue","pink","orange","yellow")
print(t)
print("=========Print the first and last color from the tuple=========")
t=("red","blue","pink","orange","yellow")
print("first value in the list:",t[0])
print("last element in list",t[-1])
print("======Find the length of the tuple======")
t=("red","blue","pink","orange","yellow")
print("length:",len(t))
print("=========Count how many times a particular color appears in the tuple==========")
t=("red","blue","pink","orange","yellow","red")
count=0
for i in t:
    if i=="red":
        count=count+1
print("count of red:",count)
print("=========Print all colors one by one using a for loop========")
t=("red","blue","pink","orange","yellow","red")
for i in t:
    print(i)
print("==========Combine two tuples of colors and print the result==========")
t=("red","blue","pink","orange","yellow","red")
t1=("green","violet","black","white")
t2=t+t1
print("combine two tuples:",t2)
print("=========Find the maximum and minimum value from a tuple of numbers========")
t1=(1,4,6,78,34,2)
print("maximum values in the list",max(t1))
print("minimum value in the list:",min(t1))
print("========Try to change a value in the tuple and observe what happens=======")
t1=(1,4,6,78,34,2)
t1[2]=3
print("change the value in tuple",t1)
