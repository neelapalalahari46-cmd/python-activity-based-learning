# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))
limit = float(input("Enter daily withdrawal limit: "))

n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0
rejected = 0
withdrawn_today = 0

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdrawal")

    choice = int(input("Select transaction type: "))
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        print("Invalid transaction amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        deposits += amount
        print("Deposit Successful")

    elif choice == 2:
        if amount > balance:
            print("Insufficient Balance")
            rejected += 1

        elif withdrawn_today + amount > limit:
            print("Daily Withdrawal Limit Exceeded")
            rejected += 1

        else:
            balance -= amount
            withdrawals += amount
            withdrawn_today += amount
            print("Withdrawal Successful")

    else:
        print("Invalid Transaction Type")
        rejected += 1

    print("Current Balance:", round(balance, 2))

print("\n--- ATM Transaction Summary ---")
print("Total Deposits:", round(deposits, 2))
print("Total Withdrawals:", round(withdrawals, 2))
print("Rejected Transactions:", rejected)
print("Final Account Balance:", round(balance, 2))
print("Daily Withdrawal Limit:", limit)
print("Remaining Withdrawal Limit:",
      round(limit - withdrawn_today, 2))
