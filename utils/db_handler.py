import sqlite3

def insert_receipts_to_db(receipts_list):
    # Skapa (eller anslut till) databasen
    conn = sqlite3.connect('db/receipt_database.db')
    cursor = conn.cursor()

    # Skapa tabellen om den inte redan finns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum TEXT,
            artikelnummer TEXT,
            beskrivning TEXT,
            antal TEXT,
            pris REAL,
            summa REAL,
            butik TEXT,
            UNIQUE(datum, artikelnummer, beskrivning, antal, pris, summa, butik)  -- Unik constraint
        )
    ''')

    # Lägg till varje kvitto i tabellen
    for receipt in receipts_list:
        cursor.execute('''
            INSERT OR IGNORE INTO receipts (datum, artikelnummer, beskrivning, antal, pris, summa, butik)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (receipt['datum'], receipt['artikelnummer'], receipt['beskrivning'], 
            receipt['antal'], receipt['pris'], receipt['summa'], receipt['butik']))
        
    # Spara ändringarna och stäng anslutningen
    conn.commit()
    conn.close()

