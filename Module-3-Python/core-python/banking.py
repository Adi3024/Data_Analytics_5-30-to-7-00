# Banking ATM System

# Sample database of customers
customers = {
    "1001": {
        "name": "John Doe",
        "pin": "1234",
        "balance": 5000,
        "account_type": "Savings"
    },
    "1002": {
        "name": "Jane Smith",
        "pin": "5678",
        "balance": 8000,
        "account_type": "Checking"
    },
    "1003": {
        "name": "Alice Johnson",
        "pin": "9012",
        "balance": 12000,
        "account_type": "Savings"
    }
}

def display_menu():
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Exit")
    print("====================")

def check_balance(account_number):
    print(f"\n--- Account Details ---")
    print(f"Name: {customers[account_number]['name']}")
    print(f"Account Type: {customers[account_number]['account_type']}")
    print(f"Current Balance: Rs. {customers[account_number]['balance']}")
    print("------------------------")

def withdraw_amount(account_number):
    try:
        amount = float(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("Amount must be greater than 0!")
            return
        if amount > customers[account_number]['balance']:
            print("Insufficient balance!")
            return
        customers[account_number]['balance'] -= amount
        print(f"Withdrawal successful! New balance: Rs. {customers[account_number]['balance']}")
    except ValueError:
        print("Invalid amount entered!")

def deposit_amount(account_number):
    try:
        amount = float(input("Enter amount to deposit: Rs. "))
        if amount <= 0:
            print("Amount must be greater than 0!")
            return
        customers[account_number]['balance'] += amount
        print(f"Deposit successful! New balance: Rs. {customers[account_number]['balance']}")
    except ValueError:
        print("Invalid amount entered!")

def main():
    print("===== Welcome to ATM =====")
    account_number = input("Enter your account number: ")
    
    if account_number not in customers:
        print("Account not found!")
        return
    
    pin = input("Enter your PIN: ")
    if pin != customers[account_number]['pin']:
        print("Incorrect PIN!")
        return
    
    print(f"Welcome, {customers[account_number]['name']}!")
    
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            withdraw_amount(account_number)
        elif choice == "3":
            deposit_amount(account_number)
        elif choice == "4":
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()     