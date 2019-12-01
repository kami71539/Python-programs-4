try:
    #value=10/0
    number=int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print("The number is getting divided by zero.")
    print(error)
except ValueError as error2:
    print("The value entered is incorrect")
    print(error2)
