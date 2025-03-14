from car import Car

class Service:
    def __init__(self, car):
        self.car = car

    def perform_service(self):
        return f"Service completed for {self.car}."
