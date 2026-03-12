# All functions for daycare/grooming staff will be here
# - Update pet care status (feeding, grooming, activities).
# - Log daily care and grooming records.
# - Generate service summary report.
from src.booking_officer import bookingOfficer_menu, show_bookingOfficer_menu

# Menu message for daycare/grooming staff
daycare_staff_menu = f"""
{'-' * 50}
Daycare/Grooming Staff Menu
{'-' * 50}
What would you like to do today?
1. Manage Pet Care Status
2. View All Record
3. Generate Summary Report
4. Quit
"""

# Menu message for pet care status
pet_care_menu = f"""
{'-' * 50}
Manage Pet Care Status
{'-' * 50}
What would you like to do today?
1. Log New Record
2. Update an Existing Record
3. Remove a Record
4. Return to previous menu
"""

# Function to show the manu for daycare/grooming staff
def show_daycare_staff_menu():
    # Print the menu
    print(daycare_staff_menu)

    # Create a loop to validate the input choice
    valid_choice = False
    while not valid_choice:
        try:
            # Ask user for choice input
            daycare_staff_choice = int(input("Enter your choice: "))

            # Match case for menu selection
            match daycare_staff_choice:
                case 1:
                    show_pet_care_menu()
                    valid_choice = True

                case 2:
                    view_all_records()
                    valid_choice = True

                case 3:
                    print("generate summary report function")
                    valid_choice = True

                case 4:
                    print("Quitting program now.")
                    valid_choice = True

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

# Function to show the manu for daycare/grooming staff
def show_pet_care_menu():
    # Print the menu
    print(pet_care_menu)

    # Create a loop to validate the input choice
    valid_choice = False
    while not valid_choice:
        try:
            # Ask user for choice input
            pet_care_choice = int(input("Enter your choice: "))

            # Match case for menu selection
            match pet_care_choice:
                case 1:
                    add_care_menu()
                    valid_choice = True

                case 2:
                    print("replace function to booking officer here")
                    valid_choice = True

                case 3:
                    print("abc")
                    valid_choice = True

                case 4:
                    show_daycare_staff_menu()
                    valid_choice = True

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

# Own function to count len
def count_len(ori_list):
    count = 0

    # For each item in the list
    for item in ori_list:
        # Increment count by 1
        count += 1
    # Return the number back to count
    return count

# Own function to append to list
def append_to_end(ori_list, item_to_append):
    ori_list[count_len(ori_list):count_len(ori_list)] = [item_to_append]
    return ori_list

# Function to add care records
def add_care_records(pet_id, pet_name, care_type, status, date):
    # Format for care record
    new_record = pet_id + "," + pet_name + "," + care_type + "," + status + "," + date + "\n"

    # Read all lines in files
    with open("../data/care_records.txt", "r") as f:
        # Read all lines in txt files as list
        record_list = f.readlines()

    # Append new record into the record list
    append_to_end(record_list, new_record)

    # Write the updated list back into txt file
    with open("../data/care_records.txt", "w") as f:
        for record in record_list:
            f.write(record)

# Function for selecting the pet for add_care_menu
def select_pet_menu():
    # Section to print the pet menu
    with open("../data/pet.txt", "r") as f:
        pet_list = f.readlines()

        # Counter for numbering of the menu
        menu_index = 1

        print(f"{'No':<3} | {'Pet ID':<8} | {'Pet Name':12}")

        for pet in pet_list:
            pet_data = pet.strip().split(",")

            print(f"{menu_index:<3} | {pet_data[1]:<8} | {pet_data[0]:12}")

            # Numbering will increase for each loop of data
            menu_index += 1

    # Section to validate the input and return the value back
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nChoose a pet to add record for: "))

            # Check if input is within the length of the txt file
            if 1 <= choice <= len(pet_list):
                # Choice = index - 1
                selected_pet = pet_list[choice - 1]
                # Split the selected line
                selected_pet_data = selected_pet.strip().split(",")
                valid_choice = True

                # Return back pet name and pet ID because that's what we only need now
                return selected_pet_data[0], selected_pet_data[1]

            else:
                print("Number out of range, please try again.")

        except ValueError:
            print("Invalid input, please try again.\n")

# Function to show add care menu and options
def add_care_menu():
    # Ask for user input
    print("\n" + '-' * 50)
    print("Add New Record")
    print('-' * 50)

    # Call function to select pet
    pet_id, pet_name = select_pet_menu()

    # Selection input for care type
    print("\nChoose Care Type:")
    print("1. Feeding")
    print("2. Grooming")
    print("3. Activities")

    valid_choice = False
    while not valid_choice:
        try:
            care_type = int(input("Enter care type: "))

            match care_type:
                case 1:
                    care_type = "Feeding"
                    valid_choice = True

                case 2:
                    care_type = "Grooming"
                    valid_choice = True

                case 3:
                    care_type = "Activities"
                    valid_choice = True

                case _:
                    print("Invalid input, please try again.\n")

        except ValueError:
            print("Invalid input, please try again.\n")

    # Selection input for status
    print("\nChoose Status:")
    print("1. Pending")
    print("2. In-progress")
    print("3. Done")

    valid_choice = False
    while not valid_choice:
        try:
            status = int(input("Enter status: "))

            match status:
                case 1:
                    status = "Pending"
                    valid_choice = True

                case 2:
                    status = "In-progress"
                    valid_choice = True

                case 3:
                    status = "Done"
                    valid_choice = True

                case _:
                    print("Invalid input, please try again.\n")

        except ValueError:
            print("Invalid input, please try again.\n")

    date = input("\nEnter Date (dd/mm/yyyy): ")

    add_care_records(pet_id, pet_name, care_type, status, date)

    print("Log added successfully!")

# Function to view all data in care_records.txt
def view_all_records():
    with open("../data/care_records.txt", "r") as f:
        record_list = f.readlines()

        # Counter for the numbering of data
        menu_index = 1

        # Print the data into specific format
        print('-' * 50)
        print("Viewing All Pet Care Records")
        print('-' * 50)
        print(f"{'No':<3} | {'Pet ID':<8} | {'Pet Name':12} | {'Care Type':12} | {'Status':12} | {'Date':12}")

        for record in record_list:
            record_data = record.strip().split(",")

            print(f"{menu_index:<3} | {record_data[1]:<8} | {record_data[0]:12} | {record_data[2]:12} | {record_data[3]:12} | {record_data[4]:12}")

            # Numbering will increase for each loop of data
            menu_index += 1

    # Loop to ask user if they want to go back to previous menu
    valid_choice = False
    while not valid_choice:
        choice = input("\nWould you like to go back to previous menu? N will quit the program. (y/n): ")

        if choice == 'y' or choice == 'Y':
            show_daycare_staff_menu()
            valid_choice = True
        elif choice == 'n' or choice == 'N':
            print("Exiting program now.")
            valid_choice = True
        else:
            print("Invalid input, please try again.")

