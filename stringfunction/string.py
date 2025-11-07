# print("==========Write a program to concatenate a given string to the end of another string.=============")
# a=input("enter a string:")
# b=input("enter a string:")
# c=a+b
# print("concatenate:",c)
# print("==========Write a program to test if a given string contains the specified sequence of char values.=============")
# a=input("enter a string:")
# print("alm" in a)
# print("============Write a program to convert all the characters in a string to lowercase.==============")
# a=input("enter a string:")
# print("convert to lowercase",a.lower())
# print("==========Write a program to trim any leading or trailing whitespace from a given string.=========")
# a=input("enter a string:")
# print("trim whitespace:",a.strip())
# print("========Write a program to reverse a string.=========")
# a=input("enter a string:")
# print("reverse:",a[::-1])
# print("=======replace all spaces with underscores======")
# print("=======middle three characters =======") 
# a=input("enter a string:")
# s=len(a)//2
# r=a[s-1:s+2]
# print("middle three character",r)
# print("========first and last letter to capital=========")
# a = input("Enter a word: ")
# b = ""
# for i in range(len(a)):
#     if not a[i].isdigit() and (i == 0 or i == len(a) - 1):
#         b += a[i].upper()
#     else:
#         b += a[i]
# print(b)
# print(" Write a program to get the length of a given string.")
# a = input("Enter a string: ")
# print("Length:", len(a))

# print(" Write a program to print the number of occurrences of a given string with repetition.")
# b = "I am New to this office but not New to remove digits in strings"
# x = input("Enter the word to count: ")
# print("Occurrences:", b.split().count(x))

# print(" Write a program to count the number of words in a string.")
# a = input("Enter a string: ")
# print("Number of words:", len(a.split()))

# print(" Write a program to replace a specified character with another character.")

# x = input("Enter character to replace: ")
# y = input("Enter new character: ")
# print("New string:",x.replace(x, y))

# print("How to count vowels in a string?")
# a = input("Enter a string: ")
# v = "aeiouAEIOU"
# c = 0
# for i in a:
#     if i in v:
#         c += 1
# print("Number of vowels:", c)

# print(" How to check if a string contains only whitespace?")
# a = input("Enter a string: ")
# if a.isspace():
#     print("String has only whitespace")
# else:
#     print("String does not contain only whitespace")

# print(" How to remove all digits from a string?")
# a = input("Enter a string: ")
# b = ""
# for i in a:
#     if not i.isdigit():
#         b += i
# print("String without digits:", b)
# print(" Find the length of your name using len()")
# n=input("enter a string")
# print("Length of name:", len(n))

# print(" Convert the string to uppercase using upper()")
# print("Uppercase:", n.upper())

# print(" Convert the string to lowercase using lower()")
# print("Lowercase:", n.lower())

# print(" Count how many times the letter 'a' appears using count()")
# print("Count of 'a':", n.count('a'))

# print(" Check if a string starts with 'Hello' using startswith()")
# g = "Hello, welcome to Python"
# print("Starts with 'Hello':", g.startswith("Hello"))

# print(" Check if a string ends with '.com' using endswith()")
# w = "www.example.com"
# print("Ends with '.com':", w.endswith(".com"))

# print("Find the position of the word 'Python' using find()")
# s = "I am learning Python programming."
# print("Position of 'Python':", s.find("Python"))
print("Replace the word 'Java' with 'Python' in a sentence using replace().")
a = input("Enter a sentence: ")
print(a.replace("Java", "Python"))

print("Remove extra spaces from both sides of a string using strip().")
a = input("Enter a string with extra spaces: ")
print(a.strip())

print("Capitalize the first letter of a sentence using capitalize().")
a = input("Enter a sentence: ")
print(a.capitalize())

print("Split a sentence into words using split().")
a = input("Enter a sentence: ")
print(a.split())

print("Join a list of words using join().")
a = ["Python", "is", "fun"]
print(" ".join(a))

print("Check if a string has only alphabets using isalpha().")
a = input("Enter a string: ")
print(a.isalpha())

print("Check if a string has only numbers using isdigit().")
a = input("Enter a string: ")
print(a.isdigit())

print("Check if a string has both letters and numbers using isalnum().")
a = input("Enter a string: ")
print(a.isalnum())

print("Check if all characters in a string are in lowercase using islower().")
a = input("Enter a string: ")
print(a.islower())

print("Check if all characters in a string are in uppercase using isupper().")
a = input("Enter a string: ")
print(a.isupper())

print("Swap lowercase to uppercase and vice versa using swapcase().")
a = input("Enter a string: ")
print(a.swapcase())

print("Convert every word’s first letter to uppercase using title().")
a = input("Enter a sentence: ")
print(a.title())

print("Check if a string contains only spaces using isspace().")
a = input("Enter a string: ")
print(a.isspace())

print("Count the number of vowels in a given string.")
a = input("Enter a string: ")
v = "aeiouAEIOU"
c = 0
for i in a:
    if i in v:
        c += 1
print("Vowel count:", c)

print("Check if a given word is a palindrome.")
a = input("Enter a word: ")
b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not a palindrome")

print("Remove all digits from a given string.")
a = input("Enter a string: ")
b = ""
for i in a:
    if not i.isdigit():
        b += i
print(b)

print("Replace all spaces in a sentence with underscores.")
a = input("Enter a sentence: ")
print(a.replace(" ", "_"))

print("Extract only numbers from a mixed string like 'abc123xyz'.")
a = input("Enter a string: ")
b = ""
for i in a:
    if i.isdigit():
        b += i
print("Numbers:", b)

print("Find and print all words in a sentence that start with a capital letter.")
a = input("Enter a sentence: ")
for i in a.split():
    if i[0].isupper():
        print(i)

print("Input a sentence and print how many times each letter occurs.")
a = input("Enter a sentence: ")
a = a.replace(" ", "")
for i in sorted(set(a)):
    print(i, "=", a.count(i))

print("Remove all punctuation marks from a given sentence.")
a = input("Enter a sentence: ")
p = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
b = ""
for i in a:
    if i not in p:
        b += i
print(b)
