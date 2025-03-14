class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Customer: {self.name}, Phone: {self.phone}"
