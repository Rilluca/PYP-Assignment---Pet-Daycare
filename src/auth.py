# Login and register authorization file for user

# Import function from other Python files
from data_manage import save_user_register

# Credentials for admin login
admin_username = "admin13579"
admin_password = "1234"

# Function to verify and authorize login
def login():
    try:
        # Ask user for username and password input
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Verify login credentials for admin
        if username == admin_username and password == admin_password:
            print("Welcome admin, select your role for today.")
            return True # Break when true

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
                    return True

        # Error result if username and password don't match
        print("Wrong username or password, please try again.\n")
        return False

    # Error exception
    except Exception as e:
        print("Error:", e)