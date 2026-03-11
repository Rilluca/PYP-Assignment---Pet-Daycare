# All functions for pet owner will be here
# - View available daycare or grooming slots.
# - Request bookings or extensions.
# - View pet service history and invoices.

#Function to display the available slots
def grooming_slots():
    #try except is used to catch errors
    try:
        #open the file "slots.txt" in read mode
        with open('../data/slots.txt', 'r') as f:
        #with statement automatically closes the file unlike file
            print("Available slots")
            #looping through the file one by one
            for line in f:
                #create an empty string to store the line
                text = ""
                #looping through each character in line
                for c in line:
                    #if character is not in new line, add it to the empty string
                    if c!= "\n":
                        text += c
                #split the line using comma as a seperator
                parts = text.split(",")

                #storeing the variable service into index no 0
                service = parts[0]
                #storing the variable name into index no 1
                name = parts[1]
                #storing the variable slots into index no 1
                slots = parts[2]

                #print the information
                print(f"Service id : {service}")
                print(f"Service name : {name}")
                print(f"Available slots : {slots}")

    #in case of error happening, this will prevent it from crashing
    except Exception as e:
        print("Cannot read file", e)

def existing_books(booking_id):
    try:
        with open('booking.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == booking_id:
                    return True
    except:
        pass

    return False

def automatic_booking_id():
    try:
        with open('../data/booking.txt', 'r') as f:
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

def request_Booking():
    name = input("Please enter your name:")
    pet_id = input("Please enter your pet_id:")
    date = input("Enter date to book (DD-MM-YYYY):")

    if name == "" or pet_id == "" or date == "":
        print("Every field must be filled")
        return

    booking_id = automatic_booking_id()
    print("Your Booking ID is:", booking_id)
    try:
        with open("../data/booking.txt", "a") as f:
            text = booking_id + "," + name + "," + date + "," + pet_id + "\n"
            f.write(text)
            print ("Booking request successful")
    except Exception as e:
        print("Booking request failed", e)

def automatic_request_extension():
    try:
        with open('../data/extension.txt', 'r') as f:
            count = 0
            line = f.readline()

            while line != "":
                count += 1
                line = f.readline()
    except:
        count = 0
        num = str(count + 1)
        while len(num) < 4:
            num = "0" + num

        extension_id = "E" + num
        return extension_id

def request_extension():
    booking_id = input("Please enter your Booking ID:")
    extension_time = input("Please enter your extension time:")

    if booking_id == "" or extension_time == "":
        print("Error: All fields must be filled.")
        return
    if not existing_books(booking_id):
        print("Booking ID does not exist")
        return

    extension_id = automatic_request_extension()
    print ("Your extension ID is:", extension_id)
    try:
        with open("../data/extension.txt", "a")as f:
            text = extension_id + "," + booking_id + "," + extension_time + "\n"
            f.write(text)
            print("Extension request successful")

    except Exception as e:
        print("Extension request failed", e)

def cancel_booking():
    booking_id = input("Please enter your Booking ID to cancel:")

    if not existing_books(booking_id):
        print("Booking ID does not exist")
        return

    try:
        with open("../data/booking.txt", "r") as f:
            new_text = ""
            line = f.readline()
            while line != "":
                if booking_id not in line:
                    new_text += line

                line = f.readline()
            with open("../data/booking.txt", "w") as f:
                f.write(new_text)
                print("Booking cancelled successfully")
    except Exception as e:
        print("Booking cancelled failed", e)

def reschedule_booking():
    booking_id =input("Please enter your Booking ID to reschedule:")
    new_date = input("Please enter your new date (DD-MM-YYYY):")

    if not existing_books(booking_id):
        print("Booking ID does not exist")
        return

    Result = False

    try:
        with open("../data/booking.txt", "r") as f:
            updated_booking = ""
            line = f.readline()
            Result = False
            while line != "":
                parts = line.strip().split(",")
                if parts[0] == booking_id:
                    parts[2] = new_date
                    Result = True
                    line = ",".join(parts) + "\n"
                updated_booking += line
                line = f.readline()
        with open("../data/booking.txt", "w") as f:
            f.write(updated_booking)
        if Result == True:
            print("Booking rescheduled successfully")
        else:
            print("Booking rescheduled failed")
    except Exception as e:
        print("Error: Rescheduling failed!")

def view_service_history():
        pet_id = input("Please enter your pet_id: ").strip()
        Result = False

        try:
            with open("../data/service_history.txt", "r") as f:
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

def continue_or_exit():
    choice = input("Do you want to continue (y/n)?").lower()

    if choice == "y":
        return True
    else:
        print("Exiting....")
        exit()

def pet_owner_menu():
    menu = True
    while menu:
        print("\n" + "="*20)
        print("  PET OWNER MENU")
        print("="*20)
        print("1. View Grooming Slots")
        print("2. Book a Service")
        print("3. Request an extension")
        print("4. Reschedule Booking")
        print("5. Cancel a Booking")
        print("6. View Service History")
        print("7. Return to Main Menu")

        choice = input("Enter choice: ")

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
        else:
            print("Invalid choice")
            break

        menu = continue_or_exit()







