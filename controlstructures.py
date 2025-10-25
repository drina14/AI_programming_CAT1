number = int(input("Enter a number: "))

if number < 0:
    print("invalid input - negative numbers not allowed")

elif number % 2==0:
    print (f"the number {number} is even. ")
else: print (f"the number {number} is odd. ")
