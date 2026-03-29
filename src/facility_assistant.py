import datetime


# -------- 1. Prepare daycare / grooming --------
def add_facility():

    while True:
        area = input("Enter area (Play Area / Grooming Station): ")
        status = input("Enter status (Ready / Cleaning Required): ")

        with open("../data/maintenance.txt", "a") as file:
            file.write(f"{area},{status},{datetime.datetime.now()}\n")

        print("Facility status saved")

        again = input("Add another facility? (yes / no): ")
        if again.lower() != "yes":
            break


# -------- 2. Add special / medical alert --------
def add_alert():

    while True:
        pet_id = input("Enter Pet ID: ")
        alert = input("Enter medical / special alert: ")

        with open("../data/pet_alert.txt", "a") as file:
            file.write(f"{pet_id},ALERT,{alert}\n")

        print("Alert added")

        again = input("Add another alert? (yes / no): ")
        if again.lower() != "yes":
            break


# -------- 3. Check overdue bookings --------
def check_overdue():

    today = datetime.date.today()

    try:
        with open("../data/booking.txt", "r") as file:
            bookings = file.readlines()

        if len(bookings) == 0:
            print("No bookings found")
            return

        print("\nChecking bookings...\n")

        for booking in bookings:

            data = booking.strip().split(",")

            # Expected format:
            # id,name,type,date,service,price,note

            if len(data) < 7:
                continue                          # FIX: silently skip invalid lines

            booking_id = data[0]
            pet_name = data[1]
            date_str = data[3]
            service = data[4]
            note = data[6]

            try:
                pickup_date = datetime.datetime.strptime(
                    date_str,
                    "%d-%m-%Y"
                ).date()
            except:
                print("Wrong date format:", date_str)
                continue

            if pickup_date < today:
                print("Overdue pickup!")
                print("Booking:", booking_id)
                print("Pet:", pet_name)
                print("Date:", date_str)

            if service != "":                     # FIX: moved outside overdue block
                print("Service:", service)

            if note != "":                        # FIX: moved outside overdue block
                print("Note:", note)

            print("--------------------")

    except FileNotFoundError:
        print("booking.txt file not found")


# -------- MENU --------
def main_menu():

    while True:

        print("\n1. Prepare daycare / play area")
        print("2. Add medical alert")
        print("3. Check overdue pickups / requests")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_facility()

        elif choice == "2":
            add_alert()

        elif choice == "3":
            check_overdue()

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice")


# -------- START PROGRAM --------
if __name__ == "__main__":
    main_menu()