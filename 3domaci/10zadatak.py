from dataclasses import dataclass


@dataclass
class Color:
    # red, green and blue are integers between 0 and 255; these properties should be private
    __red: int
    __green: int
    __blue: int

    def __str__(self):
        return f"Color({self.__red}, {self.__green}, {self.__blue})"

    def get_red(self):
        return self.__red

    def set_red(self, value):
        if value < 0 or value > 255:
            raise ValueError("Red value must be between 0 and 255")
        self.__red = value

    def get_green(self):
        return self.__green

    def set_green(self, value):
        if value < 0 or value > 255:
            raise ValueError("Green value must be between 0 and 255")
        self.__green = value

    def get_blue(self):
        return self.__blue

    def set_blue(self, value):
        if value < 0 or value > 255:
            raise ValueError("Blue value must be between 0 and 255")
        self.__blue = value
