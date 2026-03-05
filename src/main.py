# Run the program here, this will be the main of the program

# Import other Python files
import auth
import pet_owner

# Welcome message to welcome user
welcome_message = f"""
{'-' * 50}
Welcome to Paws & Play Hub management system!
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
    while True:
        # Call the login() function and store the result of login as result
        result = auth.login()

        # If result return "admin", print admin menu
        if result == "admin":
            show_admin_menu()
            break

        # If result return "user", print user menu
        if result == "user":
            pet_owner.pet_owner_menu()
            break

# Function to show admin menu
def show_admin_menu():
    # Print admin menu
    print(admin_menu)

    # Create a loop for validating input
    while True:
        try:
            # Ask user for choice input
            choice_input = int(input("Enter your choice: "))

            # Match case for menu selection
            match choice_input:
                case 1:
                    print("replace function to system admin here")
                    break

                case 2:
                    print("replace function to booking officer here")
                    break

                case 3:
                    print("replace function to grooming/daycare staff here")
                    break

                case 4:
                    print("replace function to facility assistant here")
                    break

                case 5:
                    print("Quitting program now.")
                    break

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

# Call main menu
show_main_menu()