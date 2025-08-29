gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender == "male":
    if age >= 21:
        print("Eligible for marriage")
    else:
        print("Not Eligible")
else:
    if gender == "female":
        if age >= 18:
            print("Eligible for marriage")
        else:
            print("Not Eligible")
    else:
        print("Invalid gender entered")
