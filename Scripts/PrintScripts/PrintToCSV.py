import csv
from database.database_operations_Leden import DatabaseOperations
import os 

def export_all_members_to_csv():
    db_operations = DatabaseOperations("database/DatabaseTC.db")
    members = db_operations.get_all_lid()

    if not members:
        print("No members found.")
        return

    while True:
        csv_file_path = input("Enter the path where you want to save the CSV file (e.g., members_export.csv): ")

        if not csv_file_path.endswith('.csv'):
            csv_file_path += '.csv'

        if os.path.isabs(csv_file_path) and not os.path.exists(csv_file_path):
            break
        else:
            print("Invalid file path. Please enter a valid and non-existing path.")

    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ["ID", "FirstName", "LastName", "Email"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for member in members:
            writer.writerow({"ID": member[0], "FirstName": member[1], "LastName": member[2], "Email": member[3]})

    print(f"Members exported to {csv_file_path} successfully.")
