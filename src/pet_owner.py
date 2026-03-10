# All functions for pet owner will be here
# - View available daycare or grooming slots.
# - Request bookings or extensions.
# - View pet service history and invoices.

#Function to display the available slots
def grooming_slots():
    #try except is used to catch errors
    try:
        #open the file "slots.txt" in read mode
        with open('slots.txt', 'r') as f:
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
                #split the line using space as a seperator
                parts = text.split(" ")

                #storeing the variable service into index no 0
                service = parts[0]
                #storing the variable name into index no 1
                name = parts[1]
                #storing the variable slots into index no 1
                slots = parts[2]

                #print the information
                print(f"This is the service id : {service}")
                print(f"This is the service name : {name}")
                print(f"This is the available slots : {slots}")

    #in case of error happening, this will prevent it from crashing
    except Exception as e:
        print("Cannot read file", e)

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
    while len(num) < 10:
        num = "0" + num

    booking_id = "BK" + num
    return booking_id

def request_Booking():
    name = input("Please enter your name:")
    pet_id = input("Please enter your pet_id:")
    date = input("Enter date to book (DD-MM-YYYY):")

    booking_id = automatic_booking_id()
    print("Your Booking ID is:", booking_id)
    try:
        with open("booking.txt", "a") as f:
            text = booking_id + "," + name + "," + date + "," + pet_id + "\n"
            f.write(text)
            print ("Booking request successful")
    except Exception as e:
        print("Booking request failed", e)

def request_extension():
    booking_id = input("Please enter your Booking ID:")
    extension_time = input("Please enter your extension time:")

    extension_id = input("Please enter your extension id:")
    try:
        with open("extension.txt", "a")as f:
            text = extension_id + "," + booking_id + "," + extension_time + "\n"
            f.write(text)
            print("Extension request successful")

    except Exception as e:
        print("Extension request failed", e)

def cancel_booking():
    booking_id = input("Please enter your Booking ID to cancel:")

    try:
        with open("booking.txt", "r") as f:
            new_text = ""
            line = f.readline()
            while line != "":
                if booking_id not in line:
                    new_text += line

                line = f.readline()
            with open("booking.txt", "w") as f:
                f.write(new_text)
                print("Booking cancelled successfully")
    except Exception as e:
        print("Booking cancelled failed", e)

def view_service_history():
    pet_id = input("Please enter your pet_id:")
    try:
        with open("service_history.txt", "r") as f:
            line = f.readline()
            print("Service History")
            while line != "":
                if pet_id in line:
                    print(line)
                line = f.readline()
    except Exception as e:
        print("Service file not found", e)






