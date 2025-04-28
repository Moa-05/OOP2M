import pandas as pd
import os

# Sätt rätt sökvägar
input_path = r"C:\Users\moab1\AppData\Local\Temp\f17aad81-b9aa-491d-9970-cdb9e8568f75_OOP2_final_home_assignment (4).zip.f75\OOP2_final_home_assignment\exercise_3\sales_data.csv"
output_path = os.path.join(os.path.dirname(__file__), 'cleaned_sales_data.csv')

try:
    # Steg 1: Läs in data
    data = pd.read_csv(input_path)
    print("Lyckades läsa in data:")
    print(data.head())

    # Steg 2: Ta bort rader med duplicerade ordernummer
    if 'order_number' in data.columns:
        data = data.drop_duplicates(subset=['order_number'])
        print("Duplicerade ordernummer borttagna.")
    else:
        print("Kolumnen 'order_number' saknas i data. Skipping this step.")

    # Steg 3: Beräkna total_price om den saknas
    if 'total_price' not in data.columns:
        if 'Count sold' in data.columns and 'Price per item' in data.columns:
            data['total_price'] = data['Count sold'] * data['Price per item']
            print("Kolumnen 'total_price' har beräknats.")
        else:
            print("Kolumnen 'Count sold' eller 'Price per item' saknas, och 'total_price' kan inte beräknas.")

    # Steg 4: Ta bort outliers i total_price (> 8000)
    if 'total_price' in data.columns:
        data = data[data['total_price'] <= 8000]
        print("Outliers i 'total_price' borttagna.")
    else:
        print("Kolumnen 'total_price' saknas i data. Skipping this step.")

    # Steg 5: Ta bort rader med tomma product_list
    if 'product_list' in data.columns:
        data = data[data['product_list'].notna()]
        print("Rader med tomma 'product_list' borttagna.")
    else:
        print("Kolumnen 'product_list' saknas i data. Skipping this step.")

    # Steg 6: Konvertera datumformat med felhantering
    if 'order_date' in data.columns:
        data['order_date'] = pd.to_datetime(data['order_date'], errors='coerce')
        data = data[data['order_date'].notna()]  # Ta bort felaktiga datum
        print("Datumformat konverterat och felaktiga datum borttagna.")
    else:
        print("Kolumnen 'order_date' saknas i data. Skipping this step.")

    # Steg 7: Spara resultatet till ny fil
    data.to_csv(output_path, index=False)
    print(f"Rensad data sparad till: {output_path}")
except FileNotFoundError:
    print(f"Filen hittades inte på sökvägen: {input_path}")
except Exception as e:
    print(f"Ett fel inträffade: {e}")
