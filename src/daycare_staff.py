# All functions for daycare/grooming staff will be here
# - Update pet care status (feeding, grooming, activities).
# - Log daily care and grooming records.
# - Generate service summary report.

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
                    generate_summary_report()
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
                    update_records()
                    valid_choice = True

                case 3:
                    remove_records()
                    valid_choice = True

                case 4:
                    show_daycare_staff_menu()
                    valid_choice = True

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

# Custom function to count len
# Source: from Lecturer Miss Chong Mien May
def count_len(ori_list):
    count = 0

    # For each item in the list
    for item in ori_list:
        # Increment count by 1
        count += 1
    # Return the number back to count
    return count

# Custom function to append to list
# Source: from Lecturer Miss Chong Mien May
def append_to_end(ori_list, item_to_append):
    # Use slicing method to append items at the end of the list
    # Because index = length - 1, when we slice to an empty index, we can append the item behind
    ori_list[count_len(ori_list):count_len(ori_list)] = [item_to_append]
    return ori_list

# Custom function to split words into list
# Source: An Yan, 2018, How to write my own split function without using .split and .strip function?, Stack Overflow
def custom_split(string):
    # List to hold split words
    split_list = []
    # To build each word by word
    word = ""

    for c in string:
        # If current character is not the delimiter
        if c not in ",":
            # Add current character to word if it's not a delimiter
            word += c
        else:
            # Append the word into split_list
            split_list = append_to_end(split_list, word)
            # Reset so previous word doesn't linger
            word = ""

    # Append the last word to list because there is no delimiter at the end of the string
    split_list = append_to_end(split_list, word)

    return split_list

# Custom function to strip "\n" after splitting each word in lines
# Source: Yolanda, 2016, Implement my own strip method in Python, Stack Overflow
def custom_strip(string):
    # Make sure string is not empty, get the last character of the string and check if it's newlines
    if count_len(string) > 0 and string[count_len(string) - 1] == '\n':
        # Use slicing to slice from the start up to the last character excluding newlines
        return string[0:count_len(string) - 1]
    return string

# Function to validate date format
# Source: Selected Topics in IT, 2023, Python 66: Date validation, verify correct date range and format (YYYY-MM-DD), YouTube
def validate_date():
    while True:
        date_input = input("Enter Date (dd/mm/yyyy): ")

        # Check the format of the date by length and separator
        # Must be exactly 10 characters and have '/' at position index 2 and 5
        if count_len(date_input) != 10 or date_input[2] != '/' or date_input[5] != '/':
            print("Invalid format. Please use dd/mm/yyyy (e.g., 13/03/2026).\n")
            continue

        # Extract date, month and year by slicing
        day = date_input[0:2]
        month = date_input[3:5]
        year = date_input[6:10]

        # Manual digit validation
        is_all_digits = True

        # Combine them to check all characters in one loop
        for char in (day + month + year):
            # Using range comparison
            if char < '0' or char > '9':
                is_all_digits = False
                break

        # If date does not contain numbers
        if not is_all_digits:
            print("Date can only contain numbers.\n")
            continue

        # Convert strings to integers for range validation
        day = int(day)
        month = int(month)
        year = int(year)

        # Check year
        if not (1900 <= year <= 2100):
            print("Year must be between 1900 and 2100.\n")
            continue

        # Check month
        if not (1 <= month <= 12):
            print("Month must be between 01 and 12.\n")
            continue

        # Check day
        if not (1 <= day <= 31):
            print("Day must be between 01 and 31.\n")
            continue

        # Specific logic for month with 30 days
        if month in [4, 6, 9, 11] and day > 30:
            print("This month only has 30 days.\n")
            continue

        # Specific logic for February
        if month == 2:
            # Check if it's a leap year
            is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

            # If it's a leap year
            if is_leap and day > 29:
                print(f"{year} is a leap year. February on leap year only has 29 days.")
                continue

            # If it's not a leap year
            if not is_leap and day > 28:
                print(f"{year} is not a leap year. February not on leap year only has 28 days.\n")
                continue

        # Return to the input
        return date_input

