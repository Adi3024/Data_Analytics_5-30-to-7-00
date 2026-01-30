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

5. When we have to delete entire table - Truncate
**SYNTAX for DELETE ENTIER TABLE**
```
truncate table employee_Data_Records;
```

**RENAME**
**SYNTAX for RENAME ANY COLUMN**
```
Rename table employee_Records
```