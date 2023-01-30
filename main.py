

class Mountain:
    def __init__(self, name, high, country, has_schelter):
        self.name = name
        self.__high = high
        self.country = country
        self.has_schelter = has_schelter

    def get_high(self):
        return self.__high
    def set_high(self, high):
        self.__high = high

    def get_high_to_the_top(self):
        currentHigh = int(input("Enter your current high: "))
        if currentHigh > int(self.__high):
            print("You enter wrong high")
        else:
            return self.__high-currentHigh
    def describe(self):
        print(self.name, self.__high, self.country, self.has_schelter)

mountain = Mountain("Sniezka",1602, "Poland", True)
print(mountain.get_high_to_the_top())
mountain.describe()

mountain2 = Mountain("Matterhorn", 4478, "Switzerland", False)
print(mountain2.get_high_to_the_top())
mountain2.describe()

mountain3 = Mountain(name="Gerlach", high=2655, country="Slovakia", False)
print(mountain3.get_high_to_the_top())
mountain3.describe()