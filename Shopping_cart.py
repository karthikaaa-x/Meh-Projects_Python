foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or q to exit: ")
    if food == "q":
        break
    else:
        foods.append(food)
        price = float(input("Enter price of food: "))
        prices.append(price)

for i in prices:
    total += i

print(f"Total cost of shopping cart is ${total:.2f}")