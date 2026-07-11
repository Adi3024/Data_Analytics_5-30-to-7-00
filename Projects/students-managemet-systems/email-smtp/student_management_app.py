# w.r.t. a program for stdent management application.
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
    password="",       
    database="student_management_appdb"
)

cursor = conn.cursor()
print("connection successfully established")

# ADD TASK create a function
def add_student():
    name = input("Enter student Name* :")
    age = input("Enter student Age* :")
    grade = input("Enter student Grade* :")
    
    sql = """
     INSERT INTO students(name, age, grade) VALUES (%s, %s, %s)
    """
    data = (name, age, grade)
    
    print(data)
    cursor.execute(sql, data)
    conn.commit()
    print("Student successfully added in tables")   

# display student
def display_student():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("\n==========display all students================")
    for i in result:
        print(i)

# update student
def update_student():
    student_id = int(input("Enter student id for update :"))
    name = input("Enter student Name* :")
    age = input("Enter student Age* :")
    grade = input("Enter student Grade* :")
    
    sql = """
     UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s
    """
    data = (name, age, grade, student_id)
    cursor.execute(sql, data)
    conn.commit()

# delete student
def delete_student():
    student_id = int(input("Enter student id for delete :"))
    
    sql = """
     DELETE FROM students WHERE id=%s
    """
    data = (student_id,)
    cursor.execute(sql, data)
    conn.commit()

# create a function to visualize student data
def visualize_student_data():
    cursor.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade")
    result = cursor.fetchall()
    
    grades = [row[0] for row in result]
    counts = [row[1] for row in result]
    
    plt.bar(grades, counts)
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.title('Number of Students by Grade')
    plt.show()

# create a function for pie chart display student data in chart
def show_student_pie_chart():
    df = load_student_df()
    grade_count = df['grade'].value_counts()
    
    plt.figure(figsize=(6, 6))
    plt.pie(
        grade_count,
        labels=grade_count.index,
        autopct='%1.1f%%'
    )
    
    plt.title('Student distribution by Grade')
    plt.show()

# create a function to load student data into a DataFrame
def load_student_df():
    query = "SELECT * FROM students"
    df = pd.read_sql(query, conn)
    print("\n=====dataframes=======")
    print(df)
    return df

while True:
    print("""
    1. Add Student
    2. Display Students
    3. Update Student
    4. Delete Student
    5. Visualize Student Data
    6. Show Student Pie Chart
    7. Exit
    """)
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        visualize_student_data()
    elif choice == '6':
        show_student_pie_chart()
    elif choice == '7':
        break
    else:
        print("Invalid choice, please try again.")