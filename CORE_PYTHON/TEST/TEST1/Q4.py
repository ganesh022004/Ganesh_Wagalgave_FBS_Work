# Input values
area = float(input("Enter area of wall: "))
interior_rate = float(input("Enter cost of interior painting per unit area: "))
exterior_rate = float(input("Enter cost of exterior painting per unit area: "))

# Calculations
interior_cost = area * interior_rate
exterior_cost = area * exterior_rate
total_cost = interior_cost + exterior_cost

# Output
print("Interior Painting Cost =", interior_cost)
print("Exterior Painting Cost =", exterior_cost)
print("Total Painting Cost =", total_cost)
