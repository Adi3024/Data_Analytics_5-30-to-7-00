# What is SQL ?
1. SQL is stands for structured query language
2. SQL is used to creat a database and table structured
3. SQL is used as case-insensitive language
example : INSERT | insert | Insert
4. SQL is pop based language
5. SQL creat a table structres i.e. also called structured data formate
6. SQL used some command or query to create a structures (data base and table)

## what is database ?
Data base is stored an information in forms of tables.
examples : mysql, sqllite, mongodb, oracle

## what is tables ?
table is stored data in form of column and rows
table contain column and rows


## what is column and rows in tables ?
column : column in table also called filedname
| id | name | email | password | age | salary |
|----|------|-------|----------|-----|--------|
| 1 | divyang | D@gmail.com | d123 | 27 | 59500 |

rows : rows in formate of data stored
| id | name | email | password | age | salary |
|----|------|-------|----------|-----|--------|


**USERS**
| id | name | email | password | age | salary |
|----|------|-------|----------|-----|--------|
| 1 | divyang | D@gmail.com | d123 | 27 | 59500 |
| 2 | aarya | aarya@example.com | pass456 | 24 | 62000 |
| 3 | rohan | rohan@test.com | ro123 | 30 | 75000 |
| 4 | sneha | sneha@mail.com | sn789 | 28 | 58000 |
| 5 | kabir | kabir@web.com | kb999 | 32 | 85000 |
| 6 | isha | isha@domain.com | ish432 | 26 | 61000 |
| 7 | manav | manav@service.com | mn111 | 29 | 67000 |
| 8 | tara | tara@cloud.com | tr888 | 25 | 54000 |
| 9 | viraj | viraj@pro.com | vr555 | 31 | 72000 |
| 10 | meera | meera@info.com | mr000 | 27 | 63000 |

## types of command in SQL ?
1. DDL (Data Defination Language)
2. DML (Data Manipulation Language)
3. DQL (Data Query Language)
4. TCL (Transcational control language)


1. **DDL**
Stand for data defination language
its create a data base and table structures

**command in DDL**
1. create
2. alter
3. rename
4. change
5. truncate
6. drop


**How to create a data base**
**syntax**
```
create database database name;
```
**examples**
```
create database data_analytics_app;
or 
create database data_analytics_flipkart;

```
**How to create a table**
**Chart of table create**

**USERS**
| column name | data type |
|-------------|-----------|
| id          | int (default size 11) primary key auto_increment |
| name, email, password | char, varchar (0-255) |
| address, message, comment | text |
| photo, file, pdf | varchar (0-255), blob |
| DOB, Date | date, varchar (0-255) |
| Datetime | datetime, varchar(0-255) |
| Phone Number | int, bigint (default size 20) |
| Price | int, Float, money |
| Status | (Pending, confirmed) |
| Attendance | (Absent, Present) |
| long Data | enum (enumerated) |

**Syntax of create table**
```
create table table name
(
    column name datatype(size) auto_increment primary key,
    .
    .
    .
    .
    column name datatype(size)
)
```

**EXAMPLE-1**

```
create table USERS
(
    User_ID int AUTO_INCREMENT PRIMARY KEY,
    Name Varchar(60),
    Email Varchar(60),
    Password Varchar(60),
    Age int,
    Salary Float,
    Department Varchar(60),
    Country Varchar(60)
);

```
**EXAMPLE-2**
```
Create table Employee_Data_Records
(
    Employee_ID_Number int Auto_increment Primary key,
    email_ID varchar(50),
    Joining_Date varchar(40),
    Position varchar(50),
    Age varchar(10),
    Phone_Number bigint(20),
    Salary Float,
    upload_Image blob,
    Address text
);
```

**ALTER**

1. When we have to add any new column in table - ADD
**SYNTAX for ADDING COLUMN IN TABLE**
```
Alter table employee_Data_Records add Column Name Data Type(Size);
```

2. When we have to add any new column after particular column - ADD -> AFTER
**SYNTAX for ADDING COLUMN AFTER ANY PARTICULAR COULMN IN TABLE**
```
Alter table employee_Data_Records add New Column Name Data type(size) after column name (after which column we have to add new column);
```

3. When we have to delete any column from table - DROP
**SYNTAX DELETE ANY COLUMN**
```
alter table employee_Data_Recods Drop column name;
```

**SYNTAX for DELETE ANY DATABASE**
```
Drop database data_analytics_flipkart; (after drop database we never get back the data) 
```

**SYNTAX for DELETE ANY TABLE**
```
Drop table employee_Data_Records; (after drop table we never get back the data)
```

