
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

# Area calculation
area = (length * breadth) + (0.5 * 3.14 * radius * radius)

# Perimeter calculation
perimeter = (2 * breadth) + length + (3.14 * radius)

print("Area =", area)
print("Perimeter =", perimeter)
