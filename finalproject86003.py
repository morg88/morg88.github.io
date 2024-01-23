"""Creating a Banking System """
import random
from sys import exit


class BankAccount:
    """Create class that stores methods for recursion purposes"""
    def __init__(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, dep_amount):
        self.balance = (dep_amount) + (self.balance)
        return self.balance

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance = float(self.balance) - float(withdraw_amount)
            return self.balance

        else:
            print("insufficient funds")

    def checking_balance(self):
        print(f"Your checking account balance is ${self.balance}\n")

    def account_details(self):
        print(f"Your account number is {self.account_number} and your current balance is ${self.balance}")


class Bank():
    """ Create Class that handles specific user accounts"""

    print('Hello Welcome to The Future of Banking')

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        # this method allows user to deposit and create new accounts to be stored within dictionary
        print('Lets start by entering your deposit amount!!\n')
        while True:
            try:
                initial_balance = float(input("Enter your first deposit amount:$ \n"))
                if initial_balance > 0:
                    while True:
                        account_number = random.randint(10000000, 99999999)
                        if account_number not in self.accounts:
                            break
                    new_acc = BankAccount(account_number,initial_balance)
                    self.accounts[account_number] = new_acc


                    print(f"Your new account number is: {account_number} and your account has been accredited: ${initial_balance}\n")
                    break
            except ValueError:
                print("you must add funds to your account to receive account number ")

    def get_account(self, account_num):
        # this method allows the user pull account from dictionary with account number
        return self.accounts[account_num]

    def get_account_num(self):
        # Check that the account number is entered correctly without breaking the code
        while True:
            try:
                check_acc = int(input('Enter your account number to retrieve account : \n'))
                if check_acc in self.accounts:
                    return check_acc
                print("account number not found please try again")
            except ValueError:
                print('You did not enter a valid account number please try again')

    def get_float(self, prompt):
        # check that the users input is greater then 0
        while True:
            try:
                user_input = float(input(prompt))
                if user_input >= 0:
                    return user_input
                else:
                    print("you enter an invalid number try again")
            except ValueError:
                print("you enter an invalid number try again")


    def deposit(self):
        # Use methods to find and execute deposits amount into correct accounts
        user_acc = self.get_account_num()
        acc_gt = self.get_account(user_acc)
        dep_amount = self.get_float(f"How much would you like to deposit into account #{user_acc}: \n")
        acc_gt.deposit(dep_amount)
        acc_gt.checking_balance()

    def withdraw(self):
        # User methods to find and execute withdraw amount from correct accounts
        user_acc = self.get_account_num()
        acc_gt = self.get_account(user_acc)
        withdraw_amount = self.get_float(f"How much would you like to withdraw from account #{user_acc}: \n")
        acc_gt.withdraw(withdraw_amount)
        acc_gt.checking_balance()

    def transfer(self):
        # Use two account numbers, remove from balance of sender and add to balance of receiver
        print('Sender Account ')
        user_acc_from = self.get_account_num()
        acc_gt = self.get_account(user_acc_from)
        print('Receiver Account')
        user_acc_too = self.get_account_num()
        acc_too = self.get_account(user_acc_too)
        while True:

            try:
                rem_amount = float(input(f'How much would you like to transfer to account {user_acc_too}?: \n'))
                if acc_gt.balance >= rem_amount:
                    acc_gt.balance -= rem_amount
                    acc_too.balance += rem_amount
                    print(f"Your account {user_acc_from} has transferred {rem_amount} to {user_acc_too}!!\n Your new balance for account {user_acc_from}"
                          f" is now ${acc_gt.balance}\n Your new balance for account {user_acc_too} is now ${acc_too.balance}\n")
                    break
                print("You do not have sufficient amount of funds to transfer\n")
            except ValueError:
                print('You do not have sufficient amount of funds to transfer\n')

    def bank_balance(self):
        # use class BankAccount to request balance
        acc_num = self.get_account_num()
        user_acc = self.get_account(acc_num)
        BankAccount.checking_balance(user_acc)

def menu():
    # this menu will be used in the execute function to iterate over the choices
    print("1. Create Account 2. Deposit 3. Withdraw 4. Check Balance 5. Transfer 6. Quit")


def execute_choice():
    # this will hold give the user options to choose its path
    menu()
    choice = input("How can I assist you today? choose: 1,2,3,4,5,6 : \n")

    if choice == "1":
        account1.create_account()
    elif choice == "2":
        account1.deposit()
    elif choice == "3":
        account1.withdraw()
    elif choice == "4":
        account1.bank_balance()
    elif choice == "5":
        account1.transfer()
    else:
        print("Thank you for banking with Future Banking")
        exit()


def continue_operation():
    while True:
        execute_choice()
        con_op = input("would you like to continue? Type 'y' for yes 'n' for no \n").upper()
        if con_op == "Y":
            continue
        else:
            print("Thanks for using Future Banking")
            exit()


account1 = Bank()
continue_operation()

