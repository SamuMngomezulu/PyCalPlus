def main_menu ():
    print("Calculator Menu: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulo")
    print("7. Calculate BMI")
    print("8. Convert Celsius to Fahrenheit")
    print("9. Calculate Simple Interest")
    print("10. Exit")

def addition ():
    try:

        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        print(f"The sum is {a + b}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return


def subtraction ():
    try:

        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        print(f"The difference is {a - b}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def multiplication ():
    try:

        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        print(f"The product is {a * b}")
    
    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def division ():
    try: 

        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        if b != 0:
            print(f"The quotient is: {a / b}")
        else:
            print("Error: Division by zero")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def exponentiation ():
    try:

        a = float(input("Enter the base: "))
        b = float(input("Enter the exponent: "))
        print(f"The result is {a ** b}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def modulo ():
    try: 
        a = float(input("Enter the base: "))
        b = float(input("Enter the exponent: "))
        print(f"The modulo is {a % b}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def bmi ():
    try:
            
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
        height = height / 100  
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def celsius_to_fahrenheit ():
    try: 

        celsius = float(input("Enter temperature in degrees Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"The temperature in degrees Fahrenheit is {fahrenheit}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return

def simple_interest ():
    try: 

        principal = float(input("Please enter principal amount: "))
        rate = float(input("Please enter rate of interest: "))
        time = float(input("Please enter time in number of years: "))
        simple_interest = (principal * rate * time) / 100
        print(f"The simple interest amount R{simple_interest}")

    except ValueError:
        print("Error: Please Enter valid numeric values.")
        return


while True:
    main_menu()
    choice = input("Choose an option (1-10): ")
    
    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    elif choice == '5':
        exponentiation()
    elif choice == '6':
        modulo()
    elif choice == '7':
        bmi()
    elif choice == '8':
        celsius_to_fahrenheit()
    elif choice == '9':
        simple_interest()
    elif choice == '10':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")