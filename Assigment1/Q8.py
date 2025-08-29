# 8. Convert days into years, weeks, days
days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7
print(years, "Years", weeks, "Weeks", remaining_days, "Days")