4. When we have to change column name - CHANGE 
**SYNTAX for CHANGE ANY COLUMN NAME**
```
Alter table employee_Data_Records change column name New column name Data type(size);
```

5. When we have to delete entire table data - Truncate
**SYNTAX for DELETE ENTIER DATA OF TABLE**
```
truncate table employee_Data_Records;
```

**RENAME**
**SYNTAX for RENAME ANY COLUMN**
```
Rename table employee_Records
```

## What is DML ?
DMl stands for data manupulation language DML is used to insert data | delete data | update data

1.INSERT     2.DELETE     3.UPDATE

**INSERT**

**Sigle Data OR Rows Insert**
INSERT into tbl_country(countryname) VALUES('india')

**Multiple Data OR Rows Insert**
INSERT into tbl_country(countryname) VALUES('uk'),('usa'),('china'),('russia')
OR
 INSERT into tbl_country VALUES('null','srilanka'),('null','nigeria'),('null','uae'),('null','pakistan')

**Insert All Columns from one table into another**
INSERT INTO archive_users SELECT * FROM users;

**DELETE**

1. Used to delete all data from tables
delete from users;

2. delete will be used to delete particular data or rows from tables
delete from users where user_id=1;
OR
delete from users where name='vishal';

3. delete will be used to delete using "IN" operator
delete from users where user_id between 5 and 100;

**Note after delete we will rollback our data using TCL**

**UPDATE**

**Update the rows or data**
update users set name='umang',age=35 where user_id=3;


## DQL
DQL stands for data query language DQL is used to fetch(select) data from tables

**SELECT**
1. Select all data 
```
select * from users;
```

2. Select particular data from id
```
select * from users where user_id=2;
```

3. select particular data from column name
```
select user_id , name from users;
OR
select user_id , name from users where user_id=5;
```

4. Select data apply limit
select * from users where user_id limit 0,2;
OR
select * from users where user_id limit 2,2;
OR
select * from users where user_id limit 2,2;
OR
select * from users where user_id limit 1,5;
OR 
select * from users where user_id limit 2,5;
OR
select * from users where user_id limit 4,3;

5. Select data apply "IN"
select * from users where user_id in (2,4,5,7);

6. select data apply "BETWEEN"
 ```
 select * from users where user_id between 4 and 7;
 or
 select * from users where user_id between 555 and 999;
 ```

7. select data by ascending and descending order     

   **order by**
    order by is used to filter data from ascending and descending order   

   **ascending**
   ```
    select * from users order by name asc;
   ```

    ```
    select * from users order by user_id;
   ```
   **descending**
   ```
    select * from users order by name desc;
   ```

    ```
    select * from users order by user_id desc;
   ```

   **group by**
   
   A group by is always work on group of columns 

  ```
   select sum(salary),department from flip_users group by department;
  ```   


  **having**
  having is used to filter data after group by 

  ```
   select sum(salary),department from flip_users group by department having sum(salary)>50000;
  ```      

  **like**
  1. like is used to filter data using pattern matching
  2. like is used to search for specific column data using wildcards 

   **wildcards**
   1. % (percent) : represents zero or more characters
   2. _ (underscore) : represents a single character

   **examples**
  ```
   select * from users where name like 'b%';
   OR
   select * from users where name like '%a%';
   OR
   select * from users where name like '%a';
   OR
   select * from users where name like '_a%';
  ```


  ## WHAT IS SQL FUNCTIONE
  SQL function is used to perform some operations on data and return a single value

  Types of SQL function
   1. Aggregate function
   2. Scalar function
   
   **Aggregate function**
   COUNT() : count is used to count the number of rows in a table
   SUM() : sum is used to calculate the total of a numeric column
   AVG() : avg is used to calculate the average of a numeric column
   MIN() : min is used to find the minimum value in a numeric column
   MAX() : max is used to find the maximum value in a numeric column
   
   Examples of "Aggregate function"
select count(*) from users;
OR
select sum(salary) from users;
OR
select sum(salary) as total_sum_salary from flip_users;
OR
select avg(salary) as average_salary from flip_users;
OR
select min(salary) from flip_users;
OR
select max(salary) from flip_users;
OR
select department , sum(salary) as total_salary from flip_users group by department; 
OR
select department , avg(salary) as average_salary from flip_users group by department;
OR
select department , min(salary) as minimum_salary from flip_users group by department;
OR
select department , max(salary) as maximum_salary from flip_users group by department;
OR
select department , count(*) as total_employee from flip_users group by department;
OR
select department , count(*) as total_employee from flip_users group by department having count(*)>2;
OR
select department , sum(salary) as total_salary from flip_users group by department having sum(salary)>50000;
OR
select department , avg(salary) as average_salary from flip_users group by department having avg(salary)>60000;
OR
select department , min(salary) as minimum_salary from flip_users group by department having min(salary)>50000;

