from  utils.reciept_ica import *
from utils.db_handler import * 
from utils.process_handler import * 


while True: 
    
    cml_command = input()

    if cml_command == 'Get data ': 
        extracted_list = populate_data() 
        print(populate_data())
    elif cml_command == 'write db':
        insert_receipts_to_db(extracted_list)
        print('Skriptet har körts.. ')
    elif cml_command == 'debug': 
        print(extract_data())
    elif cml_command == 'write_all': 
        process_pdfs_in_folder('kvitto')
    else: 
        print('failuuure')
