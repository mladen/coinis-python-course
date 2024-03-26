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
            # raise ValueError("Red value must be between 0 and 255")
            print("Out of range")
            pass
        else:
            self.__red = value

    def add_red(self, change):
        if self.__red + change < 0 or self.__red + change > 255:
            print("Out of range")
            pass
        else:
            self.__red += change

    def get_green(self):
        return self.__green

    def set_green(self, value):
        if value < 0 or value > 255:
            print("Out of range")
            pass
        self.__green = value

    def add_green(self, change):
        if self.__green + change < 0 or self.__green + change > 255:
            print("Out of range")
            pass
        else:
            self.__green += change

    def get_blue(self):
        return self.__blue

    def set_blue(self, value):
        if value < 0 or value > 255:
            print("Out of range")
            pass
        else:
            self.__blue = value

    def add_blue(self, change):
        if self.__blue + change < 0 or self.__blue + change > 255:
            print("Out of range")
            pass
        else:
            self.__blue += change


red = Color(255, 0, 0)
print(red)
red.add_red(10)
red.add_red(-310)
print(red)
