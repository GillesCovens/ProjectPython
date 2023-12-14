import sqlite3

class ToernooienDatabaseOperations:
    def __init__(self):
        self.connection = sqlite3.connect('database/DatabaseTC.db')
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def add_toernooi(self, naam, club):
        insert_query = '''
        INSERT INTO "Toernooien" ("Naam", "Club")
        VALUES (?, ?);
        '''
        try:
            self.cursor.execute(insert_query, (naam, club))
            self.connection.commit()
            print("Toernooi toegevoegd.")
        except sqlite3.Error:
            print("Error: Kan het toernooi niet toevoegen.")

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
            print("Geen toernooien gevonden.")
        else:
            print("Alle toernooien:")
            for toernooi in toernooien:
                print(f"ID: {toernooi[0]}, Naam: {toernooi[1]}, Club: {toernooi[2]}")

    def delete_toernooi(self, identifier):
        delete_query = '''
        DELETE FROM "Toernooien" WHERE "id" = ?;
         '''
        try:
            # Omzetten naar integer indien nodig
            toernooi_id = int(identifier)

            # Voer de query uit
            self.cursor.execute(delete_query, (toernooi_id,))
            self.connection.commit()
            print("Toernooi verwijderd.")
        except (ValueError, sqlite3.Error):
            print("Fout: Toernooi niet gevonden of kan niet worden verwijderd.")


    def close_connection(self):
        self.connection.close()
