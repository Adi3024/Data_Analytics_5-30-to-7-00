**Assignment_Module-3 PYTHON**

Question-1. What are the types of Applications?

**Answer**
```
Python is used to develop different types of applications.
There are many types of application which are listed below :
1. Web Application 
2. Desktop Application
3. Mobile Application
4. Enterprise Application 
5. Scientific Application
```

Question-2. What is Programming?

**Answer**
```
Programming in Python is the process of writing instructions using the Python language to tell a computer what to do. It is used to create applications, automate tasks, and solve problems.
```

Question-3 What is Python?

**Answer**
```
1. Python is a high-level, interpreted programming language known for its simple 
   and readable syntax.

2. It supports multiple programming paradigms including procedural, 
   object-oriented, and functional programming.

3. Python is widely used in web development, data analysis, artificial 
   intelligence, scientific computing, and automation due to its extensive standard library and rich ecosystem of third-party packages.
```

Question-4 Write a Python program to check if a number is positive, negative or
           zero.

**Answer**
```
PYTHON

num= int(input("Enter a number: "))

if num > 0:
    print("Entered Number is Positive")
elif num < 0:
    print("Entered Number is Negative")
else:
    print("Entered Number is Zero")
```

**OUTPUT**
```
Enter a NUmber : 50

"Entered Number is Positive"

Enter a Number : -2

"Entered Number is Negative"

Enter a Number : 0

"Entered Number is Zero"
```
Question-5 Write a Python program to get the Factorial number of given numbers. 

**Answer**

```
PYTHON
num = int(input("Enter number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial:", fact)
```

**OUTPUT**
```
Enter a number : 5
Factorial : 120
```

Question-6 Write a Python program to get the Fibonacci series of given range. 

**Answer**

```
PYTHON 
n = int(input("Enter a Number for terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

**OUTPUT**
```
Enter a Number of terms : 10
0 1 1 2 3 5 8 13 21 34
```

Question-7 How memory is managed in Python? 

**Answer**
```
1. Python manages memory automatically using a private memory space called the 
   Python Heap. 
2. All objects and data structures are stored in this heap.
3. Python uses a built-in Garbage Collector to remove unused objects and free   
   memory automatically. It also uses reference counting, where memory is released when an object is no longer referenced.
4. This automatic memory management makes programming easier and reduces 
   memory-related errors.
```

Question-8 What is the purpose continuing statement in python?

**Answer**

```
1. The continue statement is used inside loops to skip the current iteration and 
   move to the next iteration of the loop.
2. When Python finds continue, it does not execute the remaining code for that 
   iteration and directly starts the next loop cycle.
3. It is useful when we want to ignore specific conditions without stopping the 
   entire loop.
```

Question-9 Write python program that swap two number with temp variable
           and without temp variable. 

**Answer**

```
a = 10
b = 20

