# All functions for pet owner will be here
# - View available daycare or grooming slots.
# - Request bookings or extensions.
# - View pet service history and invoices.

#define a function to variable if a string contains only letters and spaces, and is not empty
def check_alphabet_and_empty_string_or_purely_spaces(x):
    #initialize as true
    is_alphabet = True
    #initialize a counter for total characters
    count = 0
    #initialize a counter for space characters
    s_count = 0
    #Loop through every character in the input string
    for c in x:
        # Check if the character is not a lowercase letter, uppercase letter, or a space
        if not ((c >= "a" and c <= "z" ) or (c >= "A" and c <= "Z") or c==" "):
            #set flag to false
            is_alphabet = False
        #check if a character is a space
        if c==" ":
            #increament the space by 1
            s_count=s_count+1
        #increament the total character by 1
        count=count+1
    # If the string is entirely spaces or has a length of zero
    if s_count==count or count==0:
            #set flag to false
            is_alphabet = False
    #return the result
    return is_alphabet

#define a function to convert an integer to a character based on a custom function
def custom_chr(x):
    #representing ASCII from idnex 332 to 126
    lookup = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    #if the input num is within the valid range
    if 32 <= x <= 126:
        #return the character
        return lookup[x- 32]
    #return an empty string if out of range
    return ""

#define  a function to find the ASCII index of a character
def custom_ord(x):
    #the same as in custom_chr
    lookup = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    #set index at 0
    index = 0
    #loop through every character in the lookup string
    for c in lookup:
        #if the character matches the input
        if c == x:
            #return the index plus the offset of 32
            return index + 32
        #move to the next index
        index += 1
    #return -1 if the character is not found
    return -1

#define a functon to convert a string to lowercase
def custom_lower(x):
    #initialize the empty string
    total = ""
    #loop through each character in the input string
    for c in x:
        #numeric value
        c = custom_ord(c)
        #checks if A-Z
        if 64 < c < 91:
            #add 32 to shift it o lowercase range
            c = c + 32
        #convert the numeric value back to a character
        c = custom_chr(c)
        #append the character to the result string
        total = total + c
    return total

#define a function to count the length of an item
def count_len(item):
    #set the initial counter to 0
    count = 0
    #loops through every element in the item
    for _ in item:
        #increases the counter by 1
        count += 1
    return count

#define a function to split the string into a list
def custom_split(x, y):
    #initialize an empty string
    result = []
    #initialize an empty string to build words
    current_word = ""
    #loop through every character
    for char in x:
        #if the character matches the delimiter (like a comma)
        if char == y:
            #add the built word
            result = result + [current_word]
            #reset
            current_word = ""
        else:
            #add the character to the current word builder
            current_word += char
    #add the last word remaining
    result = result + [current_word]
    return result

#define a function to remove newline and carriage return characters
def custom_strip(y):
    # initialize an empty string
    z = ""
    #loop through every character in the input
    for char in y:
        #if the character is not a newline or a carriage return
        if char != "\n" and char != "\r" and char != " ":
            #add it to the result
            z += char
    return z

#Function to display the available slots
def grooming_slots():
    #asks the user to enter a date
    date = input("Please enter your date (DD-MM-YYYY):")
    #check whether the date format is valid or not
    if not validate_date(date):
        print("Invalid date format or values. Only DD-MM-YYYY")
        return
    #max num of available slots per day
    max_slots = 10
    #variable to count how many bookings exists for a day
    booked_slots = 0
    #try except is used to catch errors
    try:
        #open the file in read mode
        with open('../data/booking.txt', 'r') as f:
        #with statement automatically closes the file unlike file
            #looping through the file one by one
            for line in f:
                #remove hidden newline characters
                clean_line = custom_strip(line)
                #split the line by commas
                parts = custom_split(clean_line, ",")
                #check if the line fits the length and same date
                if count_len(parts) >=4 and parts[3] == date:
                    #increase booked_slots by 1
                    booked_slots += 1
    #if the file doesn't exist
    except FileNotFoundError:
        #display this
        print("Booking file not found")


    #calculate the variable available slots
    available_slots = max_slots - booked_slots
    #used to prevent negative values
    if available_slots < 0:
         available_slots = 0

    #display the information
    print("Date:", date)
    print("Maximum slots:", max_slots)
    print("Booked slots:", booked_slots)
    print("Available slots:", available_slots)


