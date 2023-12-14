import sqlite3

class DatabaseOperations:
    def __init__(self, leden):
        self.connection = sqlite3.connect('database/DatabaseTC.db')
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def add_lid(self, first_name, last_name, email):
        insert_query = '''
        INSERT INTO "Lid" ("FirstName", "LastName", "Email")
        VALUES (?, ?, ?);
        '''
        try:
            self.cursor.execute(insert_query, (first_name, last_name, email))
            self.connection.commit()
            print("Member added successfully.")
        except sqlite3.IntegrityError:
            print("Error: Email address must be unique. Member not added.")

    def get_all_lid(self):
        select_all_query = '''
        SELECT * FROM "Lid";
        '''
        self.cursor.execute(select_all_query)
        members = self.cursor.fetchall()
        return members

    def print_all_lid(self):
        members = self.get_all_lid()

        if not members:
            print("No members found.")
        else:
            print("All Members:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]} {member[2]}, Email: {member[3]}")

    def delete_lid(self, identifier):
        delete_query = '''
        DELETE FROM "Lid" WHERE "Email" = ? OR "ID" = ?;
        '''
        try:
            self.cursor.execute(delete_query, (identifier, identifier))
            self.connection.commit()
            print("Member deleted successfully.")
        except sqlite3.Error:
            print("Error: Member not found or unable to delete.")

    def close_connection(self):
        self.connection.close()