# Function for selecting the pet for add_care_menu (this one is only for specific data)
# Source: hjames, 2013, Extract a column from text file - Python, Stack Overflow
def select_pet():
    with open("../data/pet.txt", "r") as f:
        pet_list = f.readlines()

        # Counter for numbering of the menu
        menu_index = 1

        print(f"{'No':<3} | {'Pet ID':<8} | {'Pet Name':12}")

        # Read each pet in pet_list and then split and strip them
        for pet in pet_list:
            strip_pet_data = custom_strip(pet)
            pet_data = custom_split(strip_pet_data)

            # Get specific data column from text file to print
            print(f"{menu_index:<3} | {pet_data[1]:<8} | {pet_data[2]:12}")

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

                # Split and strip the selected line
                strip_pet_data = custom_strip(selected_pet)
                selected_pet_data = custom_split(strip_pet_data)
                valid_choice = True

                # Return back pet name and pet ID because that's what we only need now
                return selected_pet_data[2], selected_pet_data[1]

            else:
                print("Number out of range, please try again.")

        except ValueError:
            print("Invalid input, please try again.")

# Function to add care records
# Source: Bro Code, 2024, Write files using Python!, YouTube
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

# Function to show add care menu and options
def add_care_menu():
    # Ask for user input
    print("\n" + '-' * 50)
    print("Add New Record")
    print('-' * 50)

    # Return value of pet_id, pet_name from select_pet
    pet_id, pet_name = select_pet()

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

    date = validate_date()

    add_care_records(pet_id, pet_name, care_type, status, date)

    print("Log added successfully!\n")

    # Loop to ask user if they want to go back to previous menu
    valid_choice = False
    while not valid_choice:
        choice = input("Would you like to add another record? N will go back to previous menu. (y/n): ")

        if choice == 'y' or choice == 'Y':
            add_care_menu()
            valid_choice = True
        elif choice == 'n' or choice == 'N':
            show_pet_care_menu()
            valid_choice = True
        else:
            print("Invalid input, please try again.")

# Function to hold record viewing (this one is to show all the data in the text file)
def fetch_records():
    with open("../data/care_records.txt", "r") as f:
        record_list = f.readlines()

        # Counter for the numbering of data
        menu_index = 1

        for record in record_list:
            strip_record_data = custom_strip(record)
            record_data = custom_split(strip_record_data)

            # Print the data into specific format
            print(f"{menu_index:<3} | {record_data[1]:<8} | {record_data[0]:12} | {record_data[2]:12} | {record_data[3]:12} | {record_data[4]:12}")

            # Numbering will increase for each loop of data
            menu_index += 1

    return record_list

# Function to validate input from view_records
def view_all_records():
    print('-' * 50)
    print("Viewing All Pet Care Records")
    print('-' * 50)
    print(f"{'No':<3} | {'Pet ID':<8} | {'Pet Name':12} | {'Care Type':12} | {'Status':12} | {'Date':12}")

    fetch_records()

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

# Function to update pet care status
# Source: Coding With Sagar, 2024, Contact book app in Python | Python for beginners | #project11, YouTube
def update_records():
    print('-' * 50)
    print("Update Existing Record")
    print('-' * 50)
    print(f"{'No':<3} | {'Pet ID':<8} | {'Pet Name':12} | {'Care Type':12} | {'Status':12} | {'Date':12}")

    record_list = fetch_records()

    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nChoose a record to update: "))

            # Check if input is within the length of the txt file
            if 1 <= choice <= len(record_list):
                # Choice = index - 1
                selected_pet = record_list[choice - 1]

                # Strip and split the selected line
                strip_selected_pet = custom_strip(selected_pet)
                selected_pet_data = custom_split(strip_selected_pet)
                valid_choice = True
            else:
                print("Number out of range, please try again.")

        except ValueError:
            print("Invalid input, please try again.")

    valid_choice = False
    while not valid_choice:
        print(f"\nUpdate Status (Current Status: {selected_pet_data[3]})")
        print("1. Pending")
        print("2. In-progress")
        print("3. Done")

        try:
            status_choice = int(input("Enter new status: "))

            new_status = ""
            match status_choice:
                case 1:
                    new_status = "Pending"
                case 2:
                    new_status = "In-progress"
                case 3:
                    new_status = "Done"
                case _:
                    print("Invalid input, please try again.")
                    continue

            if new_status == selected_pet_data[3]:
                print("Cannot select the same status.")
            else:
                selected_pet_data[3] = new_status
                valid_choice = True

        except ValueError:
            print("Invalid input, please try again.")

    # Pass the data to validate in validate_date() function
    date = validate_date()
    selected_pet_data[4] = date

    updated_record_string = f"{selected_pet_data[1]},{selected_pet_data[0]},{selected_pet_data[2]},{selected_pet_data[3]},{selected_pet_data[4]}\n"

    record_list[choice - 1] = updated_record_string

    with open("../data/care_records.txt", "w") as f:
        for record in record_list:
            f.write(record)

    print("\nRecord updated successfully!")

    valid_choice = False
    while not valid_choice:
        choice = input("Would you like to edit another record? N will go back to previous menu. (y/n): ")

        if choice == 'y' or choice == 'Y':
            update_records()
            valid_choice = True
        elif choice == 'n' or choice == 'N':
            show_pet_care_menu()
            valid_choice = True
        else:
            print("Invalid input, please try again.")