print ("Before swapping:")
print ("a=', a)
print ("b=", b)

a , b = b , a

print ("After swapping")
print ("a=", a)
print ("b=", b)
```

**OUTPUT**

```
Before swapping:
a = 10
b = 20

After swapping:
a = 20
b = 10
```

Question-10  Write a Python program to find whether a given number is even
             or odd, print out an appropriate message to the user.

**Answer**
```
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Entered Number is Even")
else:
    print("Entered a Number is Odd")
```

**OUTPUT**
```
Enter a number : 2
Entered Number is Even

Enter a number : 5
Entered Number is Odd
```

Question-11 Write a Python program to test whether a passed letter is a vowel
            or not. 

**Answer**
```
ch = input("Enter a letter: ").lower()

if ch in 'aeiou':
    print("Entered Letter is Vowel")
else:
    print("Entered Letter is not Vowel")
```

**OUTPUT**
```
Enter a Letter : a
Entered Letter is Vowel

Enter a Letter : b
Entered Letter is not Vowel
```

Question-12 Write a Python program to sum of three given integers. However, if
            two values are equal sum will be zero. 

**Answer**

```
a = int(input("Enter first Number:"))
b = int(input("Enter second Number:"))
c = int(input("Enter third Number:"))

if a == b or b == c or a == c:
        result = (0)
else :
        result = (a + b + c)

print ("sum of entered number is =", result)
```

**OUTPUT**
```
Enter first Number : 10
Enter second Number : 20
Enter third Number : 30

sum of entered number is = 60

Enter first Number : 10
Enter second Number : 10
Enter third Number : 30

sum of entered number is = 0
```

Question-13 Write a Python program that will return true if the two given
            integer values are equal or their sum or difference is 5. 

**Answer**

```
a = int(input("Enter first Number:"))
b = int(input("Enter second Number:"))

if a == b or a + b == 5 or abs(a - b) == 5:
    print(True)
else:
    print(False)
```

**OUTPUT**
```
Enter first Number:3
Enter second Number:2
True

Enter first Number:6
Enter second Number:2
False

```

Question-14 Write a python program to sum of the first n positive integers. 

**Answer**

```
n = int(input("Enter n: "))
print(n * (n + 1) // 2)
```

**OUTPUT**

```
Enter n: 5
15

Enter n: 10
55
```

Question-15 Write a Python program to calculate the length of a string.

**Answer**

```
s = input("Enter string: ")
print("Length of enterd string is :", len(s))
```

**OUTPUT**

```
Enter string: divyang
Length of enterd string is : 7

Enter string: brijesh
Length of enterd string is : 7

Enter string: krish
Length of enterd string is : 5

Enter string: het
Length of enterd string is : 3
```

Question-16 Write a Python program to count the number of characters
            (character frequency) in a string.

**Answer**

```
a = input("Enter a string: ")
freq = {}

for ch in a:
    if ch in freq:
       freq[ch] += 1
    
    else:
        freq[ch] = 1

print("Character frequency is :")
for ch in freq:
    print(ch, ":", freq[ch])
```

**OUTPUT**

```
Enter a string: divyang          
Character frequency is :
d : 1
i : 1
v : 1
y : 1
a : 1
n : 1
g : 1

Enter a string: Banana   
Character frequency is :
B : 1
a : 3
n : 2

```

Question-17 What are negative indexes and why are they used? 

**Answer**

```
1. Negative indexes are used to access elements from the end of a list, string, or  
   tuple in Python.

2. The index -1 represents the last element, -2 represents the second last element, 
   and so on.

3. They are used when we want to access data from the end without knowing the exact 
   length of the sequence.
```

Question-18 Write a Python program to count occurrences of a substring in a string.

**Answer**

```
s = ""hello world, hello everyone""
sub = "hello"

print(s.count(sub))
```

**OUTPUT**

```
The count of substring of string is : 2
```

QUestion-19 Write a Python program to count the occurrences of each word in a given  
            sentence.

**Answer**

```
s = input("Enter sentence: ")
words = s.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("The words of entered sentece is:", freq)
```

**OUTPUT**

```
Enter sentence: Hello Every one. My Name is Divyang Shah.
 The freq of entered sentece is: {'Hello': 1, 'Every': 1, 'one.': 1, 'My': 1, 'Name': 1, 'is': 1, 'Divyang': 1, 'Shah.': 1}
```

Question-20 Write a Python program to get a single string from two given strings,
            separated by a space and swap the first two characters of each string. 

**Answer**

```

a = "abc"
b = "xyz"

new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]

print ("New a =", new_a, "\n" "New b =" , new_b)

```

**OUTPUT**

```
New a = xyc 
New b = abz
```

Question-21 Write a Python program to add 'in' at the end of a given string (length
            should be at least 3). If the given string already ends with 'ing' then
            add 'ly' instead if the string length of the given string is less than 3,
            leave it unchanged.

**Answer**

```
s = input("Enter a string: ")

if len(s) < 3:
    resturn s
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "in")
```

**OUTPUT**

```

```

**OUTPUT**

```
Enter a string: running
runningly

Enter a string: run
runin

Enter a string: go
go
```

Question-22 Write a Python function to reverses a string if its length is a multiple
            of 4.

**Answer**

```
s = input("Enter string: ")

if len(s) % 4 == 0:
    print(s[::-1])
else:
    print(s)
```

**OUTPUT**

```
Enter string: Bina
aniB

Enter string: Divyang
Divyang
```

Question-23 Write a Python program to get a string made of the first 2 and the last
            2 chars from a given a string. If the string length is less than 2, return
            instead of the empty string.

**Answer**

```
PYTHON

s = input("Enter string: ")

if len(s) < 2:
    print("")
else:
    print(s[:2] + s[-2:])

```

**OUTPUT**

```
Enter string: Mohit
Moit

