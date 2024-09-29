import os
from utils.db_handler import insert_receipts_to_db  # Din funktion för att skriva till databasen
from utils.reciept_ica import populate_data  # Din funktion för att bearbeta en PDF och returnera datan

def process_pdfs_in_folder(folder_path):
    # Hämta alla PDF-filer i mappen
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        print(f"Bearbetar: {pdf_path}")
        
        # Bearbeta varje PDF och hämta kvittodata
        receipts_list = populate_data(pdf_path)
        
        # Infoga kvittodatan i databasen
        insert_receipts_to_db(receipts_list)

    print("Bearbetning klar.")


