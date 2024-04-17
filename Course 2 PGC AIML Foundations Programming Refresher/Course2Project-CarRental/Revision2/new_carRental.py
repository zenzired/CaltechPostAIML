from datetime import datetime, timedelta

class Car:
    def __init__(self, car_id, car_maker, car_model, car_year, category, color):
        self.car_id = car_id
        self.car_maker = car_maker
        self.car_model = car_model
        self.car_year = car_year
        self.category = category
        self.color = color
        self.available = True

class CarInventory:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_available_cars(self):
        print("Available Cars:")
        for car in self.cars:
            if car.available:
                print(f"ID: {car.car_id}, Maker: {car.car_maker}, Model: {car.car_model}, Year: {car.car_year}, Category: {car.category}, Color: {car.color}")

    def rent_car(self, car_id, num_cars, rental_mode):
        rented_cars = []
        current_time = datetime.now()
        for car in self.cars:
            if car.car_id == car_id and car.available:
                car.available = False
                rented_cars.append(car)
                print(f"{num_cars} {car.car_maker} {car.car_model} rented successfully at {current_time}")
                break
        else:
            print("Car not available or invalid ID.")

        return rented_cars, current_time, rental_mode

    def return_car(self, rented_cars, rental_time, rental_mode, num_cars):
        for car in rented_cars:
            car.available = True

        return_time = datetime.now()
        rental_period = return_time - rental_time
        total_hours = rental_period.total_seconds() / 3600

        total_cost = 0
        for car in rented_cars:
            if rental_mode == 'hourly':
                total_cost += self.calculate_hourly_cost(car.category, total_hours, num_cars)
            elif rental_mode == 'daily':
                total_cost += self.calculate_daily_cost(car.category, total_hours, num_cars)
            elif rental_mode == 'weekly':
                total_cost += self.calculate_weekly_cost(car.category, total_hours, num_cars)

        print(f"{num_cars} car(s) returned successfully at {return_time}")
        print(f"Total Cost: ${total_cost}")

    def calculate_hourly_cost(self, category, total_hours, num_cars):
        if category == 'SUV':
            return 20 * total_hours * num_cars
        elif category == 'Pickup':
            return 25 * total_hours * num_cars
        elif category == 'Sedan':
            return 15 * total_hours * num_cars
        elif category == 'Hatchback':
            return 18 * total_hours * num_cars

    def calculate_daily_cost(self, category, total_hours, num_cars):
        total_days = total_hours / 24
        if category == 'SUV':
            return 100 * total_days * num_cars
        elif category == 'Pickup':
            return 120 * total_days * num_cars
        elif category == 'Sedan':
            return 80 * total_days * num_cars
        elif category == 'Hatchback':
            return 90 * total_days * num_cars

    def calculate_weekly_cost(self, category, total_hours, num_cars):
        total_weeks = total_hours / (24 * 7)
        if category == 'SUV':
            return 500 * total_weeks * num_cars
        elif category == 'Pickup':
            return 600 * total_weeks * num_cars
        elif category == 'Sedan':
            return 400 * total_weeks * num_cars
        elif category == 'Hatchback':
            return 450 * total_weeks * num_cars

# Example Usage:
inventory = CarInventory()
inventory.add_car(Car(1, 'Toyota', 'RAV4', 2022, 'SUV', 'Blue'))
inventory.add_car(Car(2, 'Ford', 'F-150', 2023, 'Pickup', 'Black'))
# Add more cars similarly

inventory.display_available_cars()

rented_cars, rental_time, rental_mode = inventory.rent_car(1, 1, 'hourly')

# Simulate some time passing
returned_cars = inventory.return_car(rented_cars, rental_time, rental_mode, 1)
