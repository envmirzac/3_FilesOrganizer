import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

def organize_files():
    # Prompt the user to select the source directory
    source_directory = filedialog.askdirectory(title="Select Source Directory")
    if not source_directory:
        return

    # Prompt the user to select the destination directory
    destination_directory = filedialog.askdirectory(title="Select Destination Directory")
    if not destination_directory:
        return

    # Iterate through all files in the source directory
    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(file_path)
        extension = extension[1:]  # Remove the leading dot

        # Create the destination directory based on the file extension
        destination_folder = os.path.join(destination_directory, extension)
        os.makedirs(destination_folder, exist_ok=True)

        # Copy the file to the destination directory
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy2(file_path, destination_path)

    messagebox.showinfo("File Organizer", "File organization completed successfully.")

def create_ui():
    window = tk.Tk()
    window.title("File Organizer")

    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the dimensions for the UI
    ui_width = screen_width * 3 // 4
    ui_height = screen_height * 3 // 4

    # Calculate the position for the UI to be centered
    x_position = (screen_width - ui_width) // 2
    y_position = (screen_height - ui_height) // 2

    # Set the window dimensions and position
    window.geometry(f"{ui_width}x{ui_height}+{x_position}+{y_position}")

    # Add background image
    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_image_path = os.path.join(current_dir, "briefcase.jpg")
    background_image = ImageTk.PhotoImage(Image.open(background_image_path).resize((ui_width, ui_height)))
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = tk.Label(window, text="Select source and destination directories to organize files.", font=("Arial", 12), bg="white")
    label.pack(pady=(ui_height // 4, 10), padx=20, fill="x")

    source_button = tk.Button(window, text="Select Source Directory", command=organize_files, font=("Arial", 12))
    source_button.pack(pady=10)

    destination_button = tk.Button(window, text="Select Destination Directory", command=organize_files, font=("Arial", 12))
    destination_button.pack()

    window.mainloop()

def main():
    create_ui()

if __name__ == "__main__":
    main()