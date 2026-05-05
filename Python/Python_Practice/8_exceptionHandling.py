# Write a function that:
    #     takes user input
    #     safely converts to integer
    #     handles invalid input gracefully



def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Example usage
age = get_integer_input("Please enter your age: ")
print(f"You entered: {age}")    
