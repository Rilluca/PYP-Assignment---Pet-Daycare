# All features for system administrator here
# - Manage pet records and service options (add, update, remove).
# - View all data (owners, pets, bookings, payments).
# - Generate overall service report (total bookings, revenue, available slots).
from src.booking_officer import automatic_pet_id
def check_alphabet(x):
    is_alphabet = True
    count = 0
    s_count = 0
    for c in x:
        if not ((c >= "a" and c <= "z" ) or (c >= "A" and c <= "Z") or c==" "):
            is_alphabet = False
        if c==" ":
            s_count=s_count+1
        count=count+1
    if s_count==count or count==0:
            is_alphabet = False
    return is_alphabet

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
                                                print("Pet-",pet_data[2], "(",pet_data[1],")",end="\n\n")
                                                not_found=False
                                    if not_found==True:
                                        print("No pet found for this user data\n")

                        case 2:
                            with open("../data/pet.txt", "r") as file:
                                pet_list = file.readlines()
                                for line in pet_list:
                                    pet_data = line.strip().split(",")
                                    print("Pet_Id-",pet_data[1],end="\n")
                                    print("Pet-",pet_data[2],end="\n")
                                    print("Pet Owner-",pet_data[0],end="\n\n")
                        case 3:
                            with open("../data/booking.txt", "r") as file:
                                booking_list = file.readlines()
                                for line in booking_list:
                                    booking_data = line.strip().split(",")
                                    print("Booking ID-",booking_data[0],end="\n")
                                    print("Username-",booking_data[1],end="\n")
                                    print("Date-",booking_data[2],end="\n\n")
                        case 4:
                            with open("../data/service_history.txt", "r") as file:
                                payment_list = file.readlines()
                                for line in payment_list:
                                    payment_data = line.strip().split(",")
                                    print("Username-",payment_data[1],end="\n")
                                    print("Date-",payment_data[2],end="\n")
                                    print("Status-",payment_data[5],end="\n")
                                    print("Payment- RM", payment_data[4],end="\n\n")

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
                    sys_service_option2()
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
                        while True:
                            service= input("Enter service name:")
                            check_alpha = check_alphabet(service)
                            if check_alpha == True:
                                break
                            else:
                                print("Enter a valid service(only alphabet)")
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
                            payment=int(input("Enter price of the service: "))
                        except ValueError:
                            print("Enter valid price")
                        else:
                            break
                    with open("../data/Service.txt", "a+") as file:
                        file.write(f"{service},{payment}\n")
                    print("Added")
                case 2:
                    service=input("Enter service to update: ")
                    with open("../data/Service.txt", "r") as file:
                        service_list = file.readlines()
                    found = False
                    index = 0  # manual counter
                    for line in service_list:
                        service_data = line.strip().split(",")
                        if service_data[0] == service:
                            found = True
                            print("Current data:", service_data)
                            field = input("Which field to update? (service name/price): ").lower()
                            if field == "service name":
                                while True:
                                    service = input("Enter service name:")
                                    check_alpha = check_alphabet(service)
                                    if check_alpha == True:
                                        break
                                    else:
                                        print("Enter a valid service(only alphabet)")
                                service_data[0] = service
                                print("Service Name updated successfully.")
                            elif field == "price":
                                while True:
                                    try:
                                        payment = int(input("Enter price: "))
                                        payment =str(payment)
                                    except ValueError:
                                        print("Enter valid price")
                                    else:
                                        break
                                service_data[1]= payment
                                print("Service price updated successfully.")
                            else:
                                print("Invalid field.")
                            service_list[index] = ",".join(service_data) + "\n"
                            break
                        index += 1
                    if not found:
                        print("Service name not found.")
                    with open("../data/Service.txt", "w") as file:
                        file.writelines(service_list)
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
                    while True:
                            username=input("Enter username:")
                            check_alpha=check_alphabet(username)
                            if check_alpha==True:
                                break
                            else:
                                print("Enter a valid name(only alphabet)")
                    while True:
                            pet=input("Enter pet name: ")
                            check_alpha=check_alphabet(pet)
                            if check_alpha==True:
                                break
                            else:
                                print("A pet name can only contain alphabets")
                    pet_ID=automatic_pet_id()
                    with open("../data/pet.txt", "a") as file:
                        file.write(f"{username},{pet_ID},{pet}\n")
                    print("Added")
                case 2:
                    PetID=input("Enter pet ID to update: ")
                    with open("../data/pet.txt", "r") as file:
                        pet_list = file.readlines()
                    found = False
                    index = 0  # manual counter
                    for line in pet_list:
                        pet_data = line.strip().split(",")
                        if pet_data[1] == PetID:
                            found = True
                            print("Current data:", pet_data)
                            field = input("What would u like to update? pet(or)petowner/username): ").lower()
                            if field == "pet":
                                while True:
                                    pet =(input("Enter pet's new name: "))
                                    isalpha=check_alphabet(pet)
                                    if isalpha==True:
                                        break
                                    else:
                                        print("A pet name can only contain alphabets")
                                pet_data[2] = pet
                                print("pet name updated successfully.")
                            elif field == "username" or field== "petowner":
                                while True:
                                    username = input("Enter username:")
                                    check_alpha = check_alphabet(username)
                                    if check_alpha == True:
                                        break
                                    else:
                                        print("Enter a valid name(only alphabet)")
                                pet_data[0] = username
                            else:
                                print("Invalid input.")
                            pet_list[index] = ",".join(pet_data) + "\n"
                            break
                        index += 1
                    if not found:
                        print("Pet ID not found.")
                    with open("../data/pet.txt", "w") as file:
                        file.writelines(pet_list)
                case 3:
                    PetID = input("Enter pet ID you want to remove: ")
                    with open("../data/pet.txt", "r") as file:
                        pet_list = file.readlines()
                    found = False
                    index = 0
                    for line in pet_list:
                        pet_data = line.strip().split(",")
                        if pet_data[1] == PetID:
                            del pet_list[index]
                            found = True
                            break
                        index += 1
                    if found:
                        with open("../data/pet.txt", "w") as file:
                            file.writelines(pet_list)
                        print("Pet record deleted successfully.")
                    else:
                        print("Pet ID not found.")
                case 4:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")