#function to check if  a booking ID already exists
def existing_books(booking_id):
    #try block to safely read the booking file
    try:
        #open the file in read mode
        with open('../data/booking.txt', 'r') as f:
            #loop through every line in the file
            for line in f:
                #remove new line and split the line by comma
                parts = custom_split(custom_strip(line), ",")
                if parts[0] == booking_id:
                    #check if booking id matches index 0
                    return True
    except FileNotFoundError:
        #if errors happen, ignore
        pass
    #return false if booking id was not found
    return False

#Function to automatically generate booking
def automatic_booking_id():
    try:
        #open the fle in read mode
        with open('../data/booking.txt', 'r') as f:
            #counter set to 0
            count = 0
            #read the first line
            line = f.readline()
            #while line is not empty, increase counter by 1
            while line != "":
                count += 1
                #read the next line
                line = f.readline()
    #if file does not exist
    except FileNotFoundError:
        #start count at 0
        count = 0
    #convert the next booking num to str
    num = str(count + 1)
    #while length of num is less than 4
    while count_len(num) < 4:
        #add 0 in front of the number
        num = "0" + num
    #comebine prefix with num
    booking_id = "BK" + num
    #return the generated booking ID
    return booking_id

#function to validate date format
def validate_date(date_str):
    #check the length  and dash positions of the fate
    if count_len(date_str) != 10 or date_str[2] != "-" or date_str[5] != "-":
        return False

    #extract day, month , and year
    day, month, year = date_str[:2], date_str[3:5], date_str[6:]
    #check if all parts are digits
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    #convert day and month to int
    day, month = int(day), int(month)
    #validate the range of day and month
    if not (1 <= day <= 31) or not (1 <= month <= 12):
        return False
    #return True if its valid
    return True

#function to display available services and choose them
def choose_service():
    #intilialize empty services list
    services = []

    # read services from file
    try:
        #open the file in read mode
        with open('../data/Service.txt', 'r') as f:
            #loop through each line
            for line in f:
                #clean the line
                clean_line = custom_strip(line)
                #split name and price
                parts = custom_split(clean_line, ",")
                #check if valid records
                if count_len(parts) >= 2:
                    #add to service list
                    services = services + [parts]
    #if file not found error occurs
    except FileNotFoundError:
        #notify userr
        print("Service file not found")
        #return none if file missing
        return None

    # Display header for the output
    print("\nAvailable Services:")
    #initialize counter
    i = 1
    #loop through services
    for service in services:
        #dsiplay service
        print(f"{i}. {service[0]} - RM {service[1]}")
        #increament by 1
        i += 1

    #Loop until valid choice
    while True:
        try:
            #asks the user to enter their choice
            choice = int(input("Please enter your choice: "))
            #validate choice
            if 1 <= choice <= count_len(services):
                #get a selected service
                selected = services[choice - 1]
                #display the output
                print(f"You chose: {selected[0]} - RM {selected[1]}")
                return selected
            else:
                print("Invalid choice")
        #non-int error
        except ValueError:
            print("Enter a valid number")

#function to request a booking
def request_Booking():
    #asks user for the following information
    name = input("Please enter your name:")

    #validate booking name by calling the function
    if not check_alphabet_and_empty_string_or_purely_spaces(name):
        print("Invalid name")
        #if not valid, return
        return

    #ask user to input their information
    pet_id = input("Please enter your pet_id:")
    date = input("Enter date to book (DD-MM-YYYY): ")

    #validate date format
    if not validate_date(date):
        print("Invalid date format or values. Only DD-MM-YYYY")
        return

    #display the seperator lines for visual
    print("-"*20)
    #check to see if any of the field is empty
    if name == "" or pet_id == "" or date == "":
        print("Every field must be filled")
        return

    #call choos service
    service = choose_service()
    #check if service is selected
    if not service:
        #stop if no
        return
    #index number for each variables
    service_name, service_fee = service[0], service[1]

    #asks the user to input whether they want to pay or no
    payment = input(f"Do you agree to pay Rm {service_fee}? (accept/decline): ")
    #normalize payment input to lower case
    payment = custom_lower(payment)

    #if accepts
    if payment == "accept":
        #display this
        print("Payment made")
    #if does not accept
    elif payment == "decline":
        #display this and end
        print ("Payment declined")
        return
    else:
        print("Invalid Output")
        return

    try:
        #open the file in read mode to check duplicate
        with open("../data/booking.txt", "r") as f:
            #loop through each booking
            for line in f:
                #split line data and seperate by comma
                parts = custom_split(custom_strip(line), ",")
                #check if same pet is already booked on th same date
                if count_len(parts) >=4 and parts[3] == date and parts[2] == pet_id:
                    #if so, display this
                    print(f"Booking already exists for {pet_id} on {date}")
                    return

    except FileNotFoundError:
        pass
    #automaticallly generate a  new booking ID
    booking_id = automatic_booking_id()

    try:
        #open booking file in append mode
        with open("../data/booking.txt", "a") as f:
            #create booking record text
            text = f"{booking_id},{name},{pet_id},{date},{service_name},{service_fee},{payment}\n"
            #write the text in the file
            f.write(text)
        #open service history file in append mode
        with open("../data/service_history.txt", "a")as f:
            #create service history record text
            text = f"{pet_id},{name},{date},{service_name},{service_fee},{payment},Booked\n"
            #write the text in the file
            f.write(text)

            #display the information if successful
            print("\n" + "="*30)
            print("       Booking Confirmation")
            print(f"Booking ID      : {booking_id} ")
            print(f"Owner Name      : {name} ")
            print(f"Pet ID          : {pet_id} ")
            print(f"Booking Date    : {date} ")
            print(f"Service Name    : {service_name} ")
            print(f"Service Fee     : RM {service_fee} ")
            print(f"Payment status  : {payment} ")
            print("="*30 + "\n")
            print ("Booking request successful")

    #catch unexpected errors
    except Exception as e:
        print("Booking request failed", e)

