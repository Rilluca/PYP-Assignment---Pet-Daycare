# All functions for daycare/grooming staff will be here
# - Update pet care status (feeding, grooming, activities).
# - Log daily care and grooming records.
# - Generate service summary report.

# Menu message for daycare/grooming staff
daycare_staff_menu = f"""
{'-' * 50}
Daycare/Grooming Staff Menu
{'-' * 50}
What would you like to do today?
1. Add daily care record
2. Add daily grooming record
3. Update pet care status
4. Generate summary report
5. Quit
"""

def show_daycare_staff_menu():
    print(daycare_staff_menu)

    while True:
        try:
            # Ask user for choice input
            daycare_staff_choice = int(input("Enter your choice: "))

            # Match case for menu selection
            match daycare_staff_choice:
                case 1:
                    print("replace function to system admin here")
                    break

                case 2:
                    print("replace function to booking officer here")
                    break

                case 3:
                    print("abc")
                    break

                case 4:
                    print("Quitting program now.")
                    break

                case _:
                    print("Input can only be in number and within range, please try again.\n")

        except ValueError:
            print("Input can only be in number and within range, please try again.\n")

