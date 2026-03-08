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
        print("Cannot read file")


def request_Booking():
    name = input("Please enter your name:")
    pet_id = input("Please enter your pet_id:")
    date = input("Enter date to book (DD-MM-YYYY):")

    booking_id = generate_booking_id()
    record = booking_id + "," name + "," + date + "," + pet_id + "," + "Pending"

    try:
        with open("booking.txt", "as") as f:
            f.write(record)
            print("Booking record submitted")
    except Exception as e:
        print("Cannot submit booking")

def request_Extension():
    name = input("Please enter your name:")
    pet_id = input("Please enter your pet_id:")
    booking_id = input("Please enter your Booking ID:")