#function to automatically generate extension ID
def automatic_request_extension():
    try:
        #set the counter to 0
        count = 0
        #open the file in read mode
        with open('../data/extension.txt', 'r') as f:
            #read the first tine
            line = f.readline()
            #while line is not empty
            while line != "":
                #increase counter by 1
                count += 1
                #read the next line
                line = f.readline()
    #if the file does not exist
    except FileNotFoundError:
        #assumes counter starts at 0
        count = 0

    #convert next number to string
    num = str(count + 1)
    #add zero numbers at the start until length becomes greater or equal to 4
    while count_len(num) < 4:
        num = "0" + num
    #add E in front of extension id numerical number
    extension_id = "E" + num
    #return the number
    return extension_id

#function to request a booking extension date and id
def request_extension():
    #asks the user to enter a booking ID
    booking_id = input("Please enter your Booking ID:")
    #asks the user to enter an extension date
    extension_date = input("Please enter your extension date:")
    #if the date does not follow the format
    if not validate_date(extension_date):
        #display this
        print("Invalid date format. Use DD-MM-YYYY")
        return

    #check if any of the field is empty
    if booking_id == "" or extension_date == "":
        #if so, display this
        print("Error: All fields must be filled.")
        return

    #check to booking ID exists or no
    if not existing_books(booking_id):
        #if no display this
        print("Booking ID does not exist")
        return
    #autoamtically generate a new extension request ID
    extension_id = automatic_request_extension()
    #display the extension ID
    print ("Your extension ID is:", extension_id)
    try:
        #open the file in append mode
        with open("../data/extension.txt", "a")as f:
            #create extension request text
            text = extension_id + "," + booking_id + "," + extension_date + "\n"
            #write the text in the file
            f.write(text)
            #display the infromation if successful
            print("Extension request successful")

    #if unexpected errors occur
    except Exception as e:
        #dispaly this
        print("Extension request failed", e)

#function to cancel an existing booking
def cancel_booking():
    #asks the user to enter the booking ID
    booking_id = input("Please enter your Booking ID to cancel:")

    #checks if booking exists or no
    if not existing_books(booking_id):
        #if not, display this
        print("Booking ID does not exist")
        return

    try:
        #open the file in read mode
        with open("../data/booking.txt", "r") as f:
            #create a variable to store updated content
            new_text = ""
            #read the first line
            line = f.readline()
            #looping while the line is not empty
            while line != "":
                #spit the line and seperate by comma
                parts = custom_split(custom_strip(line), ",")
                #keeps lines that are not cancelled booking
                if parts[0] != booking_id:
                    new_text += line

                #read the next line
                line = f.readline()
            #opent the file in write mode
            with open("../data/booking.txt", "w") as f:
                #write the updated booking record in the file
                f.write(new_text)
                #display this
                print("Booking cancelled successfully")
    #if unexpected errorrs occur
    except Exception as e:
        #display this
        print("Booking cancelled failed", e)

