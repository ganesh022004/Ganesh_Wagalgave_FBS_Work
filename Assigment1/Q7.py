import math

# Input values
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Step 1: Calculate discriminant
d = b**2 - 4*a*c

# Step 2: Check cases
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Two different Real Roots =", root1, "and", root2)

elif d == 0:
    root = -b / (2*a)
    print("Both Roots are Same =", root)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex Roots =", real, "+", imag, "i  and", real, "-", imag, "i")
