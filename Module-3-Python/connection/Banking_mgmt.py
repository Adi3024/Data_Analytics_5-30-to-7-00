import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Database Connection

conn = sqlite3.connect("banking.db")
cur = conn.cursor()

# Create Table

cur.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    balance REAL NOT NULL
)
""")
conn.commit()

# Function

def create_account():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    balance = float(input("Enter Initial Balance: "))

    cur.execute(
        "INSERT INTO customers(name,email,balance) VALUES(?,?,?)",
        (name, email, balance)
    )
    conn.commit()

    print("Account Created Successfully")


def view_accounts():
    df = pd.read_sql_query("SELECT * FROM customers", conn)
    print("\n")
    print(df)


def search_account():
    acc_id = int(input("Enter Customer ID: "))

    cur.execute(
        "SELECT * FROM customers WHERE id=?",
        (acc_id,)
    )

    record = cur.fetchone()

    if record:
        print(record)
    else:
        print("Account Not Found")


def deposit_money():
    acc_id = int(input("Enter Customer ID: "))
    amount = float(input("Enter Deposit Amount: "))

    cur.execute(
        "UPDATE customers SET balance = balance + ? WHERE id=?",
        (amount, acc_id)
    )

    conn.commit()
    print("Amount Deposited Successfully")


def withdraw_money():
    acc_id = int(input("Enter Customer ID: "))
    amount = float(input("Enter Withdraw Amount: "))

    cur.execute(
        "SELECT balance FROM customers WHERE id=?",
        (acc_id,)
    )

    result = cur.fetchone()

    if result:
        balance = result[0]

        if balance >= amount:
            cur.execute(
                "UPDATE customers SET balance = balance - ? WHERE id=?",
                (amount, acc_id)
            )
            conn.commit()
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")
    else:
        print("Account Not Found")


def transfer_money():
    sender = int(input("Sender ID: "))
    receiver = int(input("Receiver ID: "))
    amount = float(input("Amount: "))

    cur.execute(
        "SELECT balance FROM customers WHERE id=?",
        (sender,)
    )

    sender_balance = cur.fetchone()

    if sender_balance and sender_balance[0] >= amount:

        cur.execute(
            "UPDATE customers SET balance = balance - ? WHERE id=?",
            (amount, sender)
        )

        cur.execute(
            "UPDATE customers SET balance = balance + ? WHERE id=?",
            (amount, receiver)
        )

        conn.commit()

        print("Transfer Successful")

    else:
        print("Insufficient Balance")


def delete_account():
    acc_id = int(input("Enter Customer ID: "))

    cur.execute(
        "DELETE FROM customers WHERE id=?",
        (acc_id,)
    )

    conn.commit()

    print("Account Deleted Successfully")


def show_chart():

    df = pd.read_sql_query(
        "SELECT name,balance FROM customers",
        conn
    )

    plt.figure(figsize=(8,5))
    plt.bar(df["name"], df["balance"])

    plt.title("Customer Balances")
    plt.xlabel("Customer Name")
    plt.ylabel("Balance")

    plt.show()


# Loop

while True:

    print("\n")
    print("===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Delete Account")
    print("8. Show Chart")
    print("9. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        deposit_money()

    elif choice == "5":
        withdraw_money()

    elif choice == "6":
        transfer_money()

    elif choice == "7":
        delete_account()

    elif choice == "8":
        show_chart()

    elif choice == "9":
        print("Thank You For Using Banking System")
        break

    else:
        print("Invalid Choice")

conn.close()