Enter string: Divyang
Ding

Enter string: I


```

Question-24 Write a Python function to insert a string in the middle of a string.


**Answer**
```
PYTHON
s = "My Name Divyang"
mid = len(s)//2

result = s[:mid] + " is " + s[mid:]
print("The final answer is :", result)
```

**OUTPUT**
```
The final answer is : My Name is Divyang
```

Question-25 What is List? How will you reverse a list? 

**ANSWER** 
```
1. A List in Python is a collection of items stored in a single variable. 
2. It can contain different types of data like numbers, strings, and objects. 
3. Lists are ordered, changeable (mutable), and allow duplicate values.
4. To reverse a list, we can use the reverse() method, which changes the original list 
   into reverse order.

**FOR EXAMPLE**
list = [10, 20, 30, 40]
list.reverse()
print("Final answer is : ", list)

**OUTPUT**
Final abswer is : [40, 30, 20, 10]
```

Question-26 How will you remove last object from a list? 

**Answer**
```
PYTHON
list = [1,2,3]
list.pop()
print("The answer is :", list)
```

**OUTPUT**

```
The answer is : [1, 2]
```

Question-27 Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

**Answer**

```
PYTHON
list = [2, 33, 222, 14, 25]
print(list[-1])
```

**OUTPUT**

```
25
```

Question-28 Differentiate between append () and extend () methods? 

**Answer**

```
1. Both append() and extend() are used to add elements to a list, but they work differently.

# append() : adds the entire element as a single item at the end of the list.
# extend() : adds each element of another list one by one to the end of the list.

-> So, append() adds one item, while extend() adds multiple items.

**FOR EXAMPLE**

list1 = [1, 2]

list1.append([3, 4])
print("The final answer is :", list1)

**OUTPUT**

```
The final answer is : [1, 2, [3, 4]]
```



```
list2 = [1, 2]

list2.extend([3, 4])
print("The final answer is :", list2)
```

**OUTPUT**
```
The final answer is : [1, 2, 3, 4]
```
```


Question-29 Write a Python function to get the largest number, smallest num
            and sum of all from a list.

**Answer**
```
PYTHON
lst = [10, 20, 5, 40]

print("Max:", max(lst))
print("Min:", min(lst))
print("Sum:", sum(lst))
```

**OUTPUT**
```
Max : 40
Min : 5
sum : 75
```

Question-30 How will you compare two lists?

**Answer**
```
1. Two lists can be compared using the == operator in Python.
2. The == operator checks whether both lists have the same elements in the same order. 
3. If both lists are exactly the same, it returns True; otherwise, it returns False.

list1 = [10, 20, 30]
list2 = [10, 20, 30]

print(list1 == list2)
```

**OUTPUT**

```
True
```

Question-31 Write a Python program to count the number of strings where the string
            length is 2 or more and the first and last character are same from a given list
            of strings.

**Answer**
```
PYTHON
list1 = ['abc', 'xyz', 'aba', '1221']

count = 0

for i in list1:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print("The count is :", count)
``` 

**OUTPUT**
```
The count is: 2
```

Question-32 Write a Python program to remove duplicates from a list. 

**Answer**

```
PYTHON

list1 = [10, 20, 30, 20, 40, 10, 50]

list2 = list(set(list1))

print("Final list after  duplicate removes :", list2)
```

**OUTPUT**

```
Final list after duplicate removes : [40, 10, 50, 20, 30]
```

Question-33 Write a Python program to check a list is empty or not.

**Answer**
```
PYTHON

list1 = []

if len(list1) == 0:
    print("List is empty")
else:
    print("List is not empty")
```

**OUTPUT**

```
List is empty 
```

Question-34 Write a Python function that takes two lists and returns true if they
            have at least one common member. 

**Answer**

```
PYTHON

list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]

result = False

for i in list1:
    if i in list2:
        result = True
        break

print("The final result is :", result)
```

**OUTPUT**

```
The final result is : True
```

Question-35 Write a Python program to generate and print a list of first and last 5
            elements where the values are square of numbers between 1 and 30. 

**ANswer**

```
PYTHON

list1 = []

for i in range(1, 31):
    list1.append(i ** 2)

