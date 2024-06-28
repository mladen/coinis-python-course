# Getter, Setter, and Deleter in Python


class Car:
    def __init__(self, car_model, car_fuel_consumption, car_previous_owners):
        self.car_model = car_model
        self.car_fuel_consumption = car_fuel_consumption
        self.car_previous_owners = car_previous_owners

    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        self._car_model = value

    @property
    def car_fuel_consumption(self):
        return self._car_fuel_consumption

    @car_fuel_consumption.setter
    def car_fuel_consumption(self, value):
        if not isinstance(value, float):
            raise ValueError("Fuel consumption must be a float")
        self._car_fuel_consumption = value

    @property
    def car_previous_owners(self):
        return self._car_previous_owners

    @car_previous_owners.setter
    def car_previous_owners(self, value):
        if not isinstance(value, list):
            raise ValueError("Previous owners must be a list")
        self._car_previous_owners = value

    def __str__(self):
        return f"Car model: {self.car_model}, Fuel consumption: {self.car_fuel_consumption}, Previous owners: {self.car_previous_owners}"


car1 = Car("Honda", 5.5, [{"owner_name": "John Malkovich", "days_owned": 943}])
