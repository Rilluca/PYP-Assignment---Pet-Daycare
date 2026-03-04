# Run the program here, this will be the main of the program

# Import other Python files
import auth
import pet_owner
from pet_owner import pet_owner_menu

# Welcome message to welcome user
welcome_message = f"""
{'-' * 50}
Welcome to Paws & Play Hub management system!
{'-' * 50}
Please log in to continue.
"""

# Print the welcome message
print(welcome_message)

# Create a login loop for authorization
# If username and password are wrong, user can try again without running the program again
while True:
    # Call the login() function and store the result of login as result
    result = auth.login()

    # If result return "admin", print admin menu
    if result == "admin":
        print("abc")

    # If result return "user", print user menu
    if result == "user":
        pet_owner_menu()