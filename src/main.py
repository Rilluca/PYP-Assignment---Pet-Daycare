# Run the program here, this will be the main of the program

# Import other Python files
import pet_owner
import daycare_staff

# Welcome message to welcome user
welcome_message = f"""
{'-' * 50}
Welcome to Paws & Play Hub Booking and Management System!
{'-' * 50}
Please log in to continue.
"""

# Menu message for admin
admin_menu = f"""
{'-' * 50}
Admin Menu
{'-' * 50}
Welcome admin, select your role for today.
1. System Administrator
2. Booking Officer
3. Grooming/Daycare Staff
4. Facility Assistant
5. Quit
"""

# Function to show the main menu
def show_main_menu():
    # Print the welcome message
    print(welcome_message)

    # Create a login loop for authorization
    # If username and password are wrong, user can try again without running the program again
    logged_in = False
    while not logged_in:
        # Call the login() function and store the result of login as result
        result = login()

        # If result return "admin", print admin menu
        if result == "admin":
            show_admin_menu()
            logged_in = True

        # If result return "user", print user menu
        elif result == "user":
            pet_owner.pet_owner_menu()
            logged_in = True

# Function to show admin menu
def show_admin_menu():
    # Print admin menu
    print(admin_menu)

    # Create a loop for validating input
    valid_choice = False
    while not valid_choice:
        try:
            # Ask user for choice input
            choice_input = int(input("Enter your choice: "))

            # Match case for menu selection
            match choice_input:
                case 1:
                    print("replace function to system admin here")
                    valid_choice = True

                case 2:
                    print("replace function to booking officer here")
                    valid_choice = True

                case 3:
                    daycare_staff.show_daycare_staff_menu()
                    valid_choice = True

                case 4:
                    print("replace function to facility assistant here")
                    valid_choice = True

                case 5:
                    print("Exiting program now")
                    valid_choice = True

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

# Credentials for admin login
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
            return "admin"  # Return to result for admin menu

        # Open users.txt in read mode
        with open("../data/users.txt", "r") as file:
            # Read all lines in the txt file
            credential_list = file.readlines()

            for line in credential_list:
                # Strip empty lines created by readlines() and split credentials by comma
                credentials = line.strip().split(",")

                # If user input equals to credentials
                if username == credentials[0] and password == credentials[1]:
                    print("Login successful!")
                    return "user"  # Return to result for user menu

        # Error result if username and password don't match
        print("Wrong username or password, please try again.\n")

    # Error exception
    except Exception as e:
        print(f"Error: {e}. Please contact admin.")

# Call main menu
show_main_menu()