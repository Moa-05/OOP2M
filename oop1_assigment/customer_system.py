from datetime import datetime

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Customer(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
        self.interactions = []
        self.last_interaction = None

    def add_interaction(self, interaction_type, notes):
        """Adds a new interaction with the customer and updates last_interaction."""
        interaction = {
            'timestamp': datetime.now(),
            'type': interaction_type,
            'notes': notes
        }
        self.interactions.append(interaction)
        self.last_interaction = interaction['timestamp']
        print(f"Added new interaction for customer {self.name}")

    def calculate_days_since_last_interaction(self):
        """Calculates days since last interaction or returns None if no interactions."""
        if not self.last_interaction:
            return None
        days = (datetime.now() - self.last_interaction).days
        return days

    def is_inactive(self):
        """Checks if customer is inactive (no interaction for more than 30 days)."""
        days_since = self.calculate_days_since_last_interaction()
        return days_since is not None and days_since > 30

class CustomerDataSystem:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        """Adds a new customer to the system."""
        # Check if email already exists
        if any(customer.email == email for customer in self.customers):
            raise ValueError(f"En kund med e-postadressen {email} finns redan i systemet.")
        
        new_customer = Customer(name, email, phone)
        self.customers.append(new_customer)
        print(f"Ny kund med namn {name} har lagts till")

    def remove_customer(self, email):
        """Removes a customer from the system."""
        customer = self._find_customer_by_email(email)
        if not customer:
            raise KeyError(f"Kund med e-postadress {email} hittades inte i systemet.")
        
        self.customers.remove(customer)
        print(f"Kund med e-postadress {email} har tagits bort")

    def update_contact_info(self, email, new_phone=None, new_email=None):
        """Updates a customer's contact information."""
        customer = self._find_customer_by_email(email)
        if not customer:
            raise KeyError(f"Kund med e-postadress {email} hittades inte i systemet.")
        
        if new_email:
            # Check if new email already exists
            if any(c.email == new_email for c in self.customers if c != customer):
                raise ValueError(f"E-postadressen {new_email} används redan av en annan kund.")
            customer.email = new_email
        
        if new_phone:
            customer.phone = new_phone
        
        print(f"Kontaktinformation för kund {customer.name} har uppdaterats")

    def add_interaction(self, email, interaction_type, notes):
        """Adds an interaction for a specific customer."""
        customer = self._find_customer_by_email(email)
        if not customer:
            raise KeyError(f"Kund med e-postadress {email} hittades inte i systemet.")
        
        customer.add_interaction(interaction_type, notes)

    def get_customer_interactions(self, email):
        """Returns all interactions for a specific customer."""
        customer = self._find_customer_by_email(email)
        if not customer:
            raise KeyError(f"Kund med e-postadress {email} hittades inte i systemet.")
        
        return customer.interactions

    def list_all_customers(self):
        """Prints a list of all customers in the system."""
        print("\nLista över alla kunder:")
        for customer in self.customers:
            print(f"- {customer.name} ({customer.email})")

    def list_inactive_customers(self):
        """Prints a list of all inactive customers."""
        inactive_customers = [c for c in self.customers if c.is_inactive()]
        if not inactive_customers:
            print("\nInga inaktiva kunder hittades")
            return
        
        print("\nLista över inaktiva kunder:")
        for customer in inactive_customers:
            days_since = customer.calculate_days_since_last_interaction()
            print(f"- {customer.name}: {days_since} dagar sedan senaste interaktion")

    def _find_customer_by_email(self, email):
        """Helper method to find a customer by email."""
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None 