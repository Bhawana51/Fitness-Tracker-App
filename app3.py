import tkinter as tk
from tkinter import messagebox
from datetime import date

data = {}

def add_entry():
    day = date.today().strftime("%Y-%m-%d")
    workout = workout_entry.get()
    calories = calories_entry.get()
    if workout and calories.isdigit():
        data[day] = {"Workout": workout, "Calories": int(calories)}
        update_summary()
    else:
        messagebox.showwarning("Input Error", "Enter valid workout and calories.")

def update_summary():
    summary.delete("1.0", tk.END)
    for d, entry in data.items():
        summary.insert(tk.END, f"{d}: {entry['Workout']} - {entry['Calories']} cal\n")

root = tk.Tk()
root.title("Fitness Tracker App")

tk.Label(root, text="Workout:").pack()
workout_entry = tk.Entry(root)
workout_entry.pack()

tk.Label(root, text="Calories Burned:").pack()
calories_entry = tk.Entry(root)
calories_entry.pack()

tk.Button(root, text="Add Entry", command=add_entry).pack(pady=10)

summary = tk.Text(root, height=10, width=50)
summary.pack()

root.mainloop()
