import tkinter as tk
from tkinter import filedialog
from shutil import copyfile
import os
from main import *


# Set Styling
font_style_title = ("Helvetica", 16)
font_style_body  = ("Helvetica", 10)

# Set BOM Directory
directory = "C:\\Users\\Tyler\\Desktop\\PushPin GUI\\BOM_Directory"

# Function for Selecting Files
def open_file_dialog():
    global files_to_save
    file_paths = filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = [
            ("Excel Files", "*.xls;*.xlsx"), 
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ]
    )
    files_to_save = list(file_paths)
    num_files = len(file_paths)
    if files_to_save:
        file_counter.config(text = f"Selected Files: {num_files}")
    create_listbox(file_listbox, files_to_save)
    upload_button.pack_forget()
    
# Function for Creating File Listbox
def create_listbox(listbox, file_paths):
    file_listbox.pack(pady=5)
    for file_path in file_paths:
        listbox.insert(-1, os.path.basename(file_path))
        delete_button.pack(pady=5)
    
# Function for Deleting Files from Listbox
def delete_file_from_listbox(listbox):
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index[0])
        del files_to_save[selected_index[0]-1]
        num_files = len(files_to_save)
        file_counter.config(text = f"Selected Files: {num_files}")

# Function for Updating Listbox
def update_listbox(listbox, file_paths):
    listbox.delete(0, -1)
    for file_path in file_paths:
        listbox.insert(-1, os.path.basename(file_path))

# Function for Submitting Files
def save_files():
    app.destroy()
    main(files_to_save)

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
upload_button = tk.Button(frame, text = "Select BOM(s)", font = font_style_body, command = open_file_dialog, relief = tk.RAISED, borderwidth=2)
upload_button.pack(pady=10)

# Create Listbox
file_listbox = tk.Listbox(frame, selectmode = tk.SINGLE, font = font_style_body)

# Create Delete Button for Listbox
delete_button = tk.Button(frame, text = "X", command = lambda:delete_file_from_listbox(file_listbox))

# Add save button
save_button = tk.Button(frame, text = "Submit", command = save_files)
save_button.pack(pady=10)

# Label to display selected file path
file_counter = tk.Label(frame, text = "Selected Files: None", font = font_style_body)
file_counter.pack(pady=3)



# Start main loop
app.mainloop()
