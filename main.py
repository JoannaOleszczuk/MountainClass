class Mountain:
    name = ""
    high = 0
    country = ""
    schelter = None

    def get_high_to_the_top(self):
        currentHigh = int(input("Enter your current high: "))
        if currentHigh > self.high:
            print("You enter wrong high")
        else:
            return self.high-currentHigh

mountain = Mountain()
mountain.name = "Sniezka"
mountain.high = 1602
mountain.country = "Poland"
mountain.schelter = True

def describe_mountain1(mountain):
    print(mountain.name, mountain.high, mountain.country, mountain.schelter)
describe_mountain1(mountain)

print(mountain.get_high_to_the_top())

mountain2 = Mountain()
mountain2.name = "Matterhorn"
mountain2.high = 4478
mountain2.country = "Switzerland"
mountain2.schelter = False
print(mountain2.get_high_to_the_top())

mountain3 = Mountain()
mountain3.name = "Gerlach"
mountain3.high = 2655
mountain3.country = "Slovakia"
mountain3.schelter = False
print(mountain3.get_high_to_the_top())