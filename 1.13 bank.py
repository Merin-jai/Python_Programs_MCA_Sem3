class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Hello, Welcome to the Banking Application!")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"\nAmount deposited: {amount}")
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nYou have withdrawn: {amount}")
        else:
            print("\nInsufficient balance.")

    def display(self):
        print(f"\nCurrent balance: {self.balance}")


# Example usage
if __name__ == "__main__":
    account = BankAccount()
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account.deposit()
        elif choice == '2':
            account.withdraw()
        elif choice == '3':
            account.display()
        elif choice == '4':
            print("Thank you for using the banking application!")
            break
        else:
            print("Invalid choice. Please select again.")
