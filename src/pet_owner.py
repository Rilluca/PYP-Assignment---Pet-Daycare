# All functions for pet owner will be here
# - View available daycare or grooming slots.
# - Request bookings or extensions.
# - View pet service history and invoices.

#Custon function instead of len()
def count_len(item):
    #set the initial counter to 0
    count = 0
    #loops through every element in the item
    for _ in item:
        #increases the counter by 1
        count += 1
    return count

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
                #remove newline character and split it by commas
                parts = line.strip().split(",")
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
                parts = line.strip().split(",")
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
                #split lines by comma
                parts = line.strip().split(",")
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

    payment = input(f"Do you agree to pay Rm {service_fee}? (Paid/Not Paid): ").capitalize()
    if payment == "Paid":
        print("Payment made")
    elif payment == "Not Paid":
        print("Payment declined")
    else:
        print("Invalid Input")

    try:
        #open the file in read mode to check duplicate
        with open("../data/booking.txt", "r") as f:
            #loop through each booking
            for line in f:
                #split line data and seperate by comma
                parts = line.strip().split(",")
                #check if same pet is already booked on th same date
                if count_len(parts) >=4 and parts[2] == date and parts[3] == pet_id:
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
                #spit the line adn seperate by comma
                parts = line.strip().split(",")
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
                    parts = line.strip().split(",")
                    #check if the booking id matches the exisitng booking id
                    if parts[0] == booking_id:
                        #update the booking date
                        parts[2] = new_date
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
        name = input("Please enter your name: ").strip().lower()
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
                    parts = line.strip().split(",")
                    #check if the name matches
                    if count_len(parts) >= 4 and parts[1].strip().lower() == name:
                        #display service history
                        status = parts[5] if count_len(parts) > 5 else 'Booked'
                        print(f"Pet ID: {parts[0]} | Owner Name: {parts[1]} | Service Date: {parts[2]} |"
                              f"Service Name: {parts[3]} | Service Fee: RM {parts[4]} | Payment Status : {parts[5]} | Status: {status} ")
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
def continue_or_menu():
    #infinite loop until valid input
    while True:
        #asks user to entera  choice
        choice = input("Do you want to continue (y/n)?").lower()
        #if user wants to continue, enter this
        if choice == "y":
            return True
        #if user wants to go back to the menu, enter this
        elif choice == "n":
            pet_owner_menu()
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
        menu = continue_or_menu()








