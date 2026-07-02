# w.r.t. a program for canteen management application.
# create a database connection mysql 
# create a pandas for data set or data frames 
# create a matplotlib for data visualisation in chart
# install all ....
# pip install pandas matplotlib mysql-connector-python 
# create an app and import all dependancies.

import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",       
    database="canteen_management_appdb"
)

cursor = conn.cursor()
print("connection successfully established")

# ADD TASK create a function
def add_item():
    name = input("Enter item Name* :")
    price = input("Enter item Price* :")
    category = input("Enter item Category* :")
    
    sql = """
     INSERT INTO items(name, price, category) VALUES (%s, %s, %s)
    """
    data = (name, price, category)
    
    print(data)
    cursor.execute(sql, data)
    conn.commit()
    print("Item successfully added in tables")

# display item
def display_item(): 
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    print("\n==========display all items================")
    for i in result:
        print(i)

# update item
def update_item():  
    item_id = int(input("Enter item id for update :"))
    name = input("Enter item Name* :")
    price = input("Enter item Price* :")
    category = input("Enter item Category* :")
    
    sql = """
     UPDATE items SET name=%s, price=%s, category=%s WHERE id=%s
    """
    data = (name, price, category, item_id)
    cursor.execute(sql, data)
    conn.commit()

# delete item
def delete_item():
    item_id = int(input("Enter item id for delete :"))
    
    sql = """
     DELETE FROM items WHERE id=%s
    """
    data = (item_id,)
    cursor.execute(sql, data)
    conn.commit()
    print("Item successfully deleted from tables")

# create a function to visualize item data
def visualize_item_data():
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    
    # Create a DataFrame from the fetched data
    df = pd.DataFrame(result, columns=['ID', 'Name', 'Price', 'Category'])
    
    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.bar(df['Name'], df['Price'], color='skyblue')
    plt.xlabel('Item Name')
    plt.ylabel('Price')
    plt.title('Canteen Items Price Visualization')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# create a function for pie chart display item data in chart
def show_item_pie_chart():
    cursor.execute("SELECT category, COUNT(*) FROM items GROUP BY category")
    result = cursor.fetchall()
    
    categories = [row[0] for row in result]
    counts = [row[1] for row in result]
    
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Items by Category')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# create a function for data frames
def load_item_df():
    query = "SELECT * FROM items"
    df = pd.read_sql(query, conn)
    print("\n=====dataframes=======")
    print(df)
    return df

while True:
    print("\nCanteen Management System")
    print("1. Add Item")
    print("2. Display Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Visualize Item Data")
    print("6. Show Item Pie Chart")
    print("7. Load Item DataFrame")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        display_item()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        visualize_item_data()
    elif choice == '6':
        show_item_pie_chart()
    elif choice == '7':
        load_item_df()
    elif choice == '8':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")