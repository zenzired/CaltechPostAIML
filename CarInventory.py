# CarInventory.py

class Car:
    def __init__(self, car_id, car_maker, car_model, car_year, category, color):
        self.car_id = car_id
        self.car_maker = car_maker
        self.car_model = car_model
        self.car_year = car_year
        self.category = category
        self.color = color
        self.available = True

cars = [
    Car(1, 'Toyota', 'RAV4', 2022, 'SUV', 'Blue'),
    Car(2, 'Ford', 'F-150', 2023, 'Pickup', 'Black'),
    Car(3, 'Honda', 'Civic', 2021, 'Sedan', 'Red'),
    Car(4, 'Toyota', 'Corolla', 2024, 'Sedan', 'White'),
    Car(5, 'Mazda', 'CX-5', 2023, 'SUV', 'Silver'),
    Car(6, 'Ford', 'Focus', 2022, 'Hatchback', 'Gray'),
    Car(7, 'Chevrolet', 'Silverado', 2024, 'Pickup', 'Blue'),
    Car(8, 'Honda', 'CR-V', 2023, 'SUV', 'Black'),
    Car(9, 'Hyundai', 'Elantra', 2022, 'Sedan', 'Red'),
    Car(10, 'Toyota', 'Camry', 2024, 'Sedan', 'White'),
    Car(11, 'Nissan', 'Rogue', 2022, 'SUV', 'Blue'),
    Car(12, 'Ram', '1500', 2023, 'Pickup', 'Silver'),
    Car(13, 'Volkswagen', 'Jetta', 2022, 'Sedan', 'Black'),
    Car(14, 'Subaru', 'Outback', 2023, 'SUV', 'Green'),
    Car(15, 'Kia', 'Forte', 2022, 'Sedan', 'Gray'),
    Car(16, 'Jeep', 'Wrangler', 2024, 'SUV', 'Red'),
    Car(17, 'GMC', 'Sierra', 2023, 'Pickup', 'White'),
    Car(18, 'BMW', 'X5', 2022, 'SUV', 'Black'),
    Car(19, 'Mercedes', 'C-Class', 2024, 'Sedan', 'Silver'),
    Car(20, 'Ford', 'Escape', 2023, 'SUV', 'Blue'),
    Car(21, 'Chevrolet', 'Colorado', 2022, 'Pickup', 'Red'),
    Car(22, 'Hyundai', 'Santa Fe', 2023, 'SUV', 'Gray'),
    Car(23, 'Honda', 'Accord', 2022, 'Sedan', 'White'),
    Car(24, 'Toyota', 'Highlander', 2024, 'SUV', 'Black'),
    Car(25, 'Nissan', 'Frontier', 2023, 'Pickup', 'Red'),
    Car(26, 'Audi', 'A4', 2022, 'Sedan', 'Silver'),
    Car(27, 'Subaru', 'Forester', 2024, 'SUV', 'Blue'),
    Car(28, 'Dodge', 'Ram', 2023, 'Pickup', 'Black'),
    Car(29, 'Tesla', 'Model 3', 2022, 'Sedan', 'White'),
    Car(30, 'Lexus', 'RX', 2024, 'SUV', 'Gray'),
    Car(31, 'GMC', 'Canyon', 2022, 'Pickup', 'Red'),
    Car(32, 'Volkswagen', 'Tiguan', 2023, 'SUV', 'Blue'),
    Car(33, 'BMW', '3 Series', 2022, 'Sedan', 'Black'),
    Car(34, 'Ford', 'Ranger', 2024, 'Pickup', 'White'),
    Car(35, 'Hyundai', 'Sonata', 2023, 'Sedan', 'Red'),
    Car(36, 'Jeep', 'Grand Cherokee', 2022, 'SUV', 'Silver'),
    Car(37, 'Chevrolet', 'Silverado', 2024, 'Pickup', 'Blue'),
    Car(38, 'Honda', 'Pilot', 2023, 'SUV', 'Black'),
    Car(39, 'Mazda', 'Mazda3', 2022, 'Sedan', 'Gray'),
    Car(40, 'Toyota', 'Tundra', 2024, 'Pickup', 'Red')
    # Add more cars similarly
]
