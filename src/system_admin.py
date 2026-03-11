# All features for system administrator here
# - Manage pet records and service options (add, update, remove).
# - View all data (owners, pets, bookings, payments).
# - Generate overall service report (total bookings, revenue, available slots).
from idlelib.autocomplete import TRY_A

def sys_viewdata():
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
    while True:
        try:
              option = int(input("Your choice: "))
              if 0<option<6:
                    match option:
                        case 1:
                            with open("users.txt", "r") as file:
                                credential_list = file.readlines()
                                for line in credential_list:
                                    credentials = line.strip().split(",")
                                    print(credentials[0])
                        case 2:
                            print("pets")
                        case 3:
                            print("bookings")
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
    print("""
    ===========================
    System admin menu
    ===========================
    What would you like to do?
    1. View All Data
    2. Manage Pet and Service Records
    3. Generate overall service report
    """)
    while True:
        try:
              option = int(input("Your choice: "))
              if option == 1:
                  break
              if option == 2:
                  break
              if option == 3:
                  break
              print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")
    match option:
        case 1:
            sys_viewdata()
        case 2:
            sys_manage()
        case 3:
            sys_summery()
show_sys_admin_menu()