# All features for system administrator here
# - Manage pet records and service options (add, update, remove).
# - View all data (owners, pets, bookings, payments).
# - Generate overall service report (total bookings, revenue, available slots).
from src.booking_officer import automatic_pet_id


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
                                    print("User/pet owner-",credentials[0],end="\n")
                                    print("User\'s password-",credentials[1],end="\n")
                                    with open("../data/pet.txt", "r") as file:
                                        pet_list=file.readlines()
                                        not_found = True
                                        for line in pet_list:
                                            pet_data=line.strip().split(",")
                                            if pet_data[0]==credentials[0]:
                                                print("Pet-",pet_data[2], "(",pet_data[1],")",end="\n\n1")
                                                not_found=False
                                    if not_found==True:
                                        print("No pet found for this user data\n")

                        case 2:
                            with open("../data/pet.txt", "r") as file:
                                pet_list = file.readlines()
                                for line in pet_list:
                                    pet_list = line.strip().split(",")
                                    print("Pet_Id-",pet_list[1],end="\n")
                                    print("Pet-",pet_list[2],end="\n")
                                    print("Pet Owner-",pet_list[0],end="\n\n")
                        case 3:
                            with open("../data/booking.txt", "r") as file:
                                booking_list = file.readlines()
                                for line in booking_list:
                                    booking_list = line.strip().split(",")
                                    print("Booking ID-",booking_list[0],end="\n")
                                    print("Username-",booking_list[1],end="\n")
                                    print("Date-",booking_list[2],end="\n\n")
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
    while True:
        print("""
    ===========================
    Manage
    ===========================
    What do would u like to manage?
    1.Service options
    2.Pet records
    3.Exit
    """)
        try:
            option = int(input("Your choice: "))
            match option:
                case 1:
                    sys_service_option1()
                case 2:
                    sys_manage()
                case 3:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")

def sys_service_option1():
    while True:
        print("""
    ===========================
    Manage
    ===========================
    What do would u like to do?
    1.Add
    2.Update
    3.Remove
    4.Exit
    """)
        try:
            option = int(input("Your choice: "))
            match option:
                case 1:
                    while True:
                        no_found=True
                        service=input("Enter service name: ")
                        with open("../data/Service.txt", "r") as file:
                            service_list=file.readlines()
                            for line in service_list:
                                service_data = line.strip().split(",")
                                if service==service_data[0]:
                                    print("Service already exists")
                                    no_found= False
                                    break
                        if no_found== True:
                            break
                    while True:
                        try:
                            payment=int(input("Enter payment number: "))
                        except ValueError:
                            print("Enter valid price")
                        else:
                            break
                    with open("../data/Service.txt", "a+") as file:
                        file.write(f"{service},{payment}")
                    print("Added")
                case 2:
                    service=input("Enter service to update: ")
                    with open("../data/Service.txt", "r") as file:
                        Service_list = file.readlines()
                    found = False
                    index = 0  # manual counter
                    for line in Service_list:
                        service_data = line.strip().split(",")
                        if service_data[0] == service:
                            found = True
                            print("Current data:", service_data)
                            field = input("Which field to update? (service name/price): ").lower()
                            if field == "service name":
                                service_data[0] = input("Enter Service option ")
                                print("service Name updated successfully.")
                            elif field == "price":
                                while True:
                                    try:
                                        payment = int(input("Enter price: "))
                                    except ValueError:
                                        print("Enter valid price")
                                    else:
                                        break
                                service_data[1] = payment
                                print("Service price updated successfully.")
                            else:
                                print("Invalid field.")
                            Service_list[index] = ",".join(service_data) + "\n"
                            break
                        index += 1
                        if not found:
                            print("Service name not found.")
                        with open("../data/Service.txt", "w") as file:
                            file.writelines(Service_list)
                case 3:
                    service = input("Enter the service you want to remove: ")
                    with open("../data/Service.txt", "r") as file:
                        service_list = file.readlines()
                    found = False
                    index = 0
                    for line in service_list:
                        service_data = line.strip().split(",")
                        if service_data[0] == service:
                            del service_list[index]
                            found = True
                            break
                        index += 1
                    if found:
                        with open("../data/Service.txt", "w") as file:
                            file.writelines(service_list)
                        print("Service deleted successfully.")
                    else:
                        print("Service not found.")
                case 4:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")

def sys_service_option2():
    while True:
        print("""
    ===========================
    Manage
    ===========================
    What do would u like to do?
    1.Add
    2.Update
    3.Remove
    4.Exit
    """)
        try:
            option = int(input("Your choice: "))
            match option:
                case 1:


                    pet=input("Enter pet name: ")
                    pet_ID=automatic_pet_id()
                    with open("../data/Service.txt", "a+") as file:
                        file.write(f"{username},{pet_ID},{pet},{password}")
                    print("Added")
                case 2:
                    service=input("Enter service to update: ")
                    with open("../data/Service.txt", "r") as file:
                        Service_list = file.readlines()
                    found = False
                    index = 0  # manual counter
                    for line in Service_list:
                        service_data = line.strip().split(",")
                        if service_data[0] == service:
                            found = True
                            print("Current data:", service_data)
                            field = input("Which field to update? (service name/price): ").lower()
                            if field == "service name":
                                service_data[0] = input("Enter Service option ")
                                print("service Name updated successfully.")
                            elif field == "price":
                                while True:
                                    try:
                                        payment = int(input("Enter price: "))
                                    except ValueError:
                                        print("Enter valid price")
                                    else:
                                        break
                                service_data[1] = payment
                                print("Service price updated successfully.")
                            else:
                                print("Invalid field.")
                            Service_list[index] = ",".join(service_data) + "\n"
                            break
                        index += 1
                        if not found:
                            print("Service name not found.")
                        with open("../data/Service.txt", "w") as file:
                            file.writelines(Service_list)
                case 3:
                    service = input("Enter the service you want to remove: ")
                    with open("../data/Service.txt", "r") as file:
                        service_list = file.readlines()
                    found = False
                    index = 0
                    for line in service_list:
                        service_data = line.strip().split(",")
                        if service_data[0] == service:
                            del service_list[index]
                            found = True
                            break
                        index += 1
                    if found:
                        with open("../data/Service.txt", "w") as file:
                            file.writelines(service_list)
                        print("Service deleted successfully.")
                    else:
                        print("Service not found.")
                case 4:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")




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
    2. Manage Pet Records and Service options
    3. Generate overall service report
    4. Exit
        """)
        try:
            option = int(input("Your choice: "))
            match option:
                case 1:
                    sys_viewdata()
                case 2:
                    sys_manage()
                    break
                case 3:
                    sys_summery()
                    break
                case 4:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")
show_sys_admin_menu()