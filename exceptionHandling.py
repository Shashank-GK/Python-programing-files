def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        result = num1 / num2

        print(f"The result of {num1} divided by {num2} is: {result}")

    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid integer.")

    except ZeroDivisionError as zde:
        print(f"Error: {zde}. Cannot divide by zero, Please enter a non-zero number.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("Execution completed.")


if __name__ == "__main__":
    divide_numbers()
