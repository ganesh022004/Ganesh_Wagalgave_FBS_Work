# 5. Compound Interest
P = float(input("Enter Principal: "))
T = float(input("Enter Time (in years): "))
R = float(input("Enter Rate: "))
CI = P * (pow((1 + R/100), T)) - P
print("Compound Interest =", CI)
