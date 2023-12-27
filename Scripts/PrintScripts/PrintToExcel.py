import pandas as pd
from database.database_operations_Leden import DatabaseOperations
import os 

def export_all_members_to_excel():
    db_operations = DatabaseOperations("database/DatabaseTC.db")
    members = db_operations.get_all_lid()

    if not members:
        print("No members found.")
        return

    while True:
        excel_file_path = input("Enter the path where you want to save the Excel file (e.g., members_export.xlsx): ")
        
        if not excel_file_path.endswith('.xlsx'):
            excel_file_path += '.xlsx'

        if os.path.isabs(excel_file_path) and not os.path.exists(excel_file_path):
            break
        else:
            print("Invalid file path. Please enter a valid and non-existing path.")

    columns = ["ID", "FirstName", "LastName", "Email"]
    members_df = pd.DataFrame(members, columns=columns)

    members_df.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f"Members exported to {excel_file_path} successfully.")