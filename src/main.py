# Run the program here, this will be the main of the program

# Import other Python files
import auth

# Welcome message to welcome user
welcome_message = f"""
{'-' * 50}
Welcome to Paws & Play Hub management system!
{'-' * 50}
Please log in to continue.
"""

# Print the welcome message
print(welcome_message)

# Create a login loop for authorization, if username and password are wrong,
# User can try again without running the program again
while True:
    # Call the login() function and store the result as result
    result = auth.login()

    # If credentials match, *break the program*
    if result == True:
        break

