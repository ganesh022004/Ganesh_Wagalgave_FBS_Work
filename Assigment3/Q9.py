s1=int(input("enter marks of subject 1"))
s2=int(input("enter marks of subject 2"))
s3=int(input("enter marks of subject 3"))
s4=int(input("enter marks of subject 4"))
s5=int(input("enter marks of subject 5"))
total=s1+s2+s3+s4+s5
percentage = (total / 500) * 100 

if(percentage>=70):
    grade="distination"
elif(percentage>=60):
    grade="first class"
elif(percentage>=50):
    grade="secound class"
elif(percentage>=40):
    grade="pass"
else:
    grade="fail"
print("the total is",total)
print("the persentage is ",percentage)
print("grade is :",grade)