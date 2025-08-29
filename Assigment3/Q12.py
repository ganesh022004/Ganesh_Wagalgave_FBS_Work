num = int(input("Enter a 3-digit number: "))

# Reverse the number
reverse = int(str(num)[::-1])

# Check palindrome
if num == reverse:
    print(num, "is a Palindrome number.")
else:
    print(num, "is NOT a Palindrome number.")
