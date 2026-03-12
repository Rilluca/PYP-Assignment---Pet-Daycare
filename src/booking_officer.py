# All features for booking officer here
# - Register new pet owners and their pets.
# - Process daycare and grooming bookings (reserve, cancel, reschedule).
# - View current bookings and pet service history.

bookingOfficer_menu = f"""
{'-' * 50}
Booking Officer Menu
{'-' * 50}
Welcome Booking Officer, select your option:
1. Register New Pet Owner
2. Register New Pet
3. Manage Bookings
4. View Bookings
5. View Service History
6. Quit
"""

manageBooking_menu = f"""
{'-' * 50}
Manage Bookings Menu
{'-' * 50}
Welcome to the Manage Bookings Menu, what would you like to do?
1. Add New Booking
2. Edit Existing Booking
3. Delete Booking
4. Return
"""

def automatic_booking_id():
    try:
        with open('booking.txt', 'r') as f:
            count = 0
            line = f.readline()
            while line != "":
                count += 1
                line = f.readline()
    except:
        count = 0

    num = str(count + 1)
    while len(num) < 6:
        num = "0" + num

    booking_id = "BK" + num
    return booking_id

def automatic_pet_id():
    try:
        with open('../data/pet.txt', 'r') as f:
            count = 0
            line = f.readline()
            while line != "":
                count += 1
                line = f.readline()
    except:
        count = 0

    num = str(count + 1)
    while len(num) < 3:
        num = "0" + num

    pet_id = "PT" + num
    return pet_id

def register_new_pet_owner():
    is_alphabet = True
    username = input("Enter username:")
    user_password = input("Enter password:")
    for c in username:
        if not ((c >= "a" and c <= "z") or (c >= "A" and c <= "Z")):
            is_alphabet = False
            break

    if not is_alphabet:
        return "Username can only contain alphabets"

    if user_password == "":
        return "Password cannot be empty"

    with open("users.txt", "r") as file:
        for line in file:
            if line.strip().split(",")[0] == username:
                return "Username is already taken."

    # Open file in append mode to add in new users
    with open("users.txt", "a") as file:
        file.write(f"{username},{user_password}\n")
    return "Pet owner registered successfully"

def register_new_pet():
    username = input("Enter username:")
    pet_name = input("Enter pet name:")
    user_password = input("Enter password:")

    is_alphabet = True
    for c in username:
        if not ((c >= "a" and c <= "z" ) or (c >= "A" and c <= "Z")):
            is_alphabet = False
            break
    if not is_alphabet:
        return "Username can only contain alphabets"

    is_alphabet = True
    for c in pet_name:
        if not ((c >= "a" and c <= "z" ) or (c >= "A" and c <= "Z")):
            is_alphabet = False
            break
    if not is_alphabet:
        return "Pet name can only contain alphabets"

        #Open file in append mode to add in new users
    with open("../data/pet.txt", "a+") as file:
        file.seek(0)
        for line in file:
            if line.strip().split(",")[0] == username:
                return "Username is already taken."

        pet_id = automatic_pet_id()
        file.write(username + "," + pet_id + "," + pet_name + "," + user_password + "\n")
    return "Pet registered successfully."

def add_new_booking():
    username = input("Please enter owner name:")
    pet_id = input("Please enter the pet_id:")
    date = input("Enter date to book (DD-MM-YYYY):")

    if username == "" or pet_id == "" or date == "":
        print("Every field must be filled")
        return

    booking_id = automatic_booking_id()
    print("Your Booking ID is:", booking_id)
    try:
        with open("booking.txt", "a") as f:
            text = booking_id + "," + username + "," + date + "," + pet_id + "\n"
            f.write(text)
            print("Booking added successful")
    except Exception as e:
        print("Booking failed", e)

