# Login and register authorization file for user

# Import function from other Python files
from data_manage import save_user_register

# Hardcoded credentials for admin login
admin_username = "admin"
admin_password = "123"

# Function to verify and authorize login
def login():
    try:
        # Ask user for username and password input
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Verify login credentials for admin
        if username == admin_username and password == admin_password:
            return "admin" # Return to result for admin menu

        # Open users.txt in read mode
        with open("users.txt", "r") as file:
            # Read all lines in the txt file
            credential_list = file.readlines()

            for line in credential_list:
                # Strip empty lines created by readlines() and split credentials by comma
                credentials = line.strip().split(",")

                # If user input equals to credentials
                if username == credentials[0] and password == credentials[1]:
                    print("Login successful!")
                    return "user" # Return to result for user menu

        # Error result if username and password don't match
        print("Wrong username or password, please try again.\n")

    # Error exception
    except Exception as e:
        print(f"Error: {e}. Please contact admin.")