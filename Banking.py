# Python Banking Program

def balance(amount):
    print("----------------")
    print(f"Balance: {amount:.2f}")
    print("----------------")

def deposit():
    print("--------------------------")
    addAmount = float(input("Deposit Amount: "))
    print("--------------------------")
    print(f"Amount Deposited: ${addAmount:.2f}")
    print("--------------------------")
    return addAmount

def withdraw():
    print("--------------------------")
    removeAmount = float(input("Withdraw Amount: "))
    print("--------------------------")
    if removeAmount > balanceAmount:
        print("--------------------------")
        print("Low Balance 😕")
        print("--------------------------")
    else:
        print(f"Amount Withdrawn: ${removeAmount:.2f}")
        print("--------------------------")
    return removeAmount

if __name__ == "__main__":
    print("***************\nBanking Program\n***************")
    isOnline = True
    balanceAmount = 0
    while isOnline:
        print("1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        print("************************")
        choice = int(input("Enter Your Choice[1-4]: "))
        print("************************")
        if choice == 1:
            balance(balanceAmount)
        elif choice == 2:
            balanceAmount += deposit()
        elif choice == 3:
            balanceAmount -= withdraw()
        elif choice == 4:
            isOnline = False
        else:
            print("Wrong Choice 🟥")
