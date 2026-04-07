**Assignment_Module-2 SQL**


**Create Database**

```
CREATE DATABASE MArketCo;
```

Question -1 : Statement to create the Contact table.

**Answer:**
```
CREATE TABLE Contact (
    ContactID INT PRIMARY KEY AUTO_INCREAMENT,
    CompanyID INT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);
```

Question 2 : Statement to create the Employee table.

**Answer**
```
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY AUTO_INCREAMENT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Phone VARCHAR(12)
);
```


Question 3 : Statement to create the ContactEmployee table.

**Answer**
```
CREATE TABLE ContactEmployee (
    ContactEmployeeID INT PRIMARY KEY,
    ContactID INT,
    EmployeeID INT,
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
```


**Create Company Table.**

**Answer**
```
CREATE TABLE Company (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10)
);
```

**ADD RECORDS into Company Table**
```
INSERT INTO Company VALUES (1, 'Toll Brothers', '150 Ring Road', 'Rajkot', 'Gujarat', 360004),
                           (2, 'Urban Outfitters, Inc.', 'Raiya Chowk', 'Rajkot', 'Gujarat', 360005),
                           (3, 'Tommy Hilfiger', 'Narayan Nagar', 'Ahmedabad', 'Gujarat', 380015);
```

**OUTPUT**
```

## Company Table

+-----------+------------------------+----------------+-----------+---------+--------+
| CompanyID | CompanyName            | Street         | City      | State   | Zip    |
|-----------|------------------------|----------------|-----------|---------|--------|
| 1         | Toll Brothers          | 150 Ring Road  | Rajkot    | Gujarat | 360004 |
| 2         | Urban Outfitters       | Raiya Chowk    | Rajkot    | Gujarat | 360005 |
| 3         | Tommy Hilfiger         | Narayan Nagar  | Ahmedabad | Gujarat | 380015 |
+-----------+------------------------+----------------+-----------+---------+--------+

```


**ADD RECORDS into Contact Table**
```
INSERT INTO Contact VALUES (1, 1, 'Dianne', 'Connor'),
                           (2, 2, 'Vin', 'Diesel'),
                           (3, 3, 'Paul', 'Walker');
```

**ADD RECORDS into Employee Table**
```
INSERT INTO Employee VALUES (1, 'Jack', 'Lee', '9995563278'),
                            (2, 'Lesley', 'Bland', '8899562317'),
                            (3, 'Jordana', 'Brewster', '6359587415');
```

**ADD RECORDS into ContactEmployee Table**
```
INSERT INTO ContactEmployee VALUES (1, 1, 1),
                                   (2, 2, 2),
                                   (3, 3, 3);
```


Question - 4 : In the Employee table, the statement that changes Lesley Bland’s phone number to 215-555-8800.

**Answer**
```
UPDATE Employee SET Phone = '215-555-8800' WHERE FirstName = 'Lesley' AND LastName = 'Bland';
```
**OR**
```
UPDATE Employee SET Phone = '215-555-8800' WHERE EmployeeID = 2;
```


Question - 5 : In the Company table, the statement that changes the name of “Urban Outfitters, Inc.” to “Urban Outfitters”.

**Answer**
```
UPDATE Company SET CompanyName = 'Urban Outfitters' WHERE CompanyName = 'Urban Outfitters, Inc.';
```


Question - 6 :  In ContactEmployee table, the statement that removes Dianne Connor’s contact event with Jack Lee (one statement).
**HINT**: Use the primary key of the ContactEmployee table to specify the correct record to remove.

**Answer**
```
DELETE FROM ContactEmployee WHERE ContactEmployeeID = 1;
```


Question - 7 : Write the SQL SELECT query that displays the names of the employees that have contacted Toll Brothers (one statement). 
Run the SQL SELECT query in MySQL Workbench. Copy the results below as well. 

**Answer**
```
SELECT e.FirstName, e.LastName FROM Employee e JOIN ContactEmployee ce ON e.EmployeeID = ce.EmployeeID
JOIN Contact c ON ce.ContactID = c.ContactID JOIN Company co ON c.CompanyID = co.CompanyID
WHERE co.CompanyName = 'Toll Brothers';
```

**Output**
```
+------------+----------+
| FirstName  | LastName |
+------------+----------+
| Jack       | Lee      |
+------------+----------+
```


Question - 8 : What is the significance of “%” and “_” operators in the LIKE statement ?

**Answer**
```
1. % - The significance of % in LIKE statement it means ANY NUMBER(ZERO) or MORE CHARACTERS.
For Eg. - If we want to select names which is started with character b then we have to write it as,
          **SELECT * from table_name WHERE name LIKE 'b%';**
    Eg- If we want to select select name which is ends with character b then we have to write it as,
          **SELECT * from table_name WHERE name LIKE '%b';** 

2. _ - The significance of _ in LIKE statement it means EXACTLY ONE CHARACTER or ONLY ONE CHARACTER.
For Eg. - If we want to select names which is started with double AA then we have to write it as,
          **SELECT * from table_name WHERE name LIKE 'A_';**
```


Question - 9 : Explain normalization in the context of databases.

**Answer**
```
Normalization is the process of organizing data into multiple tables to reduce redundancy and improve data consistency.
There are 3 types of Normalization.

**First Normalization (1NF) :** 
1. A table is in 1NF if each field contains only one value and each record is unique.
2. All the columns contain single values.
3. No repeating groups or multiple values in a column.

**Second Normalization (2NF) :**
1. A table is in 2NF if it is in 1NF and all non-key attributes are fully dependent on the primary key.
2. It is already in 1NF.
3. All non-key attributes depend on the whole primary key.

**Third Normalization (3NF) :**
1. A table is in 3NF if it is in 2NF and has no transitive (indirect) dependency.
2. It is already in 2NF.
3. No dependency between non-key attributes.
```


Question - 10 : What does a join in MySQL mean ?

**Answer**
```
1. JOIN is used to combine data from multiple tables based on a related column. OR
2. JOIN is used to combine rows from two or more tables based on a related column.

Types of JOIN
1. INNER JOIN : Shows only matching data in both tables.
2. LEFT JOIN  : Shows all data from left table and matching from right.
3. RIGHT JOIN : Shows all data from right table and matching from left.
4. FULL JOIN  : Shows all data from both tables.
```


Question - 11 : What do you understand about DDL, DCL and DML in MySQL ?

**Answer**
```
DDL - Data Defination Language
1. Data Defination Language is used to define or change structure of database/tables.
2. DDL is used to create, modify, and delete database structures.

Command in DDL are: 1.CREATE 2.ALTER 3.DROP 4.TRUNCATE 5.RENAME 6.CHANGE


DCL - Data Control Language
1. Data Control Language is used to control access/permissions.
2. Used to control access/permissions.

Command in DCL are : 1.GRANT 2.REVOKE


DML - Data Manipulation Language
1. Data Manipulation Language is used to work with data inside tables.
2. Used to work with data inside tables.

Command in DML are : 1.INSERT 2.UPDATE 3.DELETE 4.SELECT
```


Question - 12 : What is the role of the MySQL JOIN clause in a query, and what are some
common types of joins ?

**Answer**
```
1. The role of JOIN clause in MYSQL is used to combine data from two or more tables based on a related column.
2. It helps you get data from multiple tables in one result.
3. JOIN clause is used to combine data from multiple tables based on a related column, and common types include INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

Types of JOIN
1. INNER JOIN : Shows only matching data in both tables.
2. LEFT JOIN  : Shows all data from left table and matching from right.
3. RIGHT JOIN : Shows all data from right table and matching from left.
4. FULL JOIN  : Shows all data from both tables.
```
