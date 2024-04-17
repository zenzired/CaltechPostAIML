class CarRental:
    def __init__(self, cars_inventory):
        self.available_cars = cars_inventory
        self.rented_cars = {}

    def rent_car(self, customer_name, car_name):
        if car_name in self.available_cars:
            self.available_cars.remove(car_name)
            self.rented_cars[car_name] = customer_name
            print(f"{customer_name} rented {car_name}.")
        else:
            print(f"Sorry, {car_name} is not available for rent.")

    def return_car(self, car_name):
        if car_name in self.rented_cars:
            customer_name = self.rented_cars.pop(car_name)
            self.available_cars.append(car_name)
            print(f"{customer_name} returned {car_name}.")
        else:
            print(f"{car_name} is not rented out.")
