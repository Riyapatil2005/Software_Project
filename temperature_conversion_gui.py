import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    try:
        value = float(entry_value.get())
        unit = combo_unit.get()

        if unit == 'Celsius (°C)':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            celsius = value
        elif unit == 'Fahrenheit (°F)':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            fahrenheit = value
        elif unit == 'Kelvin (K)':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            kelvin = value
        else:
            raise ValueError("Invalid unit of measurement")

        result_text.set(f"{value} {unit} is equivalent to:\n"
                        f"{celsius:.2f} °C\n"
                        f"{fahrenheit:.2f} °F\n"
                        f"{kelvin:.2f} K")
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Please enter a valid temperature value.")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion Program")

# Value input
label_value = ttk.Label(root, text="Enter the temperature value:")
label_value.grid(column=0, row=0, padx=10, pady=5)

entry_value = ttk.Entry(root)
entry_value.grid(column=1, row=0, padx=10, pady=5)

# Unit selection
label_unit = ttk.Label(root, text="Select the unit of measurement:")
label_unit.grid(column=0, row=1, padx=10, pady=5)

combo_unit = ttk.Combobox(root, values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])
combo_unit.grid(column=1, row=1, padx=10, pady=5)
combo_unit.current(0)  # set default selection to Celsius

# Convert button
button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(column=0, row=2, columnspan=2, pady=10)

# Result display
result_text = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_text, justify="left")
label_result.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
