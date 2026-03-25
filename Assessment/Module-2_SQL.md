MODULE -2 : DA-SQL - Introduction and Getting started with SQL.

**Assessment - 1 :**
```
CREATE TABLE Worker
(
    WORKER_ID INT PRIMARY KEY AUTO_INCREAMENT,
    FIRST_NAME Varchar(50),
    LAST_NAME Varchar(50),
    SALARY FLOAT,
    JOINING_DATE Datetime(),
    DEPARTMENT Varchar(25)
);
```

| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY |  JOINING_DATE  | DEPARTMENT |
|-----------|------------|-----------|--------|----------------|------------|
|     1     |  Monika    |  Arora    | 100000 | 2/20/2014 9:00 |     HR     |
|     2     |  Niharika  |  Verma    | 80000  | 6/11/2014 9:00 |    Admin   |
|     3     |  Vishal    |  Singhal  | 300000 | 2/20/2014 9:00 |     HR     |
|     4     |  Amitabh   |  Singh    | 500000 | 2/20/2014 9:00 |    Admin   |
|     5     |  Vivek     |  Bhati    | 500000 | 6/11/2014 9:00 |    Admin   |
|     6     |  Vipul     |  Diwan    | 200000 | 6/11/2014 9:00 |   Account  |
|     7     |  Satish    |  Kumar    | 75000  | 1/20/2014 9:00 |   Account  |
|     8     |  Geetika   |  Chuahan  | 90000  | 4/11/2014 9:00 |    Admin   |


**Question - 1 :**

Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.

**Answer**

SELECT * FROM Worker ORDER BY First_name, Department DESC;


**Question - 2 :**

Write an SQL query to print details for Workers with the first names “Vipul” and “Satish” from the Worker table.

**Answer**

SELECT * FROM Worker WHERE First_Name = 'Vipul' OR First_Name = 'Satish';


**Question - 3 :**

Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.

**Answer**

SELECT * FROM worker WHERE First_Name LIKE '%h' AND LENGTH(First_Name)='6';


**Question - 4 :**

Write an SQL query to print details of the Workers whose SALARY lies between 1.

**Answer**

SELECT * FROM Worker WHERE Salary BETWEEN 1 AND 100000;


**Question - 5 :**

Write an SQL query to fetch duplicate records having matching data in some fields of a table.

**Answer**

SELECT SALARY, JOINING_DATE, DEPARTMENT, COUNT(*) AS count FROM Worker GROUP BY SALARY, JOINING_DATE, DEPARTMENT
HAVING COUNT(*) > 1;


**Question - 6 :**

Write an SQL query to show the top 6 records of a table. 

**Answer**

SELECT * FROM Worker Limit 6;


**Question - 7 :**

Write an SQL query to fetch the departments that have less than five people in them. 

**Answer**

SELECT Department, Count(Department) AS Number_of_Employee from Worker group by Department having count(department)<5;


**Question - 8 :**

Write an SQL query to show all departments along with the number of people in there.

**Answer**

SELECT Department, Count(*) AS Total_Employee from Worker group by Department;


**Question - 9 :**

Write an SQL query to print the name of employees having the highest salary in each
department.

**Answer**

SELECT DEPARTMENT,FIRST_NAME,LAST_NAME, MAX(SALARY) as Highest_Salary FROM worker GROUP BY DEPARTMENT;






**Assessment - 2 :**
Open school database, then select student table and use following SQL statements.
TYPE THE STATEMENT, PRESS ENTER AND NOTE THE OUTPUT.
```
Create DATABASE School;
```

```
CREATE TABLE Student
(
    StuID INT PRIMARY KEY AUTO_INCREAMENT,
    StuName Varchar(50),
    Sex Varchar(50),
    Percentage FLOAT,
    Class INT,
    Sec Varchar(10),
    Stream Varchar(20),
    DOB DATE
);
```

| StdID |     StdName     |  Sex   | Percentage | Class | Sec |  Stream  |    DOB     |
|-------|-----------------|--------|------------|-------|-----|----------|------------|
|  1001 | Surekha Joshi   | Female |      82    |   12  |  A  |  Science | 3/8/1998   |
|  1002 | MAAHI AGARWAL   | Female |      56    |   11  |  C  | Commerce | 11/23/2008 |
|  1003 | Sanam Verma     |  Male  |      59    |   11  |  C  | Commerce | 6/29/2006  |
|  1004 | Ronit Kumar     |  Male  |      63    |   11  |  C  | Commerce | 11/5/1997  |
|  1005 | Dipesh Pulkit   |  Male  |      78    |   11  |  B  |  Science | 14/09/2003 |
|  1006 | JAHANVI Puri    | Female |      60    |   11  |  B  | Commerce | 11/7/2008  |
|  1007 | Sanam Kumar     |  Male  |      23    |   12  |  F  | Commerce | 3/8/1998   |
|  1008 | SAHIL SARAS     |  Male  |      56    |   11  |  C  | Commerce | 11/7/2008  | 
|  1009 | AKSHARA AGARWAL | Female |      72    |   12  |  B  | Commerce | 10/1/1996  |
|  1010 | STUTI MISHRA    | Female |      39    |   11  |  F  |  Science | 11/23/2008 |
|  1011 | HARSH AGARWAL   |  Male  |      42    |   11  |  C  |  Science | 3/8/1998   |
|  1012 | NIKUNJ AGARWAL  |  Male  |      49    |   12  |  C  | Commerce | 28/06/1998 |
|  1013 | AKRITI SAXENA   | Female |      89    |   12  |  A  |  Science | 11/23/2008 |
|  1014 | TANI RASTOGI    | Female |      82    |   12  |  A  |  Science | 11/23/2008 |


**Question - 1 :**
To display all the records form STUDENT table.

**Answer**
Select *  from Student ;


**Question - 2 :**
To display any name and date of birth from the table STUDENT. 

**Answer**
Select StdName, DOB from student ;


**Question - 3 :**
To display all students record where percentage is greater of equal to 80 FROM student table. 

**Answer**
Select *  From Student where percentage >=80;


**Question - 4 :**
To display student name, stream and percentage where percentage of student is more than 80. 

**Answer**
Select StdName, Stream, Percenatge where percentage > 80;


**Question - 5 :**
To display all records of science students whose percentage is more than 75 form student table.  

**Answer**
Select * From Student where Stream = "Science" AND Percenateg > 75;