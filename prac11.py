from datetime import datetime, timedelta

# Vehicle class
class Vehicle:
    def __init__(self, vehicle_id, make, model, price_per_day, availability=True):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.price_per_day = price_per_day
        self.availability = availability  # Availability status of the vehicle

    def mark_unavailable(self):
        self.availability = False

    def mark_available(self):
        self.availability = True

    def __str__(self):
        return f"{self.make} {self.model} (ID: {self.vehicle_id}) - ${self.price_per_day}/day"

# RentalAgency class
class RentalAgency:
    def __init__(self, agency_name):
        self.agency_name = agency_name
        self.vehicles = []  # List of available vehicles
        self.rental_transactions = []  # List of completed transactions

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def view_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.vehicles if vehicle.availability]
        if available_vehicles:
            for vehicle in available_vehicles:
                print(vehicle)
        else:
            print("No vehicles available for rent at the moment.")

    def rent_vehicle(self, vehicle_id, customer, start_date, end_date):
        vehicle = self._find_vehicle(vehicle_id)

        if vehicle and vehicle.availability:
            rental_transaction = RentalTransaction(vehicle, customer, start_date, end_date)
            rental_transaction.process_rental()
            self.rental_transactions.append(rental_transaction)
            vehicle.mark_unavailable()  # Mark the vehicle as unavailable once rented
            print(f"Rental booked successfully for {customer.name}.")
        else:
            print("Vehicle not available for rental.")

    def _find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None  # Return None if vehicle not found

# RentalTransaction class
class RentalTransaction:
    def __init__(self, vehicle, customer, start_date, end_date):
        self.vehicle = vehicle
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = 0
        self.transaction_date = datetime.now()

    def calculate_total_price(self):
        rental_days = (self.end_date - self.start_date).days
        if rental_days < 1:
            rental_days = 1  # Ensure at least 1 day of rental
        self.total_price = rental_days * self.vehicle.price_per_day
        return self.total_price

    def process_rental(self):
        self.calculate_total_price()
        print(f"Vehicle: {self.vehicle.make} {self.vehicle.model}")
        print(f"Customer: {self.customer.name}")
        print(f"Rental Period: {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}")
        print(f"Total Rental Price: ${self.total_price:.2f}")
        print(f"Transaction Date: {self.transaction_date.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def __str__(self):
        return f"Rental Transaction for {self.customer.name} - Vehicle: {self.vehicle.make} {self.vehicle.model}"

# Customer class
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id}) - Email: {self.email}"


# Example usage
if __name__ == "__main__":
    # Create rental agency
    agency = RentalAgency("City Car Rentals")

    # Add vehicles to the agency's fleet
    v1 = Vehicle(101, "Toyota", "Corolla", 30)
    v2 = Vehicle(102, "Ford", "Focus", 40)
    v3 = Vehicle(103, "Chevrolet", "Malibu", 50)

    agency.add_vehicle(v1)
    agency.add_vehicle(v2)
    agency.add_vehicle(v3)

    # Create a customer
    customer = Customer(201, "Jane Smith", "jane.smith@example.com")

    # View available vehicles
    print("Available Vehicles:")
    agency.view_available_vehicles()

    # Rent a vehicle (with a rental period)
    start_date = datetime(2025, 3, 1)  # March 1, 2025
    end_date = datetime(2025, 3, 7)  # March 7, 2025
    agency.rent_vehicle(101, customer, start_date, end_date)

    # View remaining available vehicles
    print("\nAvailable Vehicles after booking:")
    agency.view_available_vehicles()

    # Trying to rent an unavailable vehicle
    agency.rent_vehicle(101, customer, start_date, end_date)

    # Rent another vehicle
    start_date = datetime(2025, 3, 5)  # March 5, 2025
    end_date = datetime(2025, 3, 8)  # March 8, 2025
    agency.rent_vehicle(102, customer, start_date, end_date)

    # View all rental transactions
    print("\nRental Transactions:")
    for transaction in agency.rental_transactions:
        print(transaction)
