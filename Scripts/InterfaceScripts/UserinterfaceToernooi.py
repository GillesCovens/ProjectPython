from database.database_operation_Toernooien import ToernooienDatabaseOperations
def run_toernooien_interface():
    toernooien_db = ToernooienDatabaseOperations()

    while True:
        print("\nToernooien Beheer:")
        print("1. Toernooi Toevoegen")
        print("2. Toernooi Details Bekijken")
        print("3. Alle Toernooien Bekijken")
        print("4. Toernooi Verwijderen")
        print("5. Stoppen")

        choice = input("Selecteer een optie (1/2/3/4/5): ")

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
            print("Ongeldige keuze. Probeer opnieuw.")

    # Sluit de databaseverbinding wanneer het programma eindigt
    toernooien_db.close_connection()

def voeg_toernooi_toe(db):
    print("\nVoeg een nieuw toernooi toe:")
    naam = input("Naam: ")
    club = input("Club: ")

    # Roep de methode aan om een toernooi toe te voegen
    db.add_toernooi(naam, club)

def bekijk_toernooi_details(db):
    print("\nBekijk toernooi details:")
    toernooi_id = input("Voer het toernooi ID in: ")

    # Roep de methode aan om details van een bepaald toernooi op te halen
    toernooi_details = db.get_all_toernooien()
    
    # Zoek naar het toernooi met het opgegeven ID
    gevonden_toernooi = None
    for toernooi in toernooi_details:
        if toernooi[0] == int(toernooi_id):
            gevonden_toernooi = toernooi
            break

    if gevonden_toernooi:
        print(f"\nDetails van Toernooi {toernooi_id}:")
        print(f"Naam: {gevonden_toernooi[1]}")
        print(f"Club: {gevonden_toernooi[2]}")
    else:
        print(f"Toernooi met ID {toernooi_id} niet gevonden.")

def verwijder_toernooi(db):
    print("\nVerwijder een toernooi:")
    toernooi_id = input("Voer het ID van het toernooi in om te verwijderen: ")

    db.delete_toernooi(toernooi_id)

def bekijk_alle_toernooien(db):
    print("\nAlle Toernooien:")
    toernooi_details = db.get_all_toernooien()

    if toernooi_details:
        for toernooi in toernooi_details:
            print(f"Toernooi ID: {toernooi[0]}, Naam: {toernooi[1]}, Club: {toernooi[2]}")
    else:
        print("Geen toernooien gevonden.")

