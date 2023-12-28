import sqlite3

class ToernooienDatabaseOperations:
    def __init__(self, db_path='database/DatabaseTC.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def add_toernooi(self, naam, club):
        insert_query = '''
        INSERT INTO "Toernooien" ("Naam", "Club")
        VALUES (?, ?);
        '''
        try:
            self.cursor.execute(insert_query, (naam, club))
            self.connection.commit()
            print("Toernooi added.")
        except sqlite3.Error:
            print("Error: Unable to add the tournament.")

    def get_all_toernooien(self):
        select_all_query = '''
        SELECT * FROM "Toernooien";
        '''
        self.cursor.execute(select_all_query)
        toernooien = self.cursor.fetchall()
        return toernooien

    def print_all_toernooien(self):
        toernooien = self.get_all_toernooien()

        if not toernooien:
            print("No tournaments found.")
        else:
            print("All toernooien:")
            for toernooi in toernooien:
                print(f"ID: {toernooi[0]}, Name: {toernooi[1]}, Club: {toernooi[2]}")

    def delete_toernooi(self, identifier):
        delete_query = '''
        DELETE FROM "Toernooien" WHERE "id" = ?;
        '''
        try:
            toernooi_id = int(identifier)
            self.cursor.execute(delete_query, (toernooi_id,))
            self.connection.commit()
            print("Toernooi removed.")
        except (ValueError, sqlite3.Error):
            print("Error: Tournament not found or cannot be deleted.")

    def close_connection(self):
        self.connection.close()