**Find second highest salary find second highest salary from table used subquery**
select max(salary) from flip_users where salary < (select max(salary) from flip_users);

**Scalar function**
UPPER() : upper is used to convert a string to uppercase
LOWER() : lower is used to convert a string to lowercase
LENGTH() : length is used to find the length of a string
NOW() : now is used to return the current date and time
DATE() : date is used to return the current date
TIME() : time is used to return the current time

**Note**: first we will create a table and insert some data then we will apply sql function on that data to understand better

**Note**: lastly we will learn about TCL (transactional control language) in next file

Examples of Scalar function
select upper(name) from users;
OR
select lower(name) from users;
OR
select length(name) from users;
OR
select now() from users;
OR
select date() from users;
OR
select time() from users;
OR
select name , upper(name) as uppercase_name from users;
OR
select name , lower(name) as lowercase_name from users;
OR
select name , length(name) as name_length from users;
OR
select name , now() as current_datetime from users;
OR
select name , date() as current_date from users;
OR
select name , time() as current_time from users;


## SQL key constraints
1. **Primary key**
a. primary key is used to uniquely identify each record in a table
b. primary key is used to create a relationship between two tables
c. primary key is used to ensure that all values in a column are different
d. primary key always define on single column.
e. primary key cannot have null value

Examples of Primary key
```
  create table users
  (
  user_id int AUTO_INCREMENT primary key,
  name varchar(55),
  password varchar(255),
  age int,
  salary float,
  department varchar(200),
  country varchar(155)   
  );
  ```

  Examples in format

  | User id | Name  |Password| Age| Salary| Department | Country|
  |---------|-------|--------|----|-------|------------|--------|
  |    1    | divya | d@123  | 27 | 59500 | PURCHASE   | INDIA  |
  |    2    | aarya | pass@1 | 24 | 62000 | IT         | INDIA  |
  |    3    | rohan | ro123  | 30 | 75000 | CSE        | INDIA  |
  |    4    | sneha | sn789  | 28 | 58000 | MARKETING  | INDIA  |
  |    5    | kabir | kb999  | 32 | 85000 | IT         | INDIA  |
  |    6    | manav | mn111  | 29 | 67000 | CSE        | INDIA  |
  |    7    | tarun | tr888  | 25 | 54000 | PURCHASE   | INDIA  |
  |    8    | viraj | vr555  | 31 | 72000 | MARKETING  | INDIA  |
  |    9    | meera | mr000  | 27 | 63000 | IT         | INDIA  | 

  2. **Foreign key :**
       a. foreign key is used to establish a relationship between two tables
       b. foreign key is used to ensure referential integrity between two tables
       c. foreign key is used to ensure that the value in a column must match the value in another table's primary key column
       d. foreign key can have null value
  
    Examples of Foreign key

   **Create table country**
   | User id | Country_Name  |
   |---------|---------------|
   |    1    |     India     |
   |    2    |      UK       |
   |    3    |     USA       |

   **Create table users**
| User id |   Name  |Password| Age| Salary| Department | Country_ID |
|---------|---------|--------|----|-------|------------|------------|
|    1    | brijesh | d@123  | 27 | 59500 | PURCHASE   |      1     |
|    2    | aarya   | pass@1 | 24 | 62000 | IT         |      1     |
|    3    | rohan   | ro123  | 30 | 75000 | CSE        |      1     |
|    4    | sneha   | sn789  | 28 | 58000 | MARKETING  |      1     |
|    5    | kabir   | kb999  | 32 | 85000 | IT         |      1     |        


## How to create foreign key
create table users
(
 user_id int AUTO_INCREMENT primary key,
 name varchar(55),
 password varchar(255),
 age int,
 salary float,
 department varchar(200),
 country_id int,
 foreign key (country_id) references country(country_id) 
);

**Unique key**
 a. unique key is used to ensure that all values in a column are different
 b. unique key is used to create a relationship between two tables
 c. unique key is used to ensure that a column cannot have duplicate values
 d. unique key can have null value one time only
 e. unique key can be defined on single column or multiple columns

Examples of unique key
create table users
(
user_id int AUTO_INCREMENT primary key,
name varchar(55),
password varchar(255) unique,
age int,
salary float,
department varchar(200),
country_id int,
foreign key (country_id) references country(country_id) 
);

alter table users add unique (email);

              
  4. **not null** : not null is used to ensure that a column cannot have a null value
  5. **default** : default is used to provide a default value for a column when no value is specified


