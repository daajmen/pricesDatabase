import pdfplumber 
import re 
from models.receipt_data import ReceiptData


def extract_data(path): 
    with pdfplumber.open(path) as pdf: 
        first_page = pdf.pages[0]

        text = first_page.extract_text()

        return text
        
def populate_data(path): 
    
    raw_data = extract_data(path)
    
    # Leta efter org.nr i formatet SE + 12 siffror
    org_nr_match = re.search(r"SE\d{12}", raw_data)

    # Mappa organisationsnummer till butiksnamn
    butik_mappning = {
        "SE556644042501": "ICA Kvantum Ale",
        "SE556223083801": "Maxi ICA Stormarknad Partille",
        "SE556183227901": "Ica Kvantum Lerum",
        "SE556514953001": "Ica Kvantum Mariestad",
        "SE559405088101": "ICA Nära Furulund",
        "SE559161958901": "ICA Nära Hallsås",
        "SE556783411301": "ICA Supermarket Floda",
        "SE556446279301": "ICA Supermarket Nordeviks",
        "SE556918855901": "Maxi ICA Stormarknad Alingsås",
        "SE556685896401": "Maxi ICA Stormarknad Högsbo",
        "SE556197636501": "Maxi ICA Stormarknad Kungälv",
        "SE556546268501": "ICA Kvantum Landvetter",
        "SE556697170001": "ICA Kvantum Munkebäck",
        "SE559054209701": "ICA Kvantum Mölndal",
        "SE556269459501": "Maxi ICA Stormarknad Göteborg"
        # Lägg till fler org.nr och butiker här
    }


    if org_nr_match:
        org_nr = org_nr_match.group()
        butik_namn = butik_mappning.get(org_nr, "Okänd butik")  # Fallback till "Okänd butik" om inget matchar
        if butik_namn == "Okänd butik":
            print(f'Okänt nummer:  {org_nr}')  # Spara det okända organisationsnumret
    else:
        butik_namn = "Okänd butik"

    # Datum
    datum = re.search(r"\d{4}-\d{2}-\d{2}", raw_data)


    # Mappa data 
    rader = raw_data.split('\n')

    pattern = re.compile(r"(.+?) (\d{10,13}) (\d+\.\d{2}) (\d+(?:\.\d+)? (?:st|kg)) (\d+\.\d{2})")
    
    receipts_list = []  # Lista för att lagra kvittoobjekt

    for rad in rader:
        match = pattern.search(rad)
        if match:
            receipt = ReceiptData()  # Skapa ny instans för varje produkt            
            if datum:         
                receipt.set_datum(datum.group())            
            receipt.set_beskrivning(match.group(1))  
            receipt.set_artikelnummer(match.group(2))
            receipt.set_pris(match.group(3)) 
            receipt.set_antal(match.group(4)) 
            receipt.set_summa(match.group(5)) 
            receipt.set_butik(butik_namn)  # Sätt butiksnamnet till None för nuvarande          

            receipts_list.append(receipt.visa_data())
    return receipts_list