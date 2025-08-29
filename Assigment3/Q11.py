total_amount = 0

ticket_price = float(input("Enter ticket price per person: "))

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    
    if age < 12:   # children discount
        pay = ticket_price * 0.70   # 30% discount
    elif age > 59:  # senior citizen discount
        pay = ticket_price * 0.50   # 50% discount
    else:
        pay = ticket_price   # full price
    
    print(f"Person {i} (Age {age}) has to pay: {pay}")
    total_amount += pay

print("\nTotal ticket amount for all 5 people:", total_amount)
