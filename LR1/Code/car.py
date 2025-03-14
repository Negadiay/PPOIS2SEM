class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.is_sold = False
        self.is_prepared = False

    def __str__(self):
        status = "Prepared" if self.is_prepared else "Not Prepared"
        return f"{self.make} {self.model} {self.year} - ${self.price} ({status})"

    def prepare_for_sale(self):
        self.is_prepared = True
        return f"{self} has been prepared for sale."