def edit_existing_booking():
    def edit_existing_booking():
        pet_id = input("Enter Pet ID to edit booking: ")

        file = open("booking.txt", "r")
        lines = file.readlines()
        file.close()

        found = False
        new_lines = []

        for line in lines:
            data = line.strip().split(",")

            if data[0] == pet_id:
                found = True
                print("Current Booking:", line.strip())

                new_date = input("Enter new booking date: ")
                new_service = input("Enter new service: ")

                updated_line = pet_id + "," + new_date + "," + new_service + "\n"
                new_lines.append(updated_line)
            else:
                new_lines.append(line)

        if found:
            file = open("booking.txt", "w")
            file.writelines(new_lines)
            file.close()
            print("Booking updated successfully.")
        else:
            print("Pet ID not found.")

def delete_booking():
    pet_id = input("Please enter the pet_id: ").strip()
    result = False

    try:
        with open("booking.txt", "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            data = line.strip().split(",")
            if data[0] != pet_id:
                new_lines.append(line)
            else:
                result = True

        with open("booking.txt", "w") as f:
            f.writelines(new_lines)

        if result:
            print("Booking deleted successfully.")
        else:
            print("Pet ID not found.")

    except FileNotFoundError:
        print("booking.txt file not found.")

def view_bookings():
    pet_id = input("Please enter the pet_id: ").strip()
    Result = False

    try:
        with open("booking.txt", "r") as f:
            print(f"\n--- Booking for {pet_id} ---")
            for line in f:
                # Clean the line and split by comma
                parts = line.strip().split(",")

                # Check if the list has enough data and matches exactly
                # Assuming pet_id is index 0
                if len(parts) > 0 and parts[0] == pet_id:
                    print(f"Date: {parts[1]} | Service: {parts[2]} | Status: {parts[3]}")
                    Result = True

            if not Result:
                print("No bookings found for this Pet ID.")

    except FileNotFoundError:
        print("File not found")

def view_service_history():
    pet_id = input("Please enter the pet_id: ").strip()
    Result = False

    try:
        with open("service_history.txt", "r") as f:
            print(f"\n--- Service History for {pet_id} ---")
            for line in f:
                # Clean the line and split by comma
                parts = line.strip().split(",")

                # Check if the list has enough data and matches exactly
                # Assuming pet_id is index 0
                if len(parts) > 0 and parts[0] == pet_id:
                    print(f"Date: {parts[1]} | Service: {parts[2]} | Status: {parts[3]}")
                    Result = True

            if not Result:
                print("No records found for this Pet ID.")

    except FileNotFoundError:
        print("File not found")

def check_input_3():
    while True:
        try:
            BO2_input = int(input("Enter your choice: "))
            match BO2_input:
                case 1:
                    print("Add New Booking(s) here")
                    add_new_booking()
                    break

                case 2:
                    print("Edit Existing Booking(s) here")
                    edit_existing_booking()
                    break

                case 3:
                    print("Delete Booking(s) here")
                    delete_booking()
                    break

                case 4:
                    print("Returning to menu")
                    break

                case _:
                    print("Input can only be in number and within range, please try again\n")

        except Exception as e:
            print(f"Error: {e}. Input can only be in number and within range, please try again\n")


def show_bookingOfficer_menu():
        # Print Booking Officer menu
        print(bookingOfficer_menu)

        # Create a loop for validating input
        while True:
            try:
                # Ask officer for choice input
                BO_input = int(input("Enter your choice: "))

                # Match case for menu selection
                match BO_input:
                    case 1:
                        print("Register New Pet Owner(s) here")
                        register_new_pet_owner()
                        break

                    case 2:
                        print("Register New Pet(s) here")
                        register_new_pet()
                        break

                    case 3:
                        print("Manage Bookings Menu here")
                        print(manageBooking_menu)
                        check_input_3()
                        break

                    case 4:
                        print("View Bookings here")
                        view_bookings()
                        break

                    case 5:
                        print("View Service History here")
                        view_service_history()
                        break

                    case 6:
                        print("Exiting menu now")
                        break

                    case _:
                        print("Input can only be in number and within range, please try again\n")

            except Exception as e:
                print(f"Error: {e}. Input can only be in number and within range, please try again\n")

