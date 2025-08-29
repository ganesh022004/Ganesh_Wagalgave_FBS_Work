#  Q3: Convert distance given in feet and inches into meter and centimeter
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))
total_inches = (feet * 12) + inches
cm = total_inches * 2.54
meters = cm / 100
print("Distance in centimeters =", cm)
print("Distance in meters =", meters)