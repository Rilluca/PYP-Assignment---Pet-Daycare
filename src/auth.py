# Login and register authorization for user

from data_manage import save_user_register

# Section for registering new user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    success = save_user_register(username, password)

    if success:
        print("User registered successfully!")