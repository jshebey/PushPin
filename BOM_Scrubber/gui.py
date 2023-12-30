import tkinter as tk
from tkinter import filedialog
from shutil import copyfile
import os
from main import *


# Set Styling
font_style_title = ("Helvetica", 16)
font_style_body  = ("Helvetica", 10)

# Set BOM Directory
directory = "C:\\Users\\jsheb\\PushPin"

# Function for Selecting Files
def open_file_dialog():
    file_paths = filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = [
            ("Excel Files", "*.xls;*.xlsx"), 
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ]
    )
    global files_to_save
    files_to_save = list(file_paths)
    num_files = len(file_paths)
    if files_to_save:
        file_counter.config(text = f"Number of Files: {num_files}")


# Create Main Application Window
app = tk.Tk()
app.title("PushPin")

# Create Frame
frame = tk.Frame(app, bg = "#F0F0F0")
frame.pack(padx=10, pady=10)


# Add title bar at top
title_bar = tk.Label(frame, text = "PushPin BOM Upload", font = font_style_title)
title_bar.pack(side = tk.TOP, fill = tk.X, padx =10, pady = 2)

# Add button to trigger file dialog
upload_button = tk.Button(frame, text = "Click Here to Upload BOM", font = font_style_body, command = open_file_dialog, relief = tk.RAISED, borderwidth=2)
upload_button.pack(pady=10)

# Add scrub button
scrub_button = tk.Button(frame, text = "Scrub", command= lambda:main(files_to_save[0]))
scrub_button.pack(pady=10)

# Label to display selected file path
file_counter = tk.Label(frame, text = "Selected Files: None", font = font_style_body)
file_counter.pack(pady=3)

# Status Bar
status_bar = tk.Label(frame, text = "", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
status_bar.pack(side = tk.BOTTOM, fill = tk.X)



# Start main loop
app.mainloop()