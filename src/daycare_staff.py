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
1. Update Pet Care Status
2. Log Daily Records
3. Generate Summary Report
4. Quit
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

                    valid_choice = True

                case 2:
                    print("replace function to booking officer here")
                    valid_choice = True

                case 3:
                    print("abc")
                    valid_choice = True

                case 4:
                    print("Quitting program now.")
                    valid_choice = True

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

# Own function to count len
def count_len(ori_list):
    count = 0

    for item in ori_list:
        count += 1
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

# Function to show add care menu and options
def add_care_menu():
    # Ask for user input
    print("\n" + '-' * 50)
    print("Add New Record")
    print('-' * 50)

    pet_id = input("Enter Pet ID (PTxxx): ")
    pet_name = input("Enter Pet Name: ")

    # Selection input for care type
    print("Choose Care Type:")
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
    print("Choose Status:")
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

    date = input("Enter Date (dd/mm/yyyy): ")

    add_care_records(pet_id, pet_name, care_type, status, date)

    print("Log added successfully!")

#