# Function to remove an existing care record
# Source: Coding With Sagar, 2024, Contact book app in Python | Python for beginners | #project11, YouTube
def remove_records():
    print('-' * 50)
    print("Remove Existing Record")
    print('-' * 50)

    # Display records using the existing fetch function
    print(f"{'No':<3} | {'Pet ID':<8} | {'Pet Name':12} | {'Care Type':12} | {'Status':12} | {'Date':12}")

    record_list = fetch_records()

    # Validation loop for selecting which record to delete
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nChoose a record that you would like to remove: "))

            if 1 <= choice <= len(record_list):
                valid_confirm = False

                while not valid_confirm:
                    confirm = input(f"Are you sure you want to delete record {choice}? (y/n): ")

                    if confirm == 'y' or confirm == 'Y':
                        record_list[choice - 1: choice] = []

                        with open("../data/care_records.txt", "w") as f:
                            for record in record_list:
                                f.write(record)
                        print("\nRecord removed successfully!")
                        valid_confirm = True
                        valid_choice = True

                    elif confirm == 'n' or confirm == 'N':
                        print("\nDeletion cancelled.")
                        valid_confirm = True
                        valid_choice = True

                    else:
                        print("Invalid input, please enter 'y' or 'n'.")
            else:
                print("Number out of range, please try again.")

        except ValueError:
            print("Invalid input, please enter a number.")

    # Loop to ask user if they want to stay or go back
    valid_choice = False
    while not valid_choice:
        choice = input("Would you like to remove another record? N will go back to previous menu. (y/n): ")

        if choice == 'y' or choice == 'Y':
            remove_records()
            valid_choice = True

        elif choice == 'n' or choice == 'N':
            show_pet_care_menu()
            valid_choice = True

        else:
            print("Invalid input, please try again.")

# Function to generate and display a summary report of all services
def generate_summary_report():
    print('=' * 50)
    print("Service Summary Report")
    print('=' * 50)

    # Read the current records
    with open("../data/care_records.txt", "r") as f:
        record_list = f.readlines()

    # Initialize counters
    total_records = count_len(record_list)

    # Counters for care types
    feeding_count = 0
    grooming_count = 0
    activities_count = 0

    # Counters for status
    pending_count = 0
    inprogress_count = 0
    done_count = 0

    # Process data through the list
    for record in record_list:
        strip_record = custom_strip(record)
        data = custom_split(strip_record)

        # Count care types
        if data[2] == "Feeding":
            feeding_count += 1
        elif data[2] == "Grooming":
            grooming_count += 1
        elif data[2] == "Activities":
            activities_count += 1

        # Count status
        if data[3] == "Pending":
            pending_count += 1
        elif data[3] == "In-progress":
            inprogress_count += 1
        elif data[3] == "Done":
            done_count += 1

    # Display the summary results
    print(f"Total Services Logged: {total_records}")
    print("-" * 50)
    print("Breakdown by Care Type:")
    print(f"- Feeding    : {feeding_count}")
    print(f"- Grooming   : {grooming_count}")
    print(f"- Activities : {activities_count}")
    print("-" * 50)
    print("Breakdown by Status:")
    print(f"- Pending    : {pending_count}")
    print(f"- In-progress: {inprogress_count}")
    print(f"- Done       : {done_count}")
    print("=" * 50)

    valid_choice = False
    while not valid_choice:
        choice = input("\nPress 'Y' to return to the previous menu: ")

        if choice == 'y' or choice == 'Y':
            show_daycare_staff_menu()
            valid_choice = True
        else:
            print("Invalid input, please try again.")