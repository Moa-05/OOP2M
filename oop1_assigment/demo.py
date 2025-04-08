from customer_system import CustomerDataSystem
from datetime import datetime, timedelta

def main():
    # Create a new customer data system
    system = CustomerDataSystem("MyCustomerSystem")
    
    print("=== Demonstrering av CustomerDataSystem ===")
    
    # Add some customers
    try:
        system.add_customer("Anna Andersson", "anna@example.com", "0701234567")
        system.add_customer("Bertil Bengtsson", "bertil@example.com", "0702345678")
        system.add_customer("Cecilia Carlsson", "cecilia@example.com", "0703456789")
    except ValueError as e:
        print(f"Fel vid tillägg av kund: {e}")
    
    # List all customers
    system.list_all_customers()
    
    # Add some interactions
    try:
        system.add_interaction("anna@example.com", "Telefon", "Kund ringde för att fråga om produkter")
        system.add_interaction("bertil@example.com", "E-post", "Svarade på frågor om leveranstid")
        system.add_interaction("cecilia@example.com", "Möte", "Personligt möte för att diskutera nya projekt")
    except KeyError as e:
        print(f"Fel vid tillägg av interaktion: {e}")
    
    # Update contact information
    try:
        system.update_contact_info("anna@example.com", new_phone="0709876543")
        system.update_contact_info("bertil@example.com", new_email="bertil.ny@example.com")
    except (KeyError, ValueError) as e:
        print(f"Fel vid uppdatering av kontaktinformation: {e}")
    
    # Try to add a customer with existing email (should raise error)
    try:
        system.add_customer("David Davidsson", "anna@example.com", "0704567890")
    except ValueError as e:
        print(f"Förväntat fel vid tillägg av kund med existerande e-post: {e}")
    
    # Try to remove a non-existent customer (should raise error)
    try:
        system.remove_customer("nonexistent@example.com")
    except KeyError as e:
        print(f"Förväntat fel vid borttagning av icke-existerande kund: {e}")
    
    # List inactive customers (should be empty at this point)
    system.list_inactive_customers()
    
    # Add an old interaction to make a customer inactive
    try:
        # Create a customer with an old interaction
        system.add_customer("Erik Eriksson", "erik@example.com", "0705678901")
        # Simulate an old interaction by modifying the last_interaction
        customer = system._find_customer_by_email("erik@example.com")
        if customer:
            customer.last_interaction = datetime.now() - timedelta(days=35)
    except (ValueError, KeyError) as e:
        print(f"Fel vid skapande av inaktiv kund: {e}")
    
    # List inactive customers again (should show Erik)
    system.list_inactive_customers()

if __name__ == "__main__":
    main() 