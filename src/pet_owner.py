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
        with open('../data/booking.txt', 'r') as f:
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
    while len(num) < 4:
        num = "0" + num

    booking_id = "BK" + num
    return booking_id

def validate_date(date_str):
    if len(date_str) != 10 or date_str[2] != "-" or date_str[5] != "-":
        return False

    day, month, year = date_str[:2], date_str[3:5], date_str[6:]
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day, month = int(day), int(month)
    if not (1 <= day <= 31) or not (1 <= month <= 12):
        return False

    return True

def request_Booking():
    name = input("Please enter your name:")
    pet_id = input("Please enter your pet_id:")
    date = input("Enter date to book (DD-MM-YYYY): ")

    if not validate_date(date):
        print("Invalid date format or values. Only DD-MM-YYYY")
        return

    print("-"*20)
    if name == "" or pet_id == "" or date == "":
        print("Every field must be filled")
        return

    try:
        with open("../data/booking.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >=4 and parts[2] == date and parts[3] == pet_id:
                    print(f"Booking already exists for {pet_id} on {date}")
                    return

    except FileNotFoundError:
        pass

    booking_id = automatic_booking_id()

    try:
        with open("../data/booking.txt", "a") as f:
            text = booking_id + "," + name + "," + date + "," + pet_id + "\n"
            f.write(text)

        with open("../data/service_history.txt", "a")as f:
            text = pet_id + "," + name + "," + date + "," + "Booked\n"
            f.write(text)

            print("\n" + "="*30)
            print("       Booking Confirmation")
            print(f"Booking ID      : {booking_id} ")
            print(f"Owner Name      : {name} ")
            print(f"Pet ID          : {pet_id} ")
            print(f"Booking Date    : {date} ")
            print("="*30 + "\n")
            print ("Booking request successful")

    except Exception as e:
        print("Booking request failed", e)

def automatic_request_extension():
    try:
        count = 0
        with open('../data/extension.txt', 'r') as f:
            line = f.readline()
            while line != "":
                count += 1
                line = f.readline()

    except FileNotFoundError:
        count = 0

    num = str(count + 1)
    while len(num) < 4:
        num = "0" + num

    extension_id = "E" + num
    return extension_id

def request_extension():
    booking_id = input("Please enter your Booking ID:")
    extension_time = input("Please enter your extension time:")
    if not validate_date(extension_time):
        print("Invalid date format. Use DD-MM-YYYY")
        return

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
                parts = line.strip().split(",")
                if parts[0] != booking_id:
                    new_text += line

                line = f.readline()
            with open("../data/booking.txt", "w") as f:
                f.write(new_text)
                print("Booking cancelled successfully")
    except Exception as e:
        print("Booking cancelled failed", e)

def reschedule_booking():
        booking_id = input("Enter your Booking ID to reschedule: ").strip()
        new_date = input("Enter new date (DD-MM-YYYY): ").strip()

        if not existing_books(booking_id):
            print("Booking ID does not exist")
            return

        if len(new_date) != 10 or new_date[2] != "-" or new_date[5] != "-":
            print("Invalid date format. Use DD-MM-YYYY")
            return

        day, month, year = new_date[:2], new_date[3:5], new_date[6:]
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("Date must contain numbers")
            return
        day, month = int(day), int(month)
        if not (1 <= day <= 31) or not (1 <= month <= 12):
            print("Invalid day or month")
            return

        updated_booking = ""
        success = False

        try:
            with open("../data/booking.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if parts[0] == booking_id:
                        parts[2] = new_date
                        success = True
                    updated_booking += ",".join(parts) + "\n"

            with open("../data/booking.txt", "w") as f:
                f.write(updated_booking)

            if success:
                print("Booking rescheduled successfully!")
            else:
                print("Failed to reschedule booking.")

        except Exception as e:
            print("Error: Rescheduling failed:", e)
def view_service_history():
        name = input("Please enter your name: ").strip().lower()
        Result = False

        try:
            with open("../data/service_history.txt", "r") as f:
                print(f"\n--- Service History for {name} ---")
                for line in f:

                    parts = line.strip().split(",")

                    if len(parts) >= 4 and parts[1].strip().lower() == name:
                        print(f"Pet ID: {parts[0]} | Owner Name: {parts[1]} | Service Date: {parts[2]} | Status: {parts[3]}")
                        Result = True

                if not Result:
                    print("No records found for this HOOMAN.")

        except FileNotFoundError:
            print("File not found")

def continue_or_menu():
    while True:
        choice = input("Do you want to continue (y/n)?").lower()

        if choice == "y":
            return True
        elif choice == "n":
            pet_owner_menu()
            return False
        else:
            print("Invalid choice")


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

        menu = continue_or_menu()








