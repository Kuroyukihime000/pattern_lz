class Mashin:
    def __init__(self):
        self.mark = None
        self.model = None
        self.year = None

    def __str__(self):
        return (f"{self.year} {self.mark} {self.model}")

class BuildMashin:
    def __init__(self):
        self.car = Mashin()

    def u_make(self, mark):
        self.car.mark = mark
        return self

    def u_model(self, model):
        self.car.model = model
        return self

    def u_year(self, year):
        self.car.year = year
        return self
    
    def build(self):
        return self.car


