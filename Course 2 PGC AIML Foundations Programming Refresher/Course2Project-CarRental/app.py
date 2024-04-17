from flask import Flask, render_template, request
import datetime
from car_rental_utils import CarRental

app = Flask(__name__)
rental_shop = CarRental()

@app.route("/")
def index():
    rental_shop.display_available_cars()
    return render_template("index.html")

@app.route("/rent", methods=["POST"])
def rent():
    car_type = request.form["car_type"]
    rental_duration = int(request.form["rental_duration"])
    rental_mode = request.form["rental_mode"]

    rental_time = datetime.datetime.now()
    if rental_mode == "hourly":
        rental_time -= datetime.timedelta(hours=rental_duration)
    elif rental_mode == "daily":
        rental_time -= datetime.timedelta(days=rental_duration)
    elif rental_mode == "weekly":
        rental_time -= datetime.timedelta(weeks=rental_duration)

    rental_shop.rent(car_type, rental_duration, rental_mode, rental_time)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
