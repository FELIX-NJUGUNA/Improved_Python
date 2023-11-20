class Resistor:
    # Define the color band names
    band_colors = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    # Private data members
    band1 = None
    band2 = None
    band3 = None
    value = None

    # Constructor taking three strings as parameters
    # and calculating the resistance
    def __init__(self, b1, b2, b3, colors=None):
        if colors is None:
            colors = Resistor.band_colors

        # Convert band colors to their corresponding numeric values
        b1_num = colors[b1.lower()]
        b2_num = colors[b2.lower()]
        b3_num = colors[b3.lower()]

        # Calculate the resistor value
        resistance = (b1_num * 10 + b2_num) * 10 ** b3_num

        # Set the private resistance value
        self.value = resistance

    # Set the resistance value
    def setResistance(self, val):
        self.value = val

    # Get the resistance value
    def getResistance(self):
        return self.value


resistor = Resistor("white", "red", "black")

print(resistor.getResistance())
