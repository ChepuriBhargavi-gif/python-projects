class Account:
    def __init__(self,username,password,balance = 0):
        self.username = username
        self.password = password
        self.balance = balance
        self.mini_statment = []
    def credit(self):
        amount = float(input("Enter amount to credit"))
        if amount <= 0:
            print("Please Enter Positive amount")
        else:
            self.balance += amount
            self.mini_statment.append(f"Credited {amount}")
            print(f'{amount} is Credited Successfully')
    def debit(self):
        amount = float(input("Enter amount to debit"))
        if amount <= 0:
            print("Please Enter Positive amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.mini_statment.append(f"Debited {amount}")
            print(f"{amount} Debited")
    def check_balance(self):
        print(f"Balance {self.balance}")
    def mini_statement(self):
        if len(self.mini_statment) == 0:
            print("No Transactions")
        else:
            for i in self.mini_statment:
                print(i)

        print(f"Available Balance: {self.balance}")

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self,username,password):
        if username in self.accounts:
            print("Username already exits")
        else:
            self.accounts[username] = Account(username,password)
            print("\nAccount Created Successfully")
            print("---- Welcome to SBI Bank ----")

    def login(self,username,password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Success")
                return account
            else:
                print("Invalid Password")
        else:
            print("Invalid username")
        return None

bank = BankingSystem()

while True:
    print("\n --- Bank Management System")

    print("1.Create")
    print("2.Login")
    print("3.Exit")

    choice = input("Enter your choice (1-3):")

    if choice == "1":
        username = input("Enter username:")
        password = int(input("Enter Password:"))
        bank.create_account(username,password)

    elif choice == "2":
        username = input("Enter username:")
        password = int(input("Enter Password:"))
        account = bank.login(username,password)

        if account is not None:
            while True:
                print("--- SBI Bank ---")
                print("1.Credit")
                print("2.Debit")
                print("3.Check Balance")
                print("4.Mini Statement")
                print("5.Exit")

                choice = input("Enter you choice(1-5):")

                if choice == '1':
                    account.credit()
                elif choice == '2':
                    account.debit()
                elif choice == '3':
                    account.check_balance()
                elif choice == '4':
                    account.mini_statement()
                elif choice == '5':
                    print("Thank you for using the SBI Bank")
                    break
                else:
                    print("Invalid Choice")

    elif choice == "3":
        print("Thank you for using SBI Bank")
        break
    else:
        print("Invalid choice Please Enter Valid Choice")
