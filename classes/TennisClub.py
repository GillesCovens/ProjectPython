class TennisClub:
    def __init__(self, name, location, membership_fee):
        self.name = name
        self.location = location
        self.membership_fee = membership_fee

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_membership_fee(self):
        return self.membership_fee

    def set_name(self, name):
        answer = input("Are you sure you want to change the name of the club? (y/n)")
        if answer == "y":
            self.name = name
        else:
            print("The name of the club is not changed.")




