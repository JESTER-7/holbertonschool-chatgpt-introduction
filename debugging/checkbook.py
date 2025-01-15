#!/usr/bin/python3
class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance inquiries.

    Attributes:
        balance (float): The current balance of the checkbook.
    """

    def __init__(self):
        """
        Initialize a Checkbook instance with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add a specified amount to the balance.

        Parameters:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deduct a specified amount from the balance if sufficient funds are available.

        Parameters:
            amount (float): The amount to be withdrawn.

        Returns:
            None
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook class.
    Provides options to deposit, withdraw, check balance, or exit.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
