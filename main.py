import tkinter as tk
from tkinter import messagebox, simpledialog

class UnitConverter:
    def __init__(self):
        self.history = []

    def convert_length(self, value, from_unit, to_unit):
        length_units = {
            'meters': 1,
            'kilometers': 1000,
            'miles': 1609.34,
            'feet': 0.3048,
            'inches': 0.0254,
            'yards': 0.9144,
            'nautical_miles': 1852
        }
        if from_unit not in length_units or to_unit not in length_units:
            raise KeyError("Invalid length unit.")
        return round(value * (length_units[from_unit] / length_units[to_unit]), 2)

    def convert_mass(self, value, from_unit, to_unit):
        mass_units = {
            'grams': 1,
            'kilograms': 1000,
            'pounds': 453.592,
            'ounces': 28.3495,
            'stones': 6350.29
        }
        if from_unit not in mass_units or to_unit not in mass_units:
            raise KeyError("Invalid mass unit.")
        return round(value * (mass_units[from_unit] / mass_units[to_unit]), 2)

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return round((value * 9/5) + 32, 2)
            elif to_unit == 'Kelvin':
                return round(value + 273.15, 2)
            else:
                return value
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return round((value - 32) * 5/9, 2)
            elif to_unit == 'Kelvin':
                return round((value - 32) * 5/9 + 273.15, 2)
            else:
                return value
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return round(value - 273.15, 2)
            elif to_unit == 'Fahrenheit':
                return round((value - 273.15) * 9/5 + 32, 2)
            else:
                return value
        else:
            raise KeyError("Invalid temperature unit.")

    def add_to_history(self, conversion):
        self.history.append(conversion)

    def show_history(self):
        if not self.history:
            return "Conversion history is empty."
        else:
            return "\n".join(self.history)

class ConverterApp:
    def __init__(self, root):
        self.converter = UnitConverter()
        self.root = root
        self.root.title("Unit Converter")

        self.label = tk.Label(root, text="Select conversion type:")
        self.label.pack()

        self.length_button = tk.Button(root, text="Length", command=self.convert_length)
        self.length_button.pack()

        self.mass_button = tk.Button(root, text="Mass", command=self.convert_mass)
        self.mass_button.pack()

        self.temperature_button = tk.Button(root, text="Temperature", command=self.convert_temperature)
        self.temperature_button.pack()

        self.history_button = tk.Button(root, text="Show Conversion History", command=self.show_history)
        self.history_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def get_valid_unit(self, prompt, valid_units):
        while True:
            unit = simpledialog.askstring("Input", prompt)
            if unit and unit.strip().lower() in valid_units:
                return unit.strip().lower()
            else:
                messagebox.showerror("Error", f"Invalid unit. Please choose from: {', '.join(valid_units)}")

    def convert_length(self):
        try:
            value = float(simpledialog.askstring("Input", "Enter value:"))
            from_unit = self.get_valid_unit("Enter unit (meters, kilometers, miles, feet, inches, yards, nautical_miles):", 
                                              ['meters', 'kilometers', 'miles', 'feet', 'inches', 'yards', 'nautical_miles'])
            to_unit = self.get_valid_unit("Enter unit to convert to (meters, kilometers, miles, feet, inches, yards, nautical_miles):", 
                                          ['meters', 'kilometers', 'miles', 'feet', 'inches', 'yards', 'nautical_miles'])
            result = self.converter.convert_length(value, from_unit, to_unit)
            conversion_str = f"{value} {from_unit} = {result} {to_unit}"
            messagebox.showinfo("Result", conversion_str)
            self.converter.add_to_history(conversion_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value.")

    def convert_mass(self):
        try:
            value = float(simpledialog.askstring("Input", "Enter value:"))
            from_unit = self.get_valid_unit("Enter unit (grams, kilograms, pounds, ounces, stones):", 
                                              ['grams', 'kilograms', 'pounds', 'ounces', 'stones'])
            to_unit = self.get_valid_unit("Enter unit to convert to (grams, kilograms, pounds, ounces, stones):", 
                                          ['grams', 'kilograms', 'pounds', 'ounces', 'stones'])
            result = self.converter.convert_mass(value, from_unit, to_unit)
            conversion_str = f"{value} {from_unit} = {result} {to_unit}"
            messagebox.showinfo("Result", conversion_str)
            self.converter.add_to_history(conversion_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value.")

    def convert_temperature(self):
        try:
            value = float(simpledialog.askstring("Input", "Enter value:"))
            from_unit = self.get_valid_unit("Enter unit (Celsius, Fahrenheit, Kelvin):", 
                                              ['celsius', 'fahrenheit', 'kelvin'])
            to_unit = self.get_valid_unit("Enter unit to convert to (Celsius, Fahrenheit, Kelvin):", 
                                          ['celsius', 'fahrenheit', 'kelvin'])
            result = self.converter.convert_temperature(value, from_unit, to_unit)
            conversion_str = f"{value} {from_unit} = {result} {to_unit}"
            messagebox.showinfo("Result", conversion_str)
            self.converter.add_to_history(conversion_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter a numeric value.")

    def show_history(self):
        history = self.converter.show_history()
        messagebox.showinfo("Conversion History", history)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
