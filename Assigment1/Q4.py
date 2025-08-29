# Simple Interest Program

p = float(input("Enter principal: "))
t = float(input("Enter time (in years): "))
r = float(input("Enter rate (%): "))

si = (p * t * r) / 100
print("Simple Interest =", si)