print("First 5:", list1[:5])
print("Last 5:", list1[-5:])
```


**OUTPUT**

```
First 5: [1, 4, 9, 16, 25]
Last 5: [676, 729, 784, 841, 900]
```

Question-36 Write a Python function that takes a list and returns a new list with
            unique elements of the first list. 

**Answer**
```
PYTHON

list1 = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(list1))

print(unique_list)
```

**OUTPUT**

```
The Unqiue List is : [1, 2, 3, 4, 5]
```


Question-37 Write a Python program to convert a list of characters into a string. 


**Answer**

```
PYTHON

list1 = ['P', 'Y', 'T', 'H', 'O', 'N']

result = ''.join(list1)

print("The result is :", result)
```

**OUTPUT**

```
The result is : PYTHON
```


Question-38 Write a Python program to select an item randomly from a list. 

**Answer**

```
PYTHON

import random

list1 = [10, 20, 30, 40, 50]

print("ANSWER :", random.choice(list1))
```

**OUTPUT**

```
ANSWER : 30

ANSWER : 50

```


Question-39 Write a Python program to find the second smallest number in a list. 

**Answer**

```
PYTHON

list1 = [10, 25, 5, 8, 15]

list1.sort()

print("Second smallest number is:", list1[1])
```

**OUTPUT**

```
Second smallest number is: 8
```

Question-40 Write a Python program to get unique values from a list.

**Answer**

```
PYTHON

list1 = [10, 20, 30, 20, 40, 10, 50]

unique_values = list(set(list1))

print("UNIQUE VALUES :", unique_values)
```

**OUTPUT**

```
UNIQUE VALUES : [40, 10, 50, 20, 30]
```

Question-41 Write a Python program to check whether a list contains a sub list.

**Answer**

```
PYTHON
list1 = [1, 2, 3, 4, 5]
sub_list = [3, 4]

if all(item in list1 for item in sub_list):
    print("List contains sublist")
else:
    print("List does not contain sublist")
```

**OUTPUT**

```
List contains sublist
```

Question-42 Write a Python program to split a list into different variables. 

**Answer**

```
list1 = [10, 20, 30]

a, b, c = list1

print("Number a is : =", a)
print("Number b is : =", b)
print("Number c is : =", c)
```

**OUTPUT**

```
Number a is : = 10
Number b is : = 20
Number c is : = 30
```

Question-43 What is tuple? Difference between list and tuple.

**Answer**

```
TUPLE : A tuple is a collection of elements stored in a single variable. It is ordered and    
        allows duplicate values, but it is immutable, which means its values cannot be changed after creation.

**Difference between List and Tuple**

       List	                                                      Tuple
Mutable (can be changed)	                         Immutable (cannot be changed)
Uses square brackets [ ]	                         Uses parentheses ( )
Slower than tuple	                                 Faster than list
Example: [1,2,3]	                                 Example: (1,2,3)
```


Question-44 Write a Python program to create a tuple with different data types. 

**Answer**

```
PYTHON
tuple1 = (10, "Python", 3.14, True)

print(tuple1)
```

**OUTPUT**

```
(10, 'Python', 3.14, True)
```

Question-45 Write a Python program to unzip a list of tuples into individual lists.

**Answer**

```
PYTHON

list1 = [(1, 'A'), (2, 'B'), (3, 'C')]

num, char = zip(*list1)

print("Numbers:", num)
print("Characters:", char)
```

**OUTPUT**

```
Numbers: (1, 2, 3)
Characters: ('A', 'B', 'C')
```


Question-46 Write a Python program to convert a list of tuples into a dictionary. 

**Answer**

```
PYTHON

list1 = [(1, "One"), (2, "Two"), (3, "Three")]

dict1 = dict(list1)

print(dict1)
```

**OUTPUT**

```
{1: 'One', 2: 'Two', 3: 'Three'}
```


Question-47 How will you create a dictionary using tuples in python? 


**Answer**

```
PYTHON

tuple1 = (("name", "Divyang"), ("age", 28), ("city", "Rajkot"))

dict1 = dict(tuple1)

print(dict1)
```

**OUTPUT**

```
{'name': 'Divyang', 'age': 28, 'city': 'Rajkot'}
```


Question-48 Write a Python script to sort (ascending and descending) a dictionary by value. 

**Answer**

```
PYTHON
dict1 = {'a': 50, 'b': 20, 'c': 40, 'd': 10}

asc = sorted(dict1.items(), key=lambda x: x[1])
desc = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

