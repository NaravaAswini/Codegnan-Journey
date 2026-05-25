# Simple ATM PIN Check Program

correct_pin = "1234"
attempts_left = 3
balance=10000
while attempts_left > 0:
    pin = input("Enter ATM PIN: ")
    if pin == correct_pin:
        print("PIN correct. Access Granted.")
        amount = int(input("Enter amount to withdraw: "))
        if amount<=balance:
            balance=balance-amount
            print("collect cash")
            print("ramining bal:",balance)
        else:
            print("your balance is insufficient")
            print("enter sufficient balance")
    elif:
        print("enter amount to deposite:")
        balance=balance+deposite
        print("amount is added")
        print("your balance is:",balance)
        break
    else:
        attempts_left -= 1
        print("Wrong PIN")
        if attempts_left > 0:
            print(f"you have {attempts_left} more chances left")
        else:
            print("Card Blocked. No attempts left.")


