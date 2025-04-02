def divide_numbers():
    try:
        # Take two inputs from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        
        print(f"The result of division is: {result}")
        
    except ValueError:
        # Handles invalid input (non-numeric values)
        print("Error: Please enter valid numeric values.")
        
    except ZeroDivisionError:
        # Handles division by zero
        print("Error: Cannot divide by zero.")
        
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function
divide_numbers()
