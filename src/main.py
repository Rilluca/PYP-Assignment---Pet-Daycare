# Run the program here, this will be the main of the program

import auth

# Welcome message to welcome user
welcome_message = f"""
{'-' * 50}
Welcome to Paws & Play Hub management system!
{'-' * 50}
Select your role: 
1. Pet Owner Login
2. Staff Login
"""

#Print the welcome message
print(welcome_message)
# User input for menu selection
user_choice = int(input("Choose a menu option: "))

match user_choice:
    case 1:
        pass

    case 2:
        auth.register_user()



from data_manage import save_user_register


def validate_username():
    while True:
        print("1. Register")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result = save_user_register(username, password)
            if result:
                print("User successfully registered!")

        elif choice == "2":
            print("The system has ended")
            break

        else:
            print("Invalid choice")

validate_username()

