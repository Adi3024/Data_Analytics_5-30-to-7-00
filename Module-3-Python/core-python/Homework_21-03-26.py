# Write a program to check a number is prime number or not using function.

def number():
    num = int(input("Enter a Number: "))
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Entered Number is NOT a Prime Number.")
                break
        else:
            print("Entered Number is a Prime Number.")
    else:
        print("Please Try Again.")

number()


# Write a program to print simple hello word using functions.

def message():
    print("HELLO")

message()


# Write a program to Print a factorial number.

def factorial():
    num = int(input("Enter a Number: "))
    fact = 1
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:
        print("Factorial of", num, "is 1.")
    else:
        for i in range(2, num + 1):
            fact *= i
        print("Factorial of", num, "is", fact)

factorial()

# OR WE CAN ALSO WRITE AS:

def factorial():
    num = int(input("Enter a Number: "))
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    print("Factorial is:", fact)

factorial()

# Write a program to print a fibonacci series using numbers.

def fibonacci():
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    count = 0
    
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, ":")
        print(a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a, end=' ')
            a, b = b, a + b
            count += 1
fibonacci()

# Write a program to print a maximum number among 3 numbers.

def maximum():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    if (num1 >= num2) and (num1 >= num3):
        print("The maximum number is:", num1)
    elif (num2 >= num1) and (num2 >= num3):
        print("The maximum number is: ", num2)
    else:
        print("The maximum number is: ", num3)

maximum()

# Write a program to print a reverse of string.

def reverse_string():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print("Reversed string:", reversed_string)
reverse_string()

# Write a program to print a year is leap year or not using number. 

def leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Enetered year is a leap year.")
    else:
        print("Entered year is not a leap year.")
leap_year()

# Write a program to print compound interest using function.

def compound_interest():
    principal = int(input("Enter the principal amount: "))
    rate = int(input("Enter the annual interest rate (in %): "))
    time = int(input("Enter the time in years: "))
    
    # Calculate compound interest
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    
    print(f"Compound Interest: Rs. {interest:.2f}")
    print(f"Total Amount after {time} years: Rs. {amount:.2f}")

compound_interest()

