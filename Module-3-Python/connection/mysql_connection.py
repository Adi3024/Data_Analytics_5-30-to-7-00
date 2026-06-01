import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# data base conncetion
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor=db.cursor();
print("Database connected successfully")

