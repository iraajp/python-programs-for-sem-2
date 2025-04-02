import tkinter as tk
from tkinter import messagebox

# Conversion Functions
def convert_units():
    try:
        value = float(entry_value.get())  # Get input value
        conversion_type = conversion_var.get()  # Get selected conversion type
        
        if conversion_type == 'Rupees to Dollars':
            result = value / 83.0  # 1 USD = 83 INR (approx)
            result_label.config(text=f"Result: ${result:.2f} USD")
        
        elif conversion_type == 'Celsius to Fahrenheit':
            result = (value * 9/5) + 32  # Celsius to Fahrenheit formula
            result_label.config(text=f"Result: {result:.2f} °F")
        
        elif conversion_type == 'Inches to Feet':
            result = value / 12  # 1 foot = 12 inches
            result_label.config(text=f"Result: {result:.2f} feet")
        
        else:
            result_label.config(text="Select a valid conversion type")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

# Set up the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Create Labels
label_instructions = tk.Label(root, text="Enter a value to convert:")
label_instructions.pack(pady=10)

# Create Entry widget for input
entry_value = tk.Entry(root)
entry_value.pack(pady=10)

# Create dropdown menu for conversion type
conversion_var = tk.StringVar()
conversion_var.set("Rupees to Dollars")  # Default option

conversion_menu = tk.OptionMenu(root, conversion_var, 
                                "Rupees to Dollars", 
                                "Celsius to Fahrenheit", 
                                "Inches to Feet")
conversion_menu.pack(pady=10)

# Create Convert button
convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.pack(pady=10)

# Create label for result
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
