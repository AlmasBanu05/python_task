import pandas as pd
data=[5,10,15,20]
df=pd.Series(data)
print(df)
df=pd.Series(data,index=['a','b','c','d'])
print(df)
print("==========Create a DataFrame=========")
d={"name":['ravi','kiran','meena'],"age":[22,25,28],"city":['chennai','bangalore','hyderabad']}
df=pd.DataFrame(d)
print(df)
print("==========Column Operations===========")
print("============= Print only the Name column============")
print(df["name"])
print("===========2.	Print Name and City columns together===========")
print(df[['name','city']])
print("=========Print the second row using loc=========")
print(df.loc[1])
print(df.iloc[1])
print("==========Row Operations==========")
print(df[0:2])
print("============Print only rows where Age is greater than 23============")
print(df[df['age']>23])
print("=========Add a New Column=========")
df['salary']=[30000,40000,50000]
print(df)
print("===========Increase the Age of all people by 1==========")
df['age']=df['age']+1
print(df)
print("=========Increase the Age of only Kiran by 1 using loc=========")
df.loc[df['name'] == 'kiran', 'age'] += 1
print(df)