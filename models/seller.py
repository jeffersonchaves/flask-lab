class Seller:

    def __init__(self, name: str):
        self.Name = name
        self.BaseSalary = None

    def __str__(self):
        return self.Name + " " + str(self.BaseSalary)
