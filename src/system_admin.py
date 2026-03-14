# All features for system administrator here
# - Manage pet records and service options (add, update, remove).
# - View all data (owners, pets, bookings, payments).
# - Generate overall service report (total bookings, revenue, available slots).
def sys_viewdata():
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
              option = int(input("Your choice: "))
              if 0<option<6:
                    match option:
                        case 1:
                            with open("../data/users.txt", "r") as file:
                                credential_list = file.readlines()
                                for line in credential_list:
                                    credentials = line.strip().split(",")
                                    print(credentials[0])
                        case 2:
                            with open("../data/service_history.txt", "r") as file:
                                pet_list = file.readlines()
                                for line in pet_list:
                                    pet_list = line.strip().split(",")
                                    print("Pet ID-",pet_list[0],end="\n")
                                    print("Username-",pet_list[1],end="\n")
                                    print("Date-",pet_list[2],end="\n")
                                    print("Booking status-",pet_list[3],end="\n\n")
                        case 3:
                            with open("../data/booking.txt", "r") as file:
                                booking_list = file.readlines()
                                for line in booking_list:
                                    booking_list = line.strip().split(",")
                                    print("Booking ID-",booking_list[0],end="\n")
                                    print("Username-",booking_list[1],end="\n")
                                    print("Date-",booking_list[2],end="\n")
                                    print("PetID",booking_list[3],end="\n\n")
                        case 4:
                            print("payments")
                        case 5:
                            print("Exiting program")
                            break
              else:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")


def sys_manage():
    print("smth")

def sys_summery():
    print("smth")

def show_sys_admin_menu():
    while True:
        print("""
    ===========================
    System admin menu
    ===========================
    What would you like to do?
    1. View All Data
    2. Manage Pet and Service Records
    3. Generate overall service report
    4. Exit
        """)
        try:
            option = int(input("Your choice: "))
            match option:
                case 1:
                    sys_viewdata()
                case 2:
                    print("nothing yet")
                    break
                case 3:
                    print("nothing yet")
                    break
                case 4:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")
