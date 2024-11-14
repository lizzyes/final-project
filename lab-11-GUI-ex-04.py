import tkinter as tk
import random

# Create main window
groot = tk.Tk()
groot.geometry("300x300")
groot.title("Counter Application")

# Counter variable
counter = tk.IntVar(value = 0)  # Start showing 0

# Define functions for button actions
def increment():
    counter.set(counter.get() + 1)

def decrement():
    counter.set(counter.get() - 1)

def randomize():
    counter.set(random.randint(0, 100))

# Create and place label
label = tk.Label(groot, textvariable = counter, font = ("Arial", 24))
label.pack(pady = 20)

# Create and place buttons
btn_increment = tk.Button(groot, text = "Increment", command = increment)
btn_increment.pack(pady = 10)

btn_random = tk.Button(groot, text = "Random", command = randomize)
btn_random.pack(pady = 10)

btn_decrement = tk.Button(groot, text = "Decrement", command = decrement)
btn_decrement.pack(pady = 10)

groot.mainloop()
btn_random = tk.Button(groot, text = "Random", command = randomize, font = ("Arial", 14))
btn_random.pack(pady = 5)

btn_decrement = tk.Button(groot, text = "Decrement", command = decrement, font = ("Arial", 14))
btn_decrement.pack(pady = 5)

groot.mainloop()

