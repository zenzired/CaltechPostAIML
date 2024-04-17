# main.py
from car_rental_utils import CarRental
import datetime

if __name__ == "__main__":
    rental_shop = CarRental()

    rental_shop.display_available_cars()

    car_type = input("Enter the type of car you want to rent: ")
    rental_duration = int(input("Enter the rental duration (in hours): "))
    rental_mode = input("Enter the rental mode (hourly/daily/weekly): ")

    rental_time = datetime.datetime.now()

    if rental_mode == "hourly":
        rental_time -= datetime.timedelta(hours=rental_duration)
    elif rental_mode == "daily":
        rental_time -= datetime.timedelta(days=rental_duration)
    elif rental_mode == "weekly":
        rental_time -= datetime.timedelta(weeks=rental_duration)
    else:
        print("Invalid rental mode.")
        exit()

    rental_shop.rent(car_type, rental_duration, rental_mode, rental_time)
