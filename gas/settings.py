import tkinter as tk
from tkinter import ttk

def getSettings():

    ballCount = 150
    isChecked = False
    keepWindow = True

    def on_checkbox_toggled():
        print(f"Checkbox is {'checked' if checkbox_var.get() else 'unchecked'}")

    def on_slider_changed(value):
        slider_value_label.config(text=f"Value: {int(float(value))}")

    def on_button_clicked():
        global return_value
        return_value = (ballCount, isChecked)
        root.destroy()  # Close the Tkinter window

    # Create the main window
    root = tk.Tk()
    root.title("Slider and Checkbox Example")

    # Create a frame for better organization
    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Add a label for the slider
    slider_label = ttk.Label(frame, text="Number of Balls:")
    slider_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    # Add a slider with range from 0 to 300
    slider = ttk.Scale(frame, from_=0, to=300, orient='horizontal', command=on_slider_changed)
    slider.grid(row=0, column=1, padx=5, pady=5)

    # Add a label to display the current slider value
    slider_value_label = ttk.Label(frame, text="150")
    slider_value_label.grid(row=0, column=2, padx=5, pady=5)

    # Add a label for the checkbox
    checkbox_label = ttk.Label(frame, text="Shrinking Container?")
    checkbox_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    # Add a checkbox
    checkbox_var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(frame, variable=checkbox_var, command=on_checkbox_toggled)
    checkbox.grid(row=1, column=1, padx=5, pady=5)

    # Add a button below everything
    button = ttk.Button(frame, text="Run", command=on_button_clicked)
    button.grid(row=2, column=0, columnspan=3, pady=10)

    # Set a default value for the slider
    slider.set(150)

    # Start the Tkinter event loop
    root.mainloop()
    return return_value
