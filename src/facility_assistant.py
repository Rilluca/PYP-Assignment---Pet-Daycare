import datetime

def add_facility():
    area=input("Enter are to prepare (Play Area/ Grooming Station )")
    status=input("Enter preparation Status (Ready / Cleaning Required )")

    file=open("../data/maintenance.txt", "a")
    file.write(f"{area},{status},{datetime.datetime.now()}\n")
    print("Facility status added ")
    file.close()

def add_alert():
    pet_id=input("Enter Pet ID : ")
    alert=input("Enter special care / medical alert : ")

    file=open("../data/pet.txt","a")
    file.write(f"{pet_id},ALERT, {alert}\n")
    print("Alert added successfully")


def check_overdue():
    now=datetime.datetime.now()

    try:
        file=open("../data/booking.txt","r")
        bookings=file.readlines()

        print("\nChecking for overdue \n")
        for booking in bookings:
            data=booking.strip().split(",")

            if(len(data)<4):
                continue
            pet_id=data[0]
            owner=data[1]
            pickup_time=data[3]

            pickup_datetime=datetime.datetime.strptime(
                pickup_time, "%d-%m-%y")
        file.close()
    except FileNotFoundError:
        print("No Bookings Found")


def main_menu():
    while True:
        print("1. Prepare daycare / Play area")
        print("2. Add Special / medical alert ")
        print("3. Check overdue pickups ")
        print("4. Exit Program ")

        choice =input("Enter your choice ")
        if(choice=="1"):
            add_facility()
        elif(choice=="2"):
            add_alert()
        elif(choice=="3"):
            check_overdue()
        elif(choice=="4"):
            print("Exiting Facility Assistant ")
            break
        else:
            print("Invalid Choice ")