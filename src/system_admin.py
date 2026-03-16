# All features for system administrator here
# - Manage pet records and service options (add, update, remove).
# - View all data (owners, pets, bookings, payments).
# - Generate overall service report (total bookings, revenue, available slots).
from src.booking_officer import automatic_pet_id

def manual_lens(x):
    count = 0          # initialize counter
    # iterate through each element in the collection
    for object in x:
        count = count + 1   # increase counter for every element found
    return count       # return total number of elements

def append_to_end(ori_list, item_to_append):
    # insert the new item at the end of the list using slicing
    ori_list[manual_lens(ori_list):manual_lens(ori_list)] = [item_to_append]
    # return the updated list
    return ori_list
#credit to lecturer Miss Chong Mien May

def manual_spilt(x, separator):
    result = []        # initialize empty list to store split parts
    current = ""       # temporary string to build current element
    # iterate through each character in the string
    for c in x:
        if c == separator:              # if current character is the separator
            append_to_end(result, current)  # add the collected string to result list
            current = ""                # reset temporary string for next element
        else:
            current += c                # otherwise, add character to temporary string
    # add the last element after the loop ends
    append_to_end(result, current)
    # return the list of split elements
    return result

def manual_strip(x):
        start = 0
        end = manual_lens(x) - 1
        #start become the starting position index
        while start <= end and (x[start] == " " or x[start] == "\n"):
            start += 1
        #end become the ending position index
        while end >= start and (x[end] == " " or x[end] == "\n"):
            end -= 1
        #delcare result
        result = ""
        i = start
        while i <= end:
            result += x[i] #add to result word by word back
            i += 1
        return result

