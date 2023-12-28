from database.database_operation_Toernooien import ToernooienDatabaseOperations

def run_toernooien_interface():
    toernooien_db = ToernooienDatabaseOperations()

    while True:
        print("\nToernooien Beheer:")
        print("1. Add Toernooi ")
        print("2. View toernooi Details")
        print("3. View all toernooien")
        print("4. Remove Toernooi")
        print("5. Go back")

        choice = input("Select an option (1/2/3/4/5): ")

        if choice == "1":
            voeg_toernooi_toe(toernooien_db)
        elif choice == "2":
            bekijk_toernooi_details(toernooien_db)
        elif choice == "3":
            bekijk_alle_toernooien(toernooien_db)
        elif choice == "4":
            verwijder_toernooi(toernooien_db)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    toernooien_db.close_connection()

def voeg_toernooi_toe(db):
    print("\nAdd a new toernooi:")
    naam = input("Name: ")
    club = input("Club: ")

    db.add_toernooi(naam, club)

def bekijk_toernooi_details(db):
    print("\nView toernooi details:")
    toernooi_id = input("Enter the toernooi ID: ")

    toernooi_details = db.get_all_toernooien()
    
    gevonden_toernooi = next((toernooi for toernooi in toernooi_details if toernooi[0] == int(toernooi_id)), None)

    if gevonden_toernooi:
        print(f"Details of Toernooi {toernooi_id}:")
        print(f"Name: {gevonden_toernooi[1]}")
        print(f"Club: {gevonden_toernooi[2]}")
    else:
        print(f"Toernooi with ID {toernooi_id} not found.")

def verwijder_toernooi(db):
    print("\nRemove toernooi:")
    toernooi_id = input("Enter the ID of the toernooi to delete: ")

    db.delete_toernooi(toernooi_id)

def bekijk_alle_toernooien(db):
    print("\nAll Toernooien:")
    toernooi_details = db.get_all_toernooien()

    if toernooi_details:
        for toernooi in toernooi_details:
            print(f"Toernooi ID: {toernooi[0]}, Name: {toernooi[1]}, Club: {toernooi[2]}")
    else:
        print("No toernooien found.")
