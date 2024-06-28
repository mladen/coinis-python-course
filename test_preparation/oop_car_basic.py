# Getter, Setter and Deleter in Python


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        self._year = value

    @year.deleter
    def year(self):
        del self._year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


newcar1 = Car("Toyota", "Corolla", 2019)

print(newcar1)  # Toyota Corolla (2019)

# Set the brand to 123
newcar1.brand = "123"
print(newcar1)  # Toyota Corolla (2019)