def check_alphabet_and_empty_string_or_purely_spaces(x):

    is_alphabet = True   # flag to track if string is alphabetic
    count = 0            # total character counter
    s_count = 0          # space character counter
    # iterate through each character in the string
    for c in x:
        # if character is not alphabet or space, set flag to False
        if not ((c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c == " "):
            is_alphabet = False
        # count spaces
        if c == " ":
            s_count = s_count + 1
        # count total characters
        count = count + 1
    # if string is empty or contains only spaces, mark as not alphabetic
    if s_count == count or count == 0:
        is_alphabet = False
    # return the result
    return is_alphabet

def custom_lower(x):
    total = ""   # initialize string to store lowercase result
    # iterate through each character in the input string
    for c in x:
        c = custom_ord(c)   # convert character to ASCII-like value using custom_ord
        # if character is uppercase (ASCII A-Z), convert to lowercase by adding 32
        if 64 < c < 91:
            c = c + 32
        c = custom_chr(c)   # convert back to character using custom_chr
        total = total + c   # append to result string
    # return the fully lowercase string
    return total

def custom_ord(x):
#A string of characters in their exact ASCII order
#The character are starting from 32 as other
        lookup = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        # Manually search for the character
        index = 0

        for c in lookup:

            if c ==x:
                return index + 32 #for a proper ASCII
            index += 1

        return -1

def custom_chr(x):
    lookup = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    # Adjust for the starting offset of 32
    target_index = x - 32
    # Manually find the character at that index
    current_index = 0

    for c in lookup:

        if current_index == target_index:
            return c
        current_index += 1

    return ""  # Out of range in lookup


def sys_viewdata():
    # Infinite loop to continuously show the menu until user chooses to exit
    while True:
        print("""
    ===========================
    View All Data
    ===========================
    What data to view?
    1.Pet owners
    2.Pets
    3.Bookings
    4.Payments
    5.Exit
        """)
        try:
            # Get user choice and convert to integer
            option = int(input("Your choice: "))

            # Handle menu options using pattern matching
            match option:

                case 1:
                    # Option 1: View pet owners and their pets
                    with open("../data/users.txt", "r") as file:
                        credential_list = file.readlines()  # read all user records

                        # Iterate through each user
                        for line in credential_list:
                            credentials = manual_strip(line)  # remove extra spaces/newlines
                            credentials = manual_spilt(credentials, ",")  # split by comma
                            print("User/pet owner-", credentials[0], end="\n")
                            print("User's password-", credentials[1], end="\n\n")

                            # Open pet file to show pets for this user
                            with open("../data/pet.txt", "r") as file:
                                pet_list = file.readlines()
                                not_found = True  # flag to track if user has pets

                                # Iterate through each pet
                                for line in pet_list:
                                    pet_data = manual_strip(line)
                                    pet_data = manual_spilt(pet_data, ",")

                                    # If pet belongs to current user, print info
                                    if pet_data[0] == credentials[0]:
                                        print("Pet-", pet_data[2], "(", pet_data[1], ")", end="\n\n")
                                        not_found = False

                                # If no pets found for this user, print message
                                if not_found == True:
                                    print("No pet found for this user data\n")

                case 2:
                    # Option 2: View all pets
                    with open("../data/pet.txt", "r") as file:
                        pet_list = file.readlines()

                        # Print each pet record
                        for line in pet_list:
                            pet_data = manual_strip(line)
                            pet_data = manual_spilt(pet_data, ",")
                            print("Pet_Id-", pet_data[1], end="\n")
                            print("Pet-", pet_data[2], end="\n")
                            print("Pet Owner-", pet_data[0], end="\n\n")

                case 3:
                    # Option 3: View all bookings
                    with open("../data/booking.txt", "r") as file:
                        booking_list = file.readlines()

                        # Print each booking record
                        for line in booking_list:
                            booking_data = manual_strip(line)
                            booking_data = manual_spilt(booking_data, ",")
                            print("Booking ID-", booking_data[0], end="\n")
                            print("Username-", booking_data[1], end="\n")
                            print("Date-", booking_data[2], end="\n\n")

                case 4:
                    # Option 4: View payment/service history
                    with open("../data/service_history.txt", "r") as file:
                        payment_list = file.readlines()

                        # Print each payment record
                        for line in payment_list:
                            payment_data = manual_strip(line)
                            payment_data = manual_spilt(payment_data, ",")
                            print("Username-", payment_data[1], end="\n")
                            print("Date-", payment_data[2], end="\n")
                            print("Status-", payment_data[5], end="\n")
                            print("Payment- RM", payment_data[4], end="\n\n")

                case 5:
                    # Option 5: Exit the view data menu
                    print("Exiting program")
                    break

                case _:
                    # Handle invalid menu choices
                    print("Enter a Valid option")

        except ValueError:
            # Handle non-integer input
            print("Invalid choice. Please try again.")

        except Exception:
            # Catch any other unexpected errors
            print("Unknown error occured. Please try again.")

def sys_manage():
    # Infinite loop to keep the management menu active until user exits
    while True:
        # Display management menu options
        print("""
    ===========================
    Manage
    ===========================
    What do you want to manage?
    1.Service options
    2.Pet records
    3.Exit
        """)


        try:
            # Prompt user for input and convert to integer
            option = int(input("Your choice: "))

            # Match user choice to corresponding actions
            match option:

                case 1:
                    # Option 1: Manage service options (add, update, remove)
                    sys_service_option1()

                case 2:
                    # Option 2: Manage pet records (add, update, remove)
                    sys_service_option2()

                case 3:
                    # Option 3: Exit the management menu
                    print("Exiting program")
                    break

                case _:
                    # Handle any input outside 1-3
                    print("Enter a valid option")

        except ValueError:
            # Handle non-integer input
            print("Invalid choice. Please try again.")

        except Exception:
            # Catch all other unexpected errors
            print("Unknown error occured. Please try again.")

def sys_service_option1():
    # Infinite loop to keep the service management menu active until user exits
    while True:
        # Display menu options for service management
        print("""
    ===========================
    Manage
    ===========================
    What would you like to do?
    1.Add
    2.Update
    3.Remove
    4.Exit
        """)

        try:
            # Prompt user to choose an option and convert input to integer
            option = int(input("Your choice: "))

            # Match the user's input to corresponding actions
            match option:

                case 1:
                    # CASE 1: Add a new service
                    while True:
                        no_found = True  # Flag to check if service already exists

                        while True:
                            # Ask user for service name
                            service = input("Enter service name:")
                            # Validate that service name contains only letters and spaces
                            check_alpha = check_alphabet_and_empty_string_or_purely_spaces(service)

                            if check_alpha:
                                break  # Exit inner loop if validation passes
                            else:
                                print("Enter a valid service (only alphabet)")

                        # Read existing services from file
                        with open("../data/Service.txt", "r") as file:
                            service_list = file.readlines()

                            # Check if service already exists
                            for line in service_list:
                                service_data = manual_strip(line)   # Remove whitespace
                                service_data = manual_spilt(service_data, ",")  # Split by comma

                                if service == service_data[0]:
                                    print("Service already exists")
                                    no_found = False
                                    break

                        # If service does not exist, exit outer loop
                        if no_found:
                            break

                    # Ask user for price input and validate it
                    while True:
                        try:
                            payment = int(input("Enter price of the service: "))
                        except ValueError:
                            print("Enter valid price")
                        else:
                            break

                    # Append the new service and price to the file
                    with open("../data/Service.txt", "a+") as file:
                        file.write(f"{service},{payment}\n")

                    print("Added")  # Confirm addition

                case 2:
                    # CASE 2: Update an existing service
                    service = input("Enter service to update: ")

                    # Read current services
                    with open("../data/Service.txt", "r") as file:
                        service_list = file.readlines()

                    found = False
                    index = 0  # Counter to track line index

                    for line in service_list:
                        service_data = manual_strip(line)
                        service_data = manual_spilt(service_data, ",")

                        if service_data[0] == service:
                            found = True
                            print("Current data:", service_data)
                            # Ask which field to update
                            field = input("Which field to update? (service name/price): ")
                            field = custom_lower(field)  # Normalize input

                            if field == "service name":
                                # Update service name
                                while True:
                                    service = input("Enter service name:")
                                    check_alpha = check_alphabet_and_empty_string_or_purely_spaces(service)
                                    inlist = False
                                    with open("../data/Service.txt", "r") as file:
                                        service_list = file.readlines()  # read all user records
                                        # Iterate through each user
                                        for line in service_list:
                                            services = manual_strip(line)  # remove extra spaces/newlines
                                            services = manual_spilt(services, ",")  # split by comma
                                            if services[0] == service:
                                                inlist = True
                                                break
                                    if check_alpha and inlist==False:
                                        break
                                    else:
                                        print("Enter a valid service that isn't already repeated or is alphabet")

                                service_data[0] = service
                                print("Service Name updated successfully.")

                            elif field == "price":
                                # Update service price
                                while True:
                                    try:
                                        payment = int(input("Enter price: "))
                                        payment = str(payment)
                                    except ValueError:
                                        print("Ernter valid price")
                                    else:
                                        break

                                service_data[1] = payment
                                print("Service price updated successfully.")
                            else:
                                # Invalid field input
                                print("Invalid field.")

                            # Update the service list in memory
                            service_list[index] = ",".join(service_data) + "\n"
                            break

                        index += 1

                    if not found:
                        print("Service name not found.")

                    # Write updated services back to file
                    with open("../data/Service.txt", "w") as file:
                        file.writelines(service_list)

                case 3:
                    # CASE 3: Remove an existing service
                    service = input("Enter the service you want to remove: ")

                    # Read all services
                    with open("../data/Service.txt", "r") as file:
                        service_list = file.readlines()

                    found = False
                    index = 0  # Counter for line index

                    for line in service_list:
                        service_data = manual_strip(line)
                        service_data = manual_spilt(service_data, ",")

                        if service_data[0] == service:
                            # Delete the line corresponding to the service
                            del service_list[index]
                            found = True
                            break

                        index += 1

                    if found:
                        # Save updated service list to file
                        with open("../data/Service.txt", "w") as file:
                            file.writelines(service_list)

                        print("Service deleted successfully.")
                    else:
                        print("Service not found.")

                case 4:
                    # CASE 4: Exit the service management menu
                    break

                case _:
                    # Handle invalid input outside 1-4
                    print("Enter a valid option")

        except ValueError:
            # Handle non-integer input
            print("Invalid choice. Please try again.")

        except Exception:
            # Catch-all for unexpected errors
            print("Unknown error occured. Please try again.")

def sys_service_option2():
    # Infinite loop to keep the pet record management menu active until user exits
    while True:
        # Display menu options for managing pet records
        print("""
    ===========================
    Manage
    ===========================
    What would you like to do?
    1.Add
    2.Update
    3.Remove
    4.Exit
        """)

        try:
            # Prompt user to choose an option and convert input to integer
            option = int(input("Your choice: "))

            # Match the user's input to the corresponding action
            match option:

                case 1:
                    # CASE 1: Add a new pet record
                    while True:
                        username = input("Enter username:")
                        # Validate that username contains only letters and spaces
                        check_alpha = check_alphabet_and_empty_string_or_purely_spaces(username)
                        inlist = False
                        with open("../data/users.txt", "r") as file:
                            credential_list = file.readlines()  # read all user records
                            # Iterate through each user
                            for line in credential_list:
                                credentials = manual_strip(line)  # remove extra spaces/newlines
                                credentials = manual_spilt(credentials, ",")  # split by comma
                                if credentials[0] == username:
                                    inlist = True
                        if check_alpha and inlist:
                            break
                        else:
                            print("Enter a valid name that is in the user file and is alphabet")

                    while True:
                        pet = input("Enter pet name: ")
                        # Validate that pet name contains only letters and spaces
                        check_alpha = check_alphabet_and_empty_string_or_purely_spaces(pet)
                        if check_alpha:
                            break
                        else:
                            print("A pet name can only contain alphabets")

                    # Generate unique pet ID using external function
                    pet_ID = automatic_pet_id()

                    # Append the new pet record to file
                    with open("../data/pet.txt", "a") as file:
                        file.write(f"{username},{pet_ID},{pet}\n")

                    print("Added")  # Confirm addition

                case 2:
                    # CASE 2: Update an existing pet record
                    PetID = input("Enter pet ID to update: ")

                    # Read all pet records
                    with open("../data/pet.txt", "r") as file:
                        pet_list = file.readlines()

                    found = False
                    index = 0  # Counter for line index

                    for line in pet_list:
                        pet_data = manual_strip(line)   # Remove whitespace
                        pet_data = manual_spilt(pet_data, ",")  # Split by comma

                        if pet_data[1] == PetID:
                            found = True
                            print("Current data:", pet_data)
                            # Ask user which field to update
                            field = input("What would you like to update? pet(or)petowner/username: ")
                            field = custom_lower(field)  # Normalize input

                            if field == "pet":
                                # Update pet name
                                while True:
                                    pet = input("Enter pet's new name: ")
                                    isalpha = check_alphabet_and_empty_string_or_purely_spaces(pet)
                                    if isalpha:
                                        break
                                    else:
                                        print("A pet name can only contain alphabets")
                                pet_data[2] = pet
                                print("Pet name updated successfully.")

                            elif field == "username" or field == "petowner":
                                # Update owner username
                                while True:
                                    username = input("Enter username:")
                                    check_alpha = check_alphabet_and_empty_string_or_purely_spaces(username)
                                    inlist = False
                                    with open("../data/users.txt", "r") as file:
                                        credential_list = file.readlines()  # read all user records
                                    # Iterate through each user
                                        for line in credential_list:
                                            credentials = manual_strip(line)  # remove extra spaces/newlines
                                            credentials = manual_spilt(credentials, ",")  # split by comma
                                            if credentials[0]==username:
                                                inlist=True
                                    if check_alpha and inlist :
                                        break
                                    else:
                                        print("Enter a valid name that is in the user file and is alphabet")
                                pet_data[0] = username

                            else:
                                # Invalid field input
                                print("Invalid input.")

                            # Update the pet record in memory
                            pet_list[index] = ",".join(pet_data) + "\n"
                            break  # Exit loop once record is found

                        index += 1

                    if not found:
                        print("Pet ID not found.")

                    # Write updated pet records back to file
                    with open("../data/pet.txt", "w") as file:
                        file.writelines(pet_list)

                case 3:
                    # CASE 3: Remove an existing pet record
                    PetID = input("Enter pet ID you want to remove: ")

                    # Read all pet records
                    with open("../data/pet.txt", "r") as file:
                        pet_list = file.readlines()

                    found = False
                    index = 0  # Counter for line index

                    for line in pet_list:
                        pet_data = manual_strip(line)
                        pet_data = manual_spilt(pet_data, ",")
                        if pet_data[1] == PetID:
                            # Delete the line corresponding to the pet record
                            del pet_list[index]
                            found = True
                            break
                        index += 1

                    if found:
                        # Save updated pet records to file
                        with open("../data/pet.txt", "w") as file:
                            file.writelines(pet_list)
                        print("Pet record deleted successfully.")
                    else:
                        print("Pet ID not found.")

                case 4:
                    # CASE 4: Exit the pet record management menu
                    break

                case _:
                    # Handle invalid input outside 1-4
                    print("Enter a valid option")

        except ValueError:
            # Handle non-integer input
            print("Invalid choice. Please try again.")

        except Exception:
            # Catch-all for unexpected errors
            print("Unknown error occurred. Please try again.")

def sys_summary():

    # open pet.txt to count total pets
    with open("../data/pet.txt", "r") as file:
        count=0  # initialize counter

        for line in file:
            count=count+1  # increment counter for each line
        pet_amount=count  # store total pets

    # open booking.txt to count total bookings
    with open("../data/booking.txt", "r") as file:
        count=0  # reset counter

        for line in file:
            count=count+1  # increment counter for each line
            booking_amount=count  # store total bookings

    # open users.txt to count total users/pet owners
    with open("../data/users.txt", "r") as file:
        count=0  # reset counter

        for line in file:
            count=count+1  # increment counter for each line
            user_amount=count  # store total users

    # open slots.txt to count used slots and calculate available slots
    with open("../data/slots.txt", "r") as file:
        count=0  # reset counter

        for line in file:

            count=count+1  # increment counter for each line
            used_slot=count  # store used slots

            # determine available slots
            if used_slot<10:
                available_slot=10-used_slot  # calculate remaining slots
            elif used_slot==10:
                available_slot="full"  # no slots left
            else:
                available_slot="Error"  # inconsistency

        used_slot=count  # final used slot count

    # open service_history.txt to calculate total revenue
    with open("../data/service_history.txt", "r") as file:
        total=0  # initialize revenue total

        for line in file:
            data = manual_strip(line)  # remove whitespace/newlines
            data = manual_spilt(data, ",")  # split data by comma
            price=data[4]  # get price from field
            price=float(price)  # convert to float
            total=total+price  # accumulate total revenue

    # print system summary report
    print(f"""
    ============================
    Service System Report
    ============================

    Total Pet Owners/Users: {user_amount}
    Total Pets Registered: {pet_amount}
    Total Bookings: {booking_amount}

    Total Revenue: RM {total}
    -----------
    Slot info
    -----------
    Max slot=10
    Taken slot={used_slot}
    Available slot: {available_slot} 
    """)

def show_sys_admin_menu():

    while True:
        # print main admin menu options
        print("""
    ===========================
    System admin menu
    ===========================
    What would you like to do?
    1. View All Data
    2. Manage Pet Records and Service options
    3. Generate overall service report
    4. Exit
        """)

        try:
            option = int(input("Your choice: "))  # get user's menu choice
            match option:

                case 1:
                    sys_viewdata()  # call function to view all data
                case 2:
                    sys_manage()  # call function to manage pets/services

                case 3:
                    sys_summary()  # call function to generate system report

                case 4:
                    break  # exit the menu loop

                case _:
                    print("Enter a valid option")  # invalid menu option

        except ValueError:
            print("Invalid choice. Please try again.")  # handle non-integer input

        except Exception:
            print("Unknown error occured. Please try again.")  # handle unexpected errors
show_sys_admin_menu()