menu = {"Sandwich" : 2.00,
        "Fries" : 3.00,
        "Lamb chops" : 9.00,
        "Jalapenos" : 4.00}

cart = []
total = 0

print("------ MENU ------")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("------------------")

while True:
    food = input("Select your choice or q to quit: ")

    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)

print(f"Your total is ${total}")