print("Ascending:", asc)
print("Descending:", desc)
```

*OUTPUT**

```
Ascending: [('d', 10), ('b', 20), ('c', 40), ('a', 50)]
Descending: [('a', 50), ('c', 40), ('b', 20), ('d', 10)]
```


Question-49 Write a Python script to concatenate following dictionaries to create a new one. 

**Answer**

```
PYTHON

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

result = {}
result.update(dict1)
result.update(dict2)
result.update(dict3)

print("result is :", result)
```

**OUTPUT**

```
result is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```


Question-50 Write a Python script to check if a given key already exists in a dictionary. 


**Answer**

```
PYTHON

dict1 = {'name': 'Divyang', 'age': 28, 'city': 'Rajkot'}

key = 'age'

if key in dict1:
    print("Key is exists")
else:
    print("Key does not exist")
```

**OUTPUT**

```
Key is exists
```


Question-51 How Do You Traverse Through a Dictionary Object in Python? 

**Answer**

```
PYTHON

dict1 = {'name': 'Divyang', 'age': 28, 'city': 'Rajkot'}

for key, value in dict1.items():
    print(key, ":", value)
```

**OUTPUT**

```
name : Divyang
age : 28
city : Rajkot
```


Question-52 How Do You Check the Presence of a Key in A Dictionary? 

**Answer**

```
PYTHON

dict1 = {'name': 'Divyang', 'age': 28}

if 'name' in dict1:
    print("Key is present")
else:
    print("Key is not present")
```

**OUTPUT**

```
Key is present
```


Question-53 Write a Python script to print a dictionary where the keys are numbers between 1  
         and 15. 

**Answer**

```
PYTHON

dict1 = {}

for i in range(1, 16):
    dict1[i] = i * i

print(dict1)
```

**OUTPUT**

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
```

Question-54 Write a Python program to check multiple keys exists in a dictionary 

**Answer**

```
PYTHON

dict1 = {'name': 'Divyang', 'age': 28, 'city': 'Rajkot'}

keys = ['name', 'age']

if all(key in dict1 for key in keys):
    print("All keys exist")
else:
    print("Some keys are missing")
```

**OUTPUT**

```
All keys exist
```

Question-55 Write a Python script to merge two Python dictionaries 

**ANswer**

```
PYTHON 

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

dict1.update(dict2)

print(dict1)
```

**OUTPUT**

```
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
```


Question-56 Write a Python program to map two lists into a dictionary
            Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

**Answer**

```
PYTHON

keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

dict1 = dict(zip(keys, values))

print(dict1)
```

**OUTPUT**

```
{'a': 400, 'b': 400, 'c': 300, 'd': 400}
```

Question-57 Write a Python program to find the highest 3 values in a dictionary.

**Answer**

```
PYTHON

dict1 = {'a': 50, 'b': 80, 'c': 20, 'd': 100, 'e': 70}

values = sorted(dict1.values(), reverse=True)

print("Highest 3 values:", values[:3])
```

**OUTPUT**

```
Highest 3 values: [100, 80, 70]
```


Question-58 Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output: Counter ({'item1': 1150, 'item2': 300})

**Answer**

```
PYTHON

from collections import Counter

list1 = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

result = Counter()

for d in list1:
    result[d['item']] += d['amount']

print(result)

```

**OUTPUT**

```
Counter({'item1': 1150, 'item2': 300})
```


Question-59 Write a Python program to create a dictionary from a string.
            Note: Track the count of the letters from the string. 

**Answer**

```
PYTHON

string = "Divyang"

dict1 = {}

for i in string:
    dict1[i] = dict1.get(i, 0) + 1

print(dict1)
```

**OUTPUT**

```
{'D': 1, 'i': 1, 'v': 1, 'y': 1, 'a': 1, 'n': 1, 'g': 1}
```


