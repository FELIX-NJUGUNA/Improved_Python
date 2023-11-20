import tkinter as tk

from resistor import Resistor


class ResistorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Resistor Calculator")

        # Color band entry widgets
        self.band1_entry = tk.Entry(self.master)
        self.band2_entry = tk.Entry(self.master)
        self.band3_entry = tk.Entry(self.master)

        # Label widgets
        tk.Label(self.master, text="Band 1 Color:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Band 2 Color:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Band 3 Color:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.master, text="Resistance Value:").grid(row=4, column=0, padx=10, pady=5)

        # Display widgets
        self.band1_entry.grid(row=0, column=1, padx=10, pady=5)
        self.band2_entry.grid(row=1, column=1, padx=10, pady=5)
        self.band3_entry.grid(row=2, column=1, padx=10, pady=5)

        # Resistance display label
        self.resistance_label = tk.Label(self.master, text="")
        self.resistance_label.grid(row=4, column=1, padx=10, pady=5)

        # Calculate button
        tk.Button(self.master, text="Calculate Resistance", command=self.calculate_resistance).grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_resistance(self):
        # Get color inputs from entry widgets
        b1_color = self.band1_entry.get().lower()
        b2_color = self.band2_entry.get().lower()
        b3_color = self.band3_entry.get().lower()

        # Create Resistor instance with user input
        resistor = Resistor(b1_color, b2_color, b3_color)

        # Display the calculated resistance
        self.resistance_label.config(text=f"{resistor.getResistance()} ohms")


if __name__ == "__main__":
    root = tk.Tk()
    app = ResistorApp(root)
    root.mainloop()
