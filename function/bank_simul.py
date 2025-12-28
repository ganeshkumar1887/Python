class BankBalance:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("--Insufficient funds--")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount}. Current balance: ${self.balance}")


def main():
    print("---Bank Simulator---")
    account = BankBalance(1000)
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            print(f"Current balance: ${account.balance}")
        
        elif choice == "4":
            print("Thanks for using the simulator!")
            print("Have a great day!")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()