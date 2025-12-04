# Mini Banking System in Python

A simple **console-based banking application** built with Python. This project demonstrates basic file handling, user input, functions, and transaction tracking.

---

## Features

* **User registration** and login
* **Deposit** and withdraw money
* **Check balance**
* **View transaction history** with timestamps

---

## How It Works

1. Users can register with a unique username and password.
2. After logging in, users can deposit or withdraw money.
3. Each transaction is recorded with a timestamp in a file.
4. User balances and transaction history are saved to separate files for persistence.

---

## Files

* `bank.py` → Main Python script
* `accounts.txt` → Stores usernames and passwords
* `balance_<username>.txt` → Stores account balance for each user
* `transactions_<username>.txt` → Stores transaction history

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/IRADUKUNDA-JULES/MINI_BANK.git
```

2. Navigate to the project folder and run:

```bash
python bank.py
```

3. Follow the prompts to register, login, and manage your account.

---

## Optional Improvements

* Hash passwords for better security
* Add categories for transactions (e.g., bills, groceries)
* Implement object-oriented programming with a `BankAccount` class
* Add a graphical interface with Tkinter or PyQt

---

## License

This project is open-source and free to use.
