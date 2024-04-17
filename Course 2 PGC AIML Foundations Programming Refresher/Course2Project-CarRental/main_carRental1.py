# main.py
from car_rental_utils import CarRental
import datetime

if __name__ == "__main__":
    rental_shop = CarRental()

    rental_shop.display_available_cars()

    print("\nCost per rental:")
    print("Sedan - Hourly: $15, Daily: $70, Weekly: $250")
    print("SUV - Hourly: $20, Daily: $90, Weekly: $300")
    print("Hatchback - Hourly: $10, Daily: $50, Weekly: $200")

    car_type = input("\nEnter the type of car you want to rent: ")
    rental_duration = int(input("Enter the rental duration (in hours): "))
    rental_mode = input("Enter the rental mode (hourly/daily/weekly): ")

    rental_time = datetime.datetime.now()

    if rental_mode == "hourly":
        rental_time -= datetime.timedelta(hours=rental_duration)
        if car_type == "Sedan":
            rental_shop.rent_hourly(car_type, 1, rental_time, hourly_rate=15)
        elif car_type == "SUV":
            rental_shop.rent_hourly(car_type, 1, rental_time, hourly_rate=20)
        elif car_type == "Hatchback":
            rental_shop.rent_hourly(car_type, 1, rental_time, hourly_rate=10)
        else:
            print("Invalid car type.")
    elif rental_mode == "daily":
        rental_time -= datetime.timedelta(days=rental_duration)
        if car_type == "Sedan":
            rental_shop.rent_daily(car_type, 1, rental_time, daily_rate=70)
        elif car_type == "SUV":
            rental_shop.rent_daily(car_type, 1, rental_time, daily_rate=90)
        elif car_type == "Hatchback":
            rental_shop.rent_daily(car_type, 1, rental_time, daily_rate=50)
        else:
            print("Invalid car type.")
    elif rental_mode == "weekly":
        rental_time -= datetime.timedelta(weeks=rental_duration)
        if car_type == "Sedan":
            rental_shop.rent_weekly(car_type, 1, rental_time, weekly_rate=250)
        elif car_type == "SUV":
            rental_shop.rent_weekly(car_type, 1, rental_time, weekly_rate=300)
        elif car_type == "Hatchback":
            rental_shop.rent_weekly(car_type, 1, rental_time, weekly_rate=200)
        else:
            print("Invalid car type.")
    else:
        print("Invalid rental mode.")

