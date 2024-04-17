# Car Rental System

This is a simple car rental system implemented in Python. It allows users to rent cars on an hourly, daily, or weekly basis, return them, and view ongoing rentals.

## Features

- Display available cars
- Display cars by category
- Rent a car
- Return a car
- Display ongoing rentals

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/car-rental-system.git
    ```

2. **Navigate to the directory:**

    ```bash
    cd car-rental-system
    ```

3. **Run the car rental system:**

    ```bash
    python car_rental_system.py
    ```

4. **Follow the prompts to interact with the car rental system:**

    - Choose from the menu options to view available cars, rent a car, return a car, or view ongoing rentals.
    - When prompted, enter the required information such as car ID, rental mode, etc.
    - If the selected car is unavailable for rental, the system will display a message indicating that the car is not available and prompt you to choose another option.

## Limitations

1. **Simplified Billing:** The billing system in the program is basic and may not handle complex billing scenarios or additional charges such as insurance fees, taxes, etc.
2. **No User Authentication:** The program does not include user authentication mechanisms, making it unsuitable for multi-user environments where user identification and authorization are required.
3. **Single-User Interface:** The program operates as a single-user command-line application and does not support concurrent users or multiple sessions simultaneously.
4. **Limited Inventory Management:** While the program allows for renting and returning cars, it lacks advanced inventory management features such as car maintenance scheduling, damage tracking, or automated alerts for low inventory.
5. **No Database Integration:** The car inventory data is stored within the program and does not utilize a database backend. This may limit scalability and data persistence in larger-scale applications.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Short Write-up

The Python Car Rental System is a simple yet efficient command-line program designed to manage car rentals. Built using Python, it offers users the ability to rent cars on an hourly, daily, or weekly basis, return them, and view ongoing rentals. With a user-friendly interface and intuitive functionality, it provides a convenient solution for car rental needs. However, users should be aware of its limitations and consider additional requirements for more advanced use cases.
