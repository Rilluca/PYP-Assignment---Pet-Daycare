# Read and write function for everything

# Function to register user
# Need to add validation here later
def save_user_register(username, user_password):
    is_alphabet = True
    for c in username:
        if not ((c >= "a" and c <= "z" ) or (c >= "A" and c <= "Z")):
            is_alphabet = False
            break
    if not is_alphabet:
        return "Username can only contain alphabets"

    with open("../data/users.txt", "r") as file:
         for line in file:
            if line.strip().split(",")[0] == username:
                return "Username is already taken."

        #Open file in append mode to add in new users
    with open("../data/users.txt", "a") as file:
        file.write(f"{username},{user_password}\n")
    return True