#function to reschedule booking date
def reschedule_booking():
        #asks the user to enter their booking id
        booking_id = input("Enter your Booking ID to reschedule: ")
        #asks the user to enter a new date
        new_date = input("Enter new date (DD-MM-YYYY): ")

        #check if the booking exists or not
        if not existing_books(booking_id):
            #if not, dispaly this
            print("Booking ID does not exist")
            return

        #check if the date follows the right format or not
        if not validate_date(new_date):
            #if not display this
            print("Invalid date format. Use DD-MM-YYYY")
            return

        #variable to store an updated booking
        updated_booking = ""
        #track if update was successful
        success = False

        try:
            #open the file in read mode
            with open("../data/booking.txt", "r") as f:
                #looping through each booking
                for line in f:
                    #split booking data and seperate by comma
                    parts = custom_split(custom_strip(line), ",")
                    #check if the booking id matches the existing booking id
                    if parts[0] == booking_id:
                        #update the booking date
                        parts[3] = new_date
                        #if all these, mark succes
                        success = True
                    #rebuild booking records
                    updated_booking += ",".join(parts) + "\n"

            #open the file in write mode
            with open("../data/booking.txt", "w") as f:
                #write the updated booking in the file
                f.write(updated_booking)
            #if everything is successful
            if success:
                #display this
                print("Booking rescheduled successfully!")
            else:
                #if not, display this
                print("Failed to reschedule booking.")

        #if unexpected errors occur
        except Exception as e:
            #diplay this
            print("Error: Rescheduling failed:", e)

#function to view user service history
def view_service_history():
        #asks the user to input their name
        name = input("Please enter your name: ")
        if not check_alphabet_and_empty_string_or_purely_spaces(name):
            print("Invalid name")
            return
        name = custom_lower(name)

        #flag to check if the record exists
        Result = False

        try:
            #open the file in read mode
            with open("../data/service_history.txt", "r") as f:
                #display the header
                print(f"\n--- Service History for {name} ---")
                #loop through the file records
                for line in f:
                    #split record data and seperate by comma
                    clean_line = custom_strip(line)
                    parts = custom_split(clean_line, ",")
                    #check if the name matches
                    if count_len(parts) >= 5:
                        #get owner name from file in lowercase
                        owner_name = custom_lower(parts[1])
                        #if name matches
                        if owner_name == name:
                            # Assing local variables to the matched index for readability
                            pet_id = parts[0]
                            owner = parts[1]
                            date = parts[2]
                            service = parts[3]
                            fee = parts[4]
                            payment = parts[5]
                            status = parts[6] if count_len(parts) > 6 else 'Booked'


                        #display service history
                            print(f"Pet ID: {pet_id} | Owner Name: {owner} | Service Date: {date} |"
                                 f"Service Name: {service} | Service Fee: RM {fee} | Payment Status : {payment} | Status: {status} ")
                        #record found flagged
                        Result = True
                #if no records are found
                if not Result:
                    #display this
                    print("No records found for this HOOMAN.")
        #if file cannot be found
        except FileNotFoundError:
            #display this
            print("File not found")


#funcion to ask users whether to contineu or back to the menu
def continue_or_exit():
    #infinite loop until valid input
    while True:
        #asks user to entera  choice
        choice = custom_lower(input("Do you want to continue (y/n)?"))
        #if user wants to continue, enter this
        if choice == "y":
            return True
        #if user wants to go exit, enter this
        elif choice == "n":
            print("Goodbye!")
            return False
        else:
            #if user enters anything else, display this
            print("Invalid choice")


#main pet owner menu function
def pet_owner_menu():
    #control variable
    menu = True
    #loop while the menu is active
    while menu:
        #display menu header
        print("\n" + "="*20)
        print("  PET OWNER MENU")
        print("="*20)
        #display the options
        print("1. View Grooming Slots")
        print("2. Book a Service")
        print("3. Request an extension")
        print("4. Reschedule Booking")
        print("5. Cancel a Booking")
        print("6. View Service History")

        #asks the user to enter a choice
        choice = input("Enter choice: ")

        #call functions based on the user choice
        if choice == '1':
            grooming_slots()
        elif choice == '2':
            request_Booking()
        elif choice == '3':
            request_extension()
        elif choice == '4':
            reschedule_booking()
        elif choice == '5':
            cancel_booking()
        elif choice == '6':
            view_service_history()
        #invalid option
        else:
            print("Invalid choice")
            break

        #asks user whether to continue or not
        menu = continue_or_exit()








