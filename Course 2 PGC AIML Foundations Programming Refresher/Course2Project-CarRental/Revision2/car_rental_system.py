# car_rental_system.py

from datetime import datetime
from CarInventory import cars  # Import the cars data from the CarInventory module

class CarInventory:
    """Class to manage the car inventory and rental operations."""

    def __init__(self):
        """Initialize the CarInventory with available cars and ongoing rentals."""
        self.cars = cars  # Initialize with available cars from CarInventory module
        self.rentals = []  # Initialize list to track ongoing rentals

    def display_available_cars(self):
        """Display all available cars in the inventory."""
        print("Available Cars:")
        for car in self.cars:
            if car.available:
                print(f"ID: {car.car_id}, Maker: {car.car_maker}, Model: {car.car_model}, Year: {car.car_year}, Category: {car.category}, Color: {car.color}")

    def display_cars_by_category(self, category):
        """Display available cars in a specific category."""
        print(f"Available {category} Cars:")
        for car in self.cars:
            if car.available and car.category.upper() == category.upper():
                print(f"ID: {car.car_id}, Maker: {car.car_maker}, Model: {car.car_model}, Year: {car.car_year}, Color: {car.color}")

    def rent_car(self, car_id, rental_mode):
        """Rent a car based on car ID and rental mode (hourly, daily, weekly)."""
        cost_per_hour = None
        for car in self.cars:
            if car.car_id == car_id and car.available:
                if car.category.upper() == 'SUV':
                    cost_per_hour = 20
                elif car.category.upper() == 'PICKUP':
                    cost_per_hour = 25
                elif car.category.upper() == 'SEDAN':
                    cost_per_hour = 15
                elif car.category.upper() == 'HATCHBACK':
                    cost_per_hour = 18

                rental_time = datetime.now()
                car.available = False
                self.rentals.append((car.car_id, rental_time, cost_per_hour))
                print(f"Car {car.car_id} (Category: {car.category}) rented successfully at {rental_time}.")
                return rental_time, cost_per_hour * self.calculate_rental_duration(rental_mode), cost_per_hour
        print("Car not available or invalid ID.")
        return None, None, None

    def return_car(self, car_id, rental_time, cost_per_hour):
        """Return a rented car and generate a bill."""
        for car in self.cars:
            if car.car_id == car_id and not car.available:
                for i, rental in enumerate(self.rentals):
                    if rental[0] == car_id:
                        del self.rentals[i]
                        break

                return_time = datetime.now()
                rental_duration = return_time - rental_time
                total_hours = rental_duration.total_seconds() / 3600
                total_cost = total_hours * cost_per_hour
                car.available = True
                print(f"Car {car.car_id} returned successfully.")
                self.generate_bill(car_id, rental_time, return_time, cost_per_hour, total_hours, total_cost)
                return
        print("Car not rented or invalid ID.")

    def generate_bill(self, car_id, rental_time, return_time, cost_per_hour, total_hours, total_cost):
        """Generate a bill for the returned car."""
        print("*************** Bill ***************")
        print(f"Car ID: {car_id}")
        print(f"Rental Time: {rental_time}")
        print(f"Return Time: {return_time}")
        print(f"Rental Duration: {total_hours:.2f} hours")
        print(f"Cost per Hour: ${cost_per_hour:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")
        print("************************************")

    def calculate_rental_duration(self, rental_mode):
        """Calculate the rental duration based on the rental mode."""
        if rental_mode == 'hourly':
            return 1
        elif rental_mode == 'daily':
            return 24
        elif rental_mode == 'weekly':
            return 24 * 7
        else:
            print("Invalid rental mode. Defaulting to hourly rental.")
            return 1

    def display_ongoing_rentals(self):
        """Display ongoing rentals."""
        print("Ongoing Rentals:")
        for car_id, rental_time, cost_per_hour in self.rentals:
            return_time = datetime.now()
            rental_duration = return_time - rental_time
            total_hours = rental_duration.total_seconds() / 3600
            print(f"Car ID: {car_id}, Rental Time: {rental_time}, Duration: {total_hours:.2f} hours, Cost per Hour: ${cost_per_hour:.2f}")

def main():
    """Main function to run the car rental system."""
    inventory = CarInventory()

    print("Welcome to the Car Rental System!")
    while True:
        print("\nMenu:")
        print("1. Display All Available Cars")
        print("2. Display Cars by Category")
        print("3. Rent a Car")
        print("4. Return a Car")
        print("5. Display Ongoing Rentals")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.display_available_cars()
        elif choice == '2':
            category = input("Enter the category (SUV/Pickup/Sedan/Hatchback): ").capitalize()
            if category.upper() in {'SUV', 'PICKUP', 'SEDAN', 'HATCHBACK'}:
                inventory.display_cars_by_category(category.upper())
            else:
                print("Invalid category. Please try again.")
        elif choice == '3':
            car_id = int(input("Enter the ID of the car you want to rent: "))
            rental_mode = input("Enter the rental mode (hourly/daily/weekly): ")
            rental_time, total_cost, cost_per_hour = inventory.rent_car(car_id, rental_mode)
            if total_cost is not None:
                print(f"Rental cost: ${total_cost:.2f}")
        elif choice == '4':
            car_id = int(input("Enter the ID of the car you want to return: "))
            inventory.return_car(car_id, rental_time, cost_per_hour)
        elif choice == '5':
            inventory.display_ongoing_rentals()
        elif choice == '6':
            print("Thank you for using the Car Rental System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
