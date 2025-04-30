name="My name is kashish. My age is 22."
print(name)

#string-capitalize, replace, find, count, length, slicing indexing, endswith
print(name.startswith("My name is"))

name1="apple"
print(name1[-3:-1])

count="$ my name is $ 98$"
print(count.count("$"))

marks=int(input("enter your marks :"))
if(marks >= 90):
    grade="A"
elif(marks >= 80 and marks < 90):
    grade="B"
else:
    grade="C"
print("your grade is-", grade)

#nesting
age=int(input("enter your age :"))
if(age>=25):
    if(age>=80):
        print("you cannot cook")
    else:
        print("you can cook")

num=int(input("enter a number : "))
if(num%2==0):
    print("even")
else:
    print("odd")

A=5
B=10
C=2

print(max(A,B,C))