## TCL (transactional control language)
1. TCL stands for transactional control language
2. TCL is used to manage transactions in a database
3. TCL is used to ensure the integrity of a database
4. TCL is used to rollback a transaction in case of an error
5. TCL is used to commit a transaction to make it permanent in the database


   1. **commit** : commit is used to save the changes made by a transaction to the database

     **syntax**
     ```
       commit;
  
     ```

   2. **rollback** : rollback is used to undo the changes made by a transaction in case of an error
    **syntax**
 ```
   rollback;

```

**examples of commit and rollback**
start transaction; delete from users where user_id=2; commit;

delete from users where user_id=1; rollback;


**Note** :MYSQL is not support rollback in structures**


## Home work

**students based database**

1. create a database named "school"
```
Create database SCHOOL;
```

2. create a table named "students" with the following columns: id (primary key), name, age, grade, and country_id (foreign key referencing the  
country table).
```
Create table STUDENTS;
(
    Student_ID int Primary key Auto_Increament,
    Name varchar(255),
    Age int,
    Grade varchar(255),
    Country_ID int,
    foreign key(Country_ID) references country(country_id)
)
```

3. insert at least 5 records into the students table.
   | Student_ID | Student_Name | Student_Age | Student_Grade | Student_Country_ID |
   |------------|--------------|-------------|---------------|--------------------|
   |    1       |   Brijesh    |     25      |       A       |          1         |
   |    2       |    Krish     |     22      |       AB      |          2         |
   |    3       |     Het      |     21      |       B       |          3         |
   |    4       |   Divyang    |     28      |       BB      |          4         |
   |    5       |   Mirang     |     29      |       C       |          5         |

4. create a table named "country" with the following columns: country_id (primary key) and country_name.
```
 Create table COUNTRY
 (
    Country_ID int Primary Key Auto_Increament,
    Country_Name Varchar(255)
 )
 ```

5. Insert at least 3 records into the country table.
   | Country_ID | Country_Name |
   |------------|--------------|
   |    1       |    INDIA     |
   |    2       |     USA      |
   |    3       |     UK       |
   |    4       |     UAE      |
   |    5       |    RUSSIA    |

6. write a query to select all students along with their country names.
```

```

7. write a query to find the average age of students in each grade.
```
SELECT avg(age) AS average_student_age from student;
```

8. write a query to find the total number of students in each country.
```

```
9. write a query to find the student with the highest grade.
```
select max(grade) from student;
```
10. write a query to update the grade of a student with a specific id.
```
update student set grade='AA' where student_id=4;
```
11. write a query to delete a student with a specific id.
```
delet from student where student_id='5';
```


**add to cart based database**
1. create a database named "ecommerce"
2. create a table named "products" with the following columns: product_id (primary key), product_name, price, and stock.
3. insert at least 5 records into the products table.
4. create a table named "customers" with the following columns: customer_id (primary key), customer_name, email, and country_id (foreign key referencing the country table).
5. insert at least 3 records into the customers table.   
6. create a table named "orders" with the following columns: order_id (primary key), customer_id (foreign key referencing the customers table), product_id (foreign key referencing the products table), quantity, and order_date.
7. insert at least 5 records into the orders table.   
8. write a query to select all orders along with customer names and product names.
9. write a query to find the total revenue generated from all orders.
10. write a query to find the most popular product based on the quantity ordered.
11. write a query to update the stock of a product after an order is placed.
12. write a query to delete an order with a specific order_id.


**faculty based database**
1. create a database named "university"
2. create a table named "faculty" with the following columns: faculty_id (primary key), faculty_name, department, and country_id (foreign key referencing the country table) and provides email as unique key in faculty tables.
3. insert at least 5 records into the faculty table.
4. create a table named "courses" with the following columns: course_id (primary key), course_name, and faculty_id (foreign key referencing the faculty table).
5. insert at least 3 records into the courses table.  
6. create a table named "students" with the following columns: student_id (primary key), student_name, age, and country_id (foreign key referencing the country table).
7. insert at least 5 records into the students table.
8. create a table named "enrollments" with the following columns: enrollment_id (primary key), student_id (foreign key referencing the students table), course_id (foreign key referencing the courses table), and enrollment_date.
9. insert at least 5 records into the enrollments table.
10. write a query to select all enrollments along with student names and course names.
11. write a query to find the total number of students enrolled in each course.
12. write a query to find the faculty member teaching the most courses.
13. write a query to update the department of a faculty member with a specific faculty_id.
14. write a query to delete a student with a specific student_id.

**Note: after creating database and tables you will insert some data in that tables then you will apply all the queries on that data to understand better**
