class TennisClub:
    def __init__(self, name, location, membership_fee):
        self.name = name
        self.location = location
        self._membership_fee = membership_fee

    def get_name(self):
        return self.name

    def get_membership_fee(self):
        return self._membership_fee

    def set_membership_fee(self, membership_fee):
        self._membership_fee = membership_fee

    def get_location(self):
        return self.location

    def set_name(self, name):
        answer = input("Are you sure you want to change the name of the club? (y/n) ")
        if answer.lower() == "y":
            self.name = name
            print("The name of the club has been changed.")
        else:
            print("The name of the club is not changed.")

    def get_details(self):
        return f"Club Details:\nName: {self.name}\nLocation: {self.location}\nMembership Fee: ${self._membership_fee:.2f}"
