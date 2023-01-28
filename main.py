

class Mountain:
    name = ""
    high = 0
    country = ""
    has_schelter = False

    def get_high_to_the_top(self):
        currentHigh = int(input("Enter your current high: "))
        if currentHigh > self.high: #write an exception!
            print("You enter wrong high")
        else:
            return self.high-currentHigh
    def describe(self):
        print(self.name, self.high, self.country, self.has_schelter)

mountain = Mountain()
mountain.high = 1602
mountain.name = "Sniezka"
mountain.country = "Poland"
mountain.has_schelter = True

print(mountain.get_high_to_the_top())
mountain.describe()


mountain2 = Mountain()
mountain2.name = "Matterhorn"
mountain2.high = 4478
mountain2.country = "Switzerland"
mountain2.has_schelter = False
print(mountain2.get_high_to_the_top())

mountain3 = Mountain()
mountain3.name = "Gerlach"
mountain3.high = 2655
mountain3.country = "Slovakia"
mountain3.has_schelter = False
print(mountain3.get_high_to_the_top())