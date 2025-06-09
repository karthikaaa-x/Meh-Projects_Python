principal = float(input("Enter principal amount: "))

r = float(input("Enter rate of interest: "))

time = int(input("Enter time in years: "))

total_amount = principal * pow((1 + r/100),time)

print(f"Balance after {time} is ${total_amount:.2f}")