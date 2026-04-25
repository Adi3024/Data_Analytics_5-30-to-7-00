num = int(input("Enter an odd number: "))

if num % 2 == 0:
    raise Exception("Even number entered!")
else:
    print("Valid odd number")