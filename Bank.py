def showBalance(balance):
    return balance

def deposit(balance, amount):
    balance += amount
    return balance

def withdraw(balance, amount):
    balance -= amount
    return balance

amount = 0

balance = 0

while True:
    print("Bank Menu \n")
    choice = int(input("1. Show Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit \n"))
    if choice == 1:
        balance = showBalance(balance)
        print(f"Your balance is ${balance}. \n")
        continue
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = deposit(balance, amount)
        print(f"${amount} is added to your account. \n")
        continue
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        balance = withdraw(balance, amount)
        print(f"${amount} is withdrawn from your account. \n")
        continue
    elif choice == 4:
        break
    else:
        print("Invalid Choice! Try again")
        continue