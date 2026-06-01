import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn=sqlite3.connect('banking.db')
print("Database created successfully")

cur=conn.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS customers
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 email TEXT NOT NULL UNIQUE,
#                 balance REAL NOT NULL)''')

# print ("Table created successfully")


# cur.execute('''
# INSERT INTO customers (name, email, balance) VALUES
# ('Brijesh', 'Brijesh@example.com', 10000.0), 
#              ('Krish', 'Krish@example.com', 7000.0), 
#              ('Het', 'Het@example.com', 5000.0)
#             ''')

# print ("Data inserted successfully")

# #Insert multiple records using a list of tuples
# insert_data = [
#      ('Divyang', 'Divyang@example.com', 8000.0),
#      ('Satyarth', 'Satyarth@example.com', 6000.0),
#      ('Chaman', 'Chaman@example.com', 4000.0)
# ]

# # #Add multiple records using executemany
# cur.executemany('''
#                  INSERT INTO customers (name, email, balance) VALUES (?, ?, ?)
#                 ''', insert_data)


# fetch data from database and display in tabular format
query = "SELECT * FROM customers"
df = pd.read_sql_query(query, conn)
print(df)


# dispaly in bar chart
# plt.figure(figsize=(10, 6))
# plt.bar(df['name'], df['balance'])
# plt.title('Customer Balances')
# plt.xlabel('Customer Name')
# plt.ylabel('Balance')
# plt.grid(True)


# display in pie chart
# plt.figure(figsize=(8,8))
# plt.pie(df['balance'], labels=df['name'], autopct='%1.1f%%')
# plt.title('Customer Balance Distribution') 

# dispaly in scatter plot chart
plt.figure(figsize=(10, 6))
plt.scatter(df['id'], df['name'], df['balance'])
plt.title('Customer Balances with ID')
plt.xlabel('Customer ID')
plt.ylabel('Balance')
plt.grid(True)

plt.show()

conn.commit()

conn.close()

