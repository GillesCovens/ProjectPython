from classes.TennisClub import TennisClub

def create_tennis_club():
    print("Welcome to the Tennis Club creation wizard!")

    name = input("Enter the name of the tennis club: ")
    location = input("Enter the location of the tennis club: ")

    while True:
        try:
            membership_fee = float(input("Enter the membership fee of the tennis club: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the membership fee.")

    print("\nOverview of entered information:")
    print(f"Name: {name}")
    print(f"Location: {location}")
    print(f"Membership Fee: ${membership_fee:.2f}")

    confirm = input("Do you want to create the tennis club with the above information? (yes/no): ").lower()

    if confirm == "yes":
        tennis_club = TennisClub(name, location, membership_fee)
        print("Tennis Club created successfully!")
        return tennis_club
    else:
        print("Tennis Club creation canceled.")
        return None
