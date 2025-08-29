# 1. Write a program to calculate the percentage of student based on marks of any 5 
# subjects. 
# Program to calculate percentage of 5 subjects

s1 = int(input("Enter marks of Subject 1: "))
s2 = int(input("Enter marks of Subject 2: "))
s3 = int(input("Enter marks of Subject 3: "))
s4 = int(input("Enter marks of Subject 4: "))
s5 = int(input("Enter marks of Subject 5: "))

total = s1+s2+s3+s4+s5
percentage= total /500
print("Total Marks =", total)
print("Percentage =", percentage, "%")
