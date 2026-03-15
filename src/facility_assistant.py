import datetime


# -------- 1. Prepare daycare / grooming --------
def add_facility():

    area = input("Enter area (Play Area / Grooming Station): ")
    status = input("Enter status (Ready / Cleaning Required): ")

    file = open("../data/maintenance.txt", "a")
    file.write(f"{area},{status},{datetime.datetime.now()}\n")
    file.close()

    print("Facility status saved")


# -------- 2. Add special / medical alert --------
def add_alert():

    pet_id = input("Enter Pet ID: ")
    alert = input("Enter medical / special alert: ")

    file = open("../data/pet_alert.txt", "a")
    file.write(f"{pet_id},ALERT,{alert}\n")
    file.close()

    print("Alert added")


# -------- 3. Notify overdue pickups / special request --------
def check_overdue():

    today = datetime.date.today()

    try:
        file = open("../data/booking.txt", "r")
        bookings = file.readlines()

        if len(bookings) == 0:
            print("No bookings found")
            return

        print("\nChecking bookings...\n")

        for booking in bookings:

            data = booking.strip().split(",")

            # expected format
            # BK0001,Crush,24-02-2008,123

            if len(data) < 4:
                continue

            booking_id = data[0]
            pet_name = data[1]
            date_str = data[2]
            special = data[3]

            pickup_date = datetime.datetime.strptime(
                date_str,
                "%d-%m-%Y"
            ).date()

            # ✅ overdue condition
            if pickup_date < today:
                print("Overdue pickup!")
                print("Booking:", booking_id)
                print("Pet:", pet_name)
                print("Date:", date_str)

            # ✅ special request condition
            if special != "":
                print("Special request:", special)

            print("--------------------")

        file.close()

    except FileNotFoundError:
        print("No bookings found")


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
