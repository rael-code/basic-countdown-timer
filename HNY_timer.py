import tkinter as tk
import time
import threading
import random

# List of messages to display
messages = ["Happy New Year!", "Surprise!", "Happy Weekend!", "Blastoff!"]

# List of background colors
background_colors = ["lightblue", "lightgreen", "lightcoral", "lightyellow"]

# Initialize message and background color indices
message_index = 0
color_index = 0

# Function to update and display the next message and background color
def update_message_and_color():
    global message_index, color_index

    if message_index < len(messages):
        countdown_label.config(text=messages[message_index])
        message_index += 1

    if color_index < len(background_colors):
        app.configure(bg=background_colors[color_index])
        color_index += 1
    else:
        color_index = 0  # Reset color_index to cycle through colors

def start_countdown():
    def countdown():
        for _ in reversed(range(1, 11)):
            countdown_label.config(text=_)
            time.sleep(1)

        update_message_and_color()

    countdown_thread = threading.Thread(target=countdown)
    countdown_thread.start()

# Create the main application window
app = tk.Tk()
app.title("Countdown Timer")
app.geometry("300x200")

# Create a label for countdown display with no border
countdown_label = tk.Label(app, text="", font=("Arial", 24), bd=0)
countdown_label.pack(pady=0)

# Create a "Start Countdown" button
start_button = tk.Button(app, text="Start Countdown", command=start_countdown)
start_button.pack()

# Start the GUI event loop
app.mainloop()
