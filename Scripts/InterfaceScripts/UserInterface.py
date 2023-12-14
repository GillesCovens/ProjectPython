from Scripts.MakeClub import create_tennis_club
from database.database_operations_Leden import DatabaseOperations
from Scripts.PrintScripts.PrintToCSV import export_all_members_to_csv
from Scripts.PrintScripts.PrintToExcel import export_all_members_to_excel
from Scripts.InterfaceScripts.UserinterfaceToernooi import run_toernooien_interface 
def main_menu():
    db_operations = DatabaseOperations("database/DatabaseTC.db")
    created_club = None

    while True:
        print("\nMain Menu:")
        
        if created_club is None:
            print("1. Create Tennis Club")
            print("2. Exit")
            choice = input("Enter your choice (1, 2): ")
        else:
            print(f"Club '{created_club.name}' is currently active.")
            print("2. Print All Members")
            print("3. Add Member")
            print("4. Delete Member")
            print("5. Export Members List")
            print("6. Change Club Membership Fee")
            print("7. View Club Details")
            print("8. Toernooi Menu")
            print("9. Exit") 
            choice = input("Enter your choice ( 2, 3, 4, 5, 6, 7, 8, or 9): ")

        if choice == "1" and created_club is None:
            created_club = create_tennis_club()
            if created_club:
                print("\nTennis Club Information:")
                print(f"Name: {created_club.name}")
                print(f"Location: {created_club.location}")
                print(f"Membership Fee: ${created_club._membership_fee:.2f}")
        elif choice == "2" and created_club is not None:
            db_operations.print_all_lid()
        elif choice == "3" and created_club is not None:
            first_name = input("Enter member's first name: ")
            last_name = input("Enter member's last name: ")
            email = input("Enter member's email: ")
            db_operations.add_lid(first_name, last_name, email)
        elif choice == "4" and created_club is not None:
            identifier = input("Enter member's email or ID to delete: ")
            db_operations.delete_lid(identifier)
        elif choice == "5" and created_club is not None:
            export_option = input("Choose export format (1. Excel, 2. CSV): ")
            if export_option == "1":
                export_all_members_to_excel()
            elif export_option == "2":
                export_all_members_to_csv()
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif choice == "6" and created_club is not None:
            new_fee = float(input("Enter the new membership fee for the club: "))
            created_club.set_membership_fee(new_fee)
            print(f"Membership fee updated to ${new_fee:.2f}.")
        elif choice == "7" and created_club is not None:
            print("\nClub Details:")
            print(f"Name: {created_club.name}")
            print(f"Location: {created_club.location}")
            print(f"Membership Fee: ${created_club.get_membership_fee():.2f}")
        elif choice == "8":
            run_toernooien_interface() 
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