Question-60 Sample string:'w3resource' 
            Expected output:{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

**Answer**

```
PYTHON

string = "w3resource"

dict1 = {}

for i in string:
    dict1[i] = dict1.get(i, 0) + 1

print(dict1)
```

**OUTPUT**

```
{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
```


Question-61 Write a Python function to calculate the factorial of a number (a non negative integer)

**Answer**

```
PYTHON

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)
```

**OUTPUT**

```
Factorial: 120
```


Question-62 Write a Python function to check whether a number is in a given range.

**Answer**

```
PYTHON

num = 15

if num in range(10, 21):
    print("Number is in range")
else:
    print("Number is not in range")
```

**OUTPUT**

```
Number is in range
```


Question-63 Write a Python function to check whether a number is perfect or not. 

**Answer**

```
PYTHON

num = 28
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
```

**OUTPUT**

```
Perfect Number
```


Question-64 Write a Python function that checks whether a passed string is palindrome or not.

**Answer**

```
PYTHON

string = "madam"

if string == string[::-1]:
    print("Entered String is :", "Palindrome")
else:
    print(Entered String is not :", "Not Palindrome")
```

**OUTPUT**

```
Entered String is : Palindrome
```


Question-65 How Many Basic Types of Functions Are Available in Python? 

**Answer**

```

There are mainly 2 basic types of functions in Python:

1. Built-in Functions

These are functions already provided by Python.
Examples: print(), len(), type(), input()

2. User-defined Functions

These are functions created by the user using the 'def' keyword according to their needs.
```

Question-66 How can you pick a random item from a list or tuple? 

**ANswer**

```
PYTHON

import random

list1 = [10, 20, 30, 40]

print(random.choice(list1))
```

**OUTPUT**

```
30 

40

10
```


Question-67 How can you pick a random item from a range?

**Answer**

```
PYTHON

import random

print(random.choice(range(1, 11)))
```

**OUTPUT**

```
5

7

1
```


Question-68 How can you get a random number in python?

**Answer**

```
PYTHON

import random

print(random.randint(1, 100))
```

**OUTPUT**

```
73

55

10
```


Question-69 How will you set the starting value in generating random numbers? 

**Answer**

```
PYTHON

import random

random.seed(10)

print(random.randint(1, 100))
```

**OUTPUT**

```
74

74

74
```

Question-70 How will you randomize the items of a list in place? 

**Answer**

```
PYTHON

import random

list1 = [10, 20, 30, 40, 50]

random.shuffle(list1)

print(list1)
```

**OUTPUT**

```
[10, 40, 20, 30, 50]
```

Question-71 What is File function in python? What are keywords to create
            and write file. 

**Answer**

```
A file function in Python is used to create, read, write, and manage files.

Keywords used:
"w" → Write only (creates file if not exists)
"w+"→ write/read if file dees not exist create a new file
"a" → Append only (append on file file and create new file if not exist)
"a+"→ append and read create a new if not exist
"r" → Read only
"r+"→ read/write only
```

Question-72 Write a Python program to read an entire text file. 

**Answer**

```
PYTHON

file = open("demo.txt", "r")
print(file.read())
file.close()
```

**OUTPUT**

```
Hello Python
Welcome to File Handling
```


Question-73 Write a Python program to append text to a file and display the text. 

**Answer**

```
PYTHON

file = open("demo.txt", "a")
file.write("\nWelcome to Python")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()
```

**OUTPUT**

```
Welcome to Python
```


Question-74 Write a Python program to read first n lines of a file.

**Answer**

```
PYTHON

n = 2

file = open("demo.txt", "r")

for i in range(n):
    print(file.readline())

file.close()
```

**OUTPUT**

```
Welcome to Python
```
Question-75 Write a Python program to read last n lines of a file.

**Answer**

```
PYTHON

n = 3

file = open("demo.txt", "r")
lines = file.readlines()

for line in lines[-n:]:
    print(line)

file.close()
Welcome to Python
```

**OUTPUT**

```
Welcome to Python programming. This is a demo file.
```

Question-76 Write a Python program to read a file line by line and store it into a list

**Answer**

```
PYTHON

file = open("demo.txt", "r")

list1 = file.readlines()

print(list1)

file.close()
```

**OUTPUT**

```
['\n', 'Welcome to Python\n', 'Welcome to Python programming. This is a demo file.']
```

Question-77 Write a Python program to read a file line by line store it into a variable.

**Answer**

```
PYTHON

file = open("demo.txt", "r")

data = file.read()

print(data)

file.close()
```

**OUTPUT**

```
Welcome to Python
Welcome to Python programming. This is a demo file.
```

Question-78 Write a python program to find the longest words.

**Answer**

```
PYTHON

string = "Python is easy and powerful language"

words = string.split()

longest = max(words, key=len)

print("Longest word is:", longest)

```

**OUTPUT**

```
Longest word is : powerful
```

Question-79 Write a Python program to count the number of lines in a text file.

**Answer**

```
PYTHON

file = open("demo.txt", "r")

count = len(file.readlines())

print("Number of lines is:", count)

file.close()
```

**OUTPUT**

```
Number of lines is : 3
```

Question-80 Write a Python program to count the frequency of words in a file.

**Answer**

```
PYTHON

file = open("demo.txt", "r")

data = file.read().split()

dict1 = {}

for word in data:
    dict1[word] = dict1.get(word, 0) + 1

print(dict1)

file.close()
```

**OUTPUT**

```
{'Welcome': 2, 'to': 2, 'Python': 2, 'programming.': 1, 'This': 1, 'is': 1, 'a': 1, 'demo': 1, 'file.': 1}
```

Question-81 Write a Python program to write a list to a file.

**Answer**

```
PYTHON

list1 = ["Python", "Java", "C++"]

file = open("demo.txt", "w")

for item in list1:
    file.write(item + "\n")

file.close()
```

**OUTPUT**

```
in the demo file i get the below list.
Python
Java
C++
```

Question-82 Write a Python program to copy the contents of a file to another file.

**Answer**

```
PYTHON

file1 = open("demo.txt", "r")
data = file1.read()

file2 = open("copy.txt", "w")
file2.write(data)

file1.close()
file2.close()
```


Question-83 Explain Exception handling? What is an Error in Python?

**Answer**

```
**Exception Handling in Python**

Exception handling is used to handle runtime errors in a program so that the program does not stop suddenly. It helps the program continue smoothly by using try, except, else, and finally blocks.


**Error in Python**

An error is a problem in the program that causes it to stop or give wrong output. Errors can happen due to wrong syntax, wrong logic, or invalid operations during execution.

Examples:

1. SyntaxError
2. ZeroDivisionError
3. NameError
4. TypeError

```


Question-84 How many except statements can a try-except block have? Name Some built-in exception classes:

**Answer**

```
1. A try block can have multiple except statements.
2. Each except block is used to handle a different type of error.
3. Python allows multiple except blocks to handle different exceptions separately.

# Some Built-in Exception Classes in Python #
1. ValueError → when wrong value is given
2. TypeError → when wrong data type is used
3. ZeroDivisionError → when dividing by zero
5.NameError → when variable is not defined
6. IndexError → when list index is out of range
7. FileNotFoundError → when file does not exist

```


Question-85 When will the else part of try-except-else be executed?

**Answer**

```
1. The else block is executed only when no exception occurs in the try block.
2. If the code inside try runs successfully without any error, then the else block will run. If an 
   exception occurs, the else block is skipped.

**FOR EXAMPLE**

try:
    num = 10 / 2
except ZeroDivisionError:
    print("Error occurred")
else:
    print("Division successful")

**OUTPUT**

Division successful

=> This means the else block runs only when the try block executes without errors.
```


Question-86 Can one block of except statements handle multiple exception?

**Answer**

```
1. Yes, one except block can handle multiple exceptions in Python.
2. We can write multiple exception names inside parentheses () separated by commas. 
3. If any one of those exceptions occurs, that single except block will handle it.
```


Question-87 When is the finally block executed?

**Answer**

```
1. The finally block always executes whether an exception occurs or not.
2. It is mainly used for cleanup work like closing files.
```

Question-88 What happens when „1‟== 1 is executed?

**Answer**

```
1. It returns False because '1' is a string and 1 is an integer.
2. Python compares both value and data type, so different data types are not equal.
3. Even though both look similar, one is text ('1') and the other is a number (1), so Python treats 
   them as different values.
```

Question-89 How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding 
            snippets.

**Answer**

```
Exception handling is used to prevent the program from stopping suddenly when an error occurs.

try → contains the code that may cause an error
except → handles the error if it occurs
finally → always executes whether an error occurs or not

**EXAMPLE**
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")
```

**OUTPUT**

```
Cannot divide by zero
Execution completed
```

Question-90 Write python program that user to enter only odd numbers, else will raise an exception. 

**Answer**

```
PYTHON

num = int(input("Enter an odd number: "))

if num % 2 == 0:
    raise Exception("Even number entered!")
else:
    print("Valid odd number")
```

**OUTPUT**

```
Enter an odd number: 3 
Valid odd number
```