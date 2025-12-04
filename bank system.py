from datetime import datetime

def load_accounts():
    try:
        with open("accounts.txt","r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    except:
        return []
    
def login_or_register():
    accounts = load_accounts()
    while True:
        print("\n1. Login")
        print("2. Register")
        choice = input("choose option:")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            for account in accounts:
                 if account[0] == username and account [1] == password:
                     print(f"Welcome {username}")
                     return username
            print("invalid username or password ! Try again.")
        elif choice == "2":
            username = input("Choose a username: ")
            if any(account[0] == username for account in accounts):
                print("Username already exists! Try a different one.")
                continue
            password = input("Choose a password:")
            with open("accounts.txt","a")as file:
                file.write(f"{username},{password}\n")
            print(f"Account created! Welcome{username}.")
            
            with open(f"balance _{username}.txt","w")as f:
                f.write("0")
                
            with open(f"transanctions_{username}.txt","w") as f:
                pass
            return username
        else:
            print("Invalid option! choose 1 or2.")

def load_balance(username):
    
    try:
        with open(f"balance_{username}.txt","r") as file:
            return float(file.read())
    except:
        return 0

def save_balance(username, balance):
    print("saving balance...")
    with open(f"balance_{username}.txt","w") as file:
        file.write(str(balance))
        
def load_transaction(username):
    
    try:
        with open(f"transactions_{username}.txt","r")as file:
            return [line.strip() for line in file.readlines()]
    except:
        return []
    
def save_transactions(username,transactions):
    with open(f"transactions_{username}.txt","w") as file:
        for t in transactions:
            file.write(t + "\n")

username = login_or_register()
balance = load_balance(username)
transactions = load_transaction(username)

def deposit(username, transactions, amount):
    global balance
    balance += amount
    print(f"{amount} deposited.New balance: {balance}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = f"{timestamp} - Deposited:{amount}"
    transactions.append(transaction)
    save_balance(username, balance)
    save_transactions(username,transactions)
    print(transaction)
    
    
def withdraw(username, transactions, amount):
    global balance
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if amount <= balance:
       balance -= amount
       print(f"{amount} withdrawn.New balance: {balance}")
       transaction = f"{timestamp} - Withdrawn:{amount}"
       transactions.append(transaction)
       save_balance(username , balance)
       save_transactions(username ,transactions)
    else:
        print("not enough balance!")
    
        
        
def check_balance():
    print(f"your curent balance is: {balance}")
    
    
def show_transactions():
    print("\n--- Transaction History ---")
    if transactions:
        for t in transactions:
            print(t)
    else:
        print("no transactions yet.")
    
    
while True:
    print("\n--- Bank menu ---")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.Show transaction History")
    print("5.Exit")
    
    choice = input("Choose an option:")
    
    if choice =="1":
        try:
           amount = float(input("Enter amount to deposit:"))
           if amount <= 0:
               print("Enter the positive number")
               continue
           deposit(username,transactions,amount)
        except:
            print("Invalid input ! Enter numbers only.")
    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw:"))
            if amount <= 0:
                print("Enter the positive number")
                continue
            withdraw(username,transactions,amount)
        except:
            print("Invalid input ! Enter numbers only.")
    elif choice == "3":
        check_balance()
    elif choice == "4":
        show_transactions()
    elif choice == "5":
        print("thank you for using the bank.Goodbyee!")
        break
    else:
        print("invalid option! Please try again.")
        
 
    
    
    
    
    
    
    