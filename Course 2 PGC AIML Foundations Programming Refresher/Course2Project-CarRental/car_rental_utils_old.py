# car_rental_utils.py
import datetime
from car_inventory import cars_inventory

class CarRental:
    def __init__(self):
        self.available_cars = cars_inventory
        self.rented_cars = {}

    def display_available_cars(self):
        print("Available Cars:")
        for car, details in self.available_cars.items():
            print(f"{car} (Year Model: {details['year_model']}): {details['quantity']}")

    def rent_hourly(self, car_type, num_cars, rental_time):
        return self._rent(car_type, num_cars, rental_time, "hourly", hourly_rate=10)

    def rent_daily(self, car_type, num_cars, rental_time):
        return self._rent(car_type, num_cars, rental_time, "daily", daily_rate=50)

    def rent_weekly(self, car_type, num_cars, rental_time):
        return self._rent(car_type, num_cars, rental_time, "weekly", weekly_rate=200)

    def _rent(self, car_type, num_cars, rental_time, rental_mode, hourly_rate=None, daily_rate=None, weekly_rate=None):
        if car_type not in self.available_cars:
            print(f"Error: {car_type} is not available for rent.")
            return None
        
        if num_cars <= 0:
            print("Error: Number of cars should be positive.")
            return None
        
        if num_cars > self.available_cars[car_type]["quantity"]:
            print("Error: Requested number of cars exceeds available stock.")
            return None

        self.available_cars[car_type]["quantity"] -= num_cars
        self.rented_cars[car_type] = self.rented_cars.get(car_type, 0) + num_cars
        print(f"{num_cars} {car_type}(s) rented on {rental_mode} basis at {rental_time}.")
        return rental_time

    def return_cars(self, rental_time, car_type, num_cars, rental_mode):
        if car_type not in self.rented_cars or self.rented_cars[car_type] == 0:
            print(f"No {car_type} rented previously.")
            return None

        if rental_mode == "hourly":
            rate = 10
        elif rental_mode == "daily":
            rate = 50
        elif rental_mode == "weekly":
            rate = 200
        else:
            print("Invalid rental mode.")
            return None

        rental_period = self._calculate_rental_period(rental_time)
        bill = rental_period * rate * num_cars

        self.available_cars[car_type]["quantity"] += num_cars
        self.rented_cars[car_type] -= num_cars
        print(f"{num_cars} {car_type}(s) returned. Rental bill: ${bill}")
        return bill

    def _calculate_rental_period(self, rental_time):
        return (datetime.datetime.now() - rental_time).days
