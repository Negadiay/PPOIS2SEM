from car import Car
from customer import Customer
from salesperson import Salesperson
from showroom import Showroom
from test_drive import TestDrive
from service import Service

def main():
    showroom = Showroom()
    salesperson = Salesperson("Deniska")
    customers = {}

    def add_car():
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = input("Enter car year: ")
        price = input("Enter car price: ")
        showroom.add_car(Car(make, model, int(year), float(price)))
        print("Car added successfully!")

    def list_cars():
        cars = showroom.list_cars()
        if cars:
            print("Available cars:")
            for car in cars:
                print(car)
        else:
            print("No available cars.")

    def prepare_car():
        try:
            car_index = int(input("Enter car index to prepare (starting from 0): "))
            print(showroom.cars[car_index].prepare_for_sale())
        except (ValueError, IndexError):
            print("Invalid car index.")

    def sell_car():
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        customers[name] = Customer(name, phone)
        try:
            car_index = int(input("Enter car index to sell (starting from 0): "))
            print(salesperson.sell_car(showroom.cars[car_index], customers[name]))
        except (ValueError, IndexError):
            print("Invalid car index.")

    def test_drive():
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        customers[name] = Customer(name, phone)
        try:
            car_index = int(input("Enter car index for test drive (starting from 0): "))
            test_drive = TestDrive(showroom.cars[car_index], customers[name], salesperson)
            print(test_drive.conduct())
        except (ValueError, IndexError):
            print("Invalid car index.")

    def service_car():
        try:
            car_index = int(input("Enter car index for service (starting from 0): "))
            service = Service(showroom.cars[car_index])
            print(service.perform_service())
        except (ValueError, IndexError):
            print("Invalid car index.")

    def exit_program():
        print("Exiting...")
        exit()

    menu_options = {
        "1": add_car,
        "2": list_cars,
        "3": prepare_car,
        "4": sell_car,
        "5": test_drive,
        "6": service_car,
        "7": exit_program
    }

    while True:
        print("\nCar Dealership System")
        print("1. Add car")
        print("2. List available cars")
        print("3. Prepare a car for sale")
        print("4. Sell a car")
        print("5. Test drive a car")
        print("6. Service a car")
        print("7. Exit")

        choice = input("Choose an option: ")
        action = menu_options.get(choice)

        if action:
            action()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
