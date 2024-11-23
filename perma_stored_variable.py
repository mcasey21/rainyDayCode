import os

# Function to store a variable permanently in a file
def store_variable(variable):
    with open('stored_variable.txt', 'w') as file:
        file.write(variable)

# Function to read the stored variable from the file
def read_stored_variable():
    if os.path.exists('stored_variable.txt'):
        with open('stored_variable.txt', 'r') as file:
            return file.read()
    else:
        return None

# Main program
if __name__ == "__main__":
    stored_variable = read_stored_variable()

    if stored_variable is None:
        # If no variable is stored, prompt the user to enter one
        user_variable = input("Enter a variable to store permanently: ")
        store_variable(user_variable)
        print("Variable stored successfully.")
    else:
        # If a variable is already stored, prompt the user to enter it again
        user_variable = input("Enter the stored variable: ")

        if user_variable == stored_variable:
            print("Variable matches the stored one.")
        else:
            print("Error: Entered variable does not match the stored one.")
