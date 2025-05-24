import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        if var.get() == "Speed":
            distance = float(entry1.get())
            time = float(entry2.get())
            result = distance / time
            result_label.config(text=f"Speed = {result:.2f} km/h")
        elif var.get() == "Distance":
            speed = float(entry1.get())
            time = float(entry2.get())
            result = speed * time
            result_label.config(text=f"Distance = {result:.2f} km")
        elif var.get() == "Time":
            distance = float(entry1.get())
            speed = float(entry2.get())
            result = distance / speed
            result_label.config(text=f"Time = {result:.2f} hours")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

app = tk.Tk()
app.title("Speed Calculator")

var = tk.StringVar(value="Speed")

options = ["Speed", "Distance", "Time"]
tk.Label(app, text="Select Calculation:").grid(row=0, column=0, padx=10, pady=10)
option_menu = tk.OptionMenu(app, var, *options)
option_menu.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Input 1:").grid(row=1, column=0, padx=10, pady=10)
entry1 = tk.Entry(app)
entry1.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Input 2:").grid(row=2, column=0, padx=10, pady=10)
entry2 = tk.Entry(app)
entry2.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="Result will be shown here.")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()
