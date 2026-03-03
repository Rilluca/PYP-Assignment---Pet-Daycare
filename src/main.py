# Run the program here, this will be the main of the program

from src import auth

# Welcome message to welcome user
welcome_message = f"""
{'-' * 50}
Welcome to Paws & Play Hub management system!
{'-' * 50}
Menu: 
1. Pet Owner Login
2. Pet Owner Register
3. Staff Login
"""

#Print the welcome message
print(welcome_message)

# User input for menu selection
user_choice = int(input("Choose a menu option: "))

match user_choice:
    case 2:
        auth.register_user()