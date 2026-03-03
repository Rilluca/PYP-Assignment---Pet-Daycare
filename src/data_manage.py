# Read and write function for everything

# Function to register user
# Need to add validation here later
def save_user_register(username, user_password):
        #Open file in append mode to add in new users
        with open("users.txt", "a") as file:
            file.write(f"{username},{user_password}\n")
        return True