# main_carRental.py
from car_rental_utils import CarRental
import datetime

if __name__ == "__main__":
    rental_shop = CarRental()

    rental_time = datetime.datetime(2024, 3, 30, 10, 0)

    rental_shop.display_available_cars()

    rental_time = rental_shop.rent_hourly("Sedan", 2, rental_time)
    rental_time = rental_shop.rent_daily("Hatchback", 1, rental_time)
    rental_time = rental_shop.rent_weekly("SUV", 1, rental_time)

    print("\nAfter rental:")
    rental_shop.display_available_cars()

    rental_time = datetime.datetime(2024, 3, 31, 12, 0)
    rental_shop.return_cars(rental_time, "Sedan", 2, "hourly")
    rental_shop.return_cars(rental_time, "Hatchback", 1, "daily")
    rental_shop.return_cars(rental_time, "SUV", 1, "weekly")

    print("\nAfter return:")
    rental_shop.display_available_cars()
