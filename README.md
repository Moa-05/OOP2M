# Customer Data Management System

Ett system för att hantera kundprofiler och interaktioner med kunder. Systemet hjälper till att organisera, uppdatera och analysera kundinformation.

## Funktioner

- Hantera kundprofiler (lägga till, ta bort, uppdatera)
- Spåra kundinteraktioner
- Identifiera inaktiva kunder (ingen interaktion på över 30 dagar)
- Felhantering för vanliga scenarion

## Installation

1. Klona detta repository
2. Se till att du har Python 3.6 eller senare installerat

## Användning

Systemet består av två huvudklasser:

1. `Customer` - Representerar en individuell kund
2. `CustomerDataSystem` - Hanterar och organiserar kunderna

### Exempel på användning

```python
from customer_system import CustomerDataSystem

# Skapa ett nytt system
system = CustomerDataSystem("MittFöretag")

# Lägg till en kund
system.add_customer("Namn", "email@example.com", "0701234567")

# Lägg till en interaktion
system.add_interaction("email@example.com", "Telefon", "Kund ringde för frågor")

# Uppdatera kontaktinformation
system.update_contact_info("email@example.com", new_phone="0709876543")

# Lista alla kunder
system.list_all_customers()

# Lista inaktiva kunder
system.list_inactive_customers()
```

## Felhantering

Systemet hanterar följande fel:

- Försök att lägga till en kund med en redan existerande e-postadress
- Försök att uppdatera eller interagera med en icke-existerande kund
- Försök att ta bort en icke-existerande kund

## Demo

Kör `demo.py` för att se ett exempel på hur systemet fungerar:

```bash
python demo.py
```

## Krav för Godkänt

- Implementerat alla grundläggande funktioner
- Korrekt felhantering
- Demonstration av funktionalitet

## Krav för Väl Godkänt

- Implementerat funktionalitet för att identifiera inaktiva kunder
- Korrekt hantering av interaktionsdatum
- Omfattande demonstration av systemet # oop2-CDD24
