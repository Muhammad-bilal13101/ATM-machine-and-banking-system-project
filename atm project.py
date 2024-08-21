class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"


class ATM:
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")

            if choice == "1":
                print(f"Your current balance is: ${self.bank_account.get_balance()}")
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                self.bank_account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                self.bank_account.withdraw(amount)
            elif choice == "4":
                print("Exiting the ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage
account = BankAccount
atm = ATM(account)
atm.run()
