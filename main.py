

class Mountain:
    name = ""
    __high = 0
    country = ""
    has_schelter = False

    def get_high(self):
        return self.__high
    def set_high(self, high):
        self.__high = high
    def __init__(self, name="", high=0, country="", has_schelter=False):
        self.name = name
        self.__high = high
        self.country = country
        self.has_schelter = has_schelter

    def get_high_to_the_top(self):
        currentHigh = int(input("Enter your current high: "))
        if currentHigh > self.__high: #write an exception!
            print("You enter wrong high")
        else:
            return self.__high-currentHigh
    def describe(self):
        print(self.name, self.__high, self.country, self.has_schelter)

mountain = Mountain()
mountain.name = "Sniezka"
mountain.country = "Poland"
mountain.has_schelter = True
mountain.set_high(1602)
print(mountain.get_high_to_the_top())
mountain.describe()

mountain2 = Mountain("Matterhorn")
mountain2.country = "Switzerland"
mountain2.has_schelter = False
mountain2.set_high(4478)
print(mountain2.get_high_to_the_top())
mountain2.describe()

mountain3 = Mountain(name="Gerlach", high=2655, country="Slovakia")
mountain3.has_schelter = False
print(mountain3.get_high_to_the_top())
mountain3.describe()