def sys_summary():
    with open("../data/pet.txt", "r") as file:
        count=0
        for line in file:
            count=count+1
        pet_amount=count
    with open("../data/booking.txt", "r") as file:
        count=0
        for line in file:
            count=count+1
            booking_amount=count
    with open("../data/users.txt", "r") as file:
        count=0
        for line in file:
            count=count+1
            user_amount=count
    with open("../data/slots.txt", "r") as file:
        count=0
        for line in file:
            count=count+1
            used_slot=count
            if used_slot<10:
                available_slot=10-used_slot
            elif used_slot==10:
                available_slot="full"
            else:
                available_slot="Error"
        used_slot=count
    with open("../data/service_history.txt", "r") as file:
        total=0
        for line in file:
            data=line.strip().split(",")
            price=data[4]
            price=float(price)
            total=total+price
    print(f"""
    ============================
    Service System Report
    ============================

    Total Pet Owners/Users: {user_amount}
    Total Pets Registered: {pet_amount}
    Total Bookings: {booking_amount}

    Total Revenue: RM {total}
    -----------
    Slot info
    -----------
    Max slot=10
    Taken slot={used_slot}
    Available slot: {available_slot} 
    """)



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
                case 3:
                    sys_summary()
                case 4:
                    break
                case _:
                    print("Enter a valid option")
        except ValueError:
            print("Invalid choice. Please try again.")
        except Exception:
            print("Unknown error occured. Please try again.")

show_sys_admin_menu()