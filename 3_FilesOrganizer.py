import os
import shutil

def organize_files(source_directory, destination_directory):
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

        # Move the file to the destination directory
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination_path)

    print("File organization completed successfully.")

# Example usage:
source_directory = r"C:\Users\vmirzac\OneDrive - ENDAVA\Desktop\AutomationBoringStuffWithPython\3_FilesOrganizer\SourceFolder"
destination_directory = r"C:\Users\vmirzac\OneDrive - ENDAVA\Desktop\AutomationBoringStuffWithPython\3_FilesOrganizer\DestinationFolder"

organize_files(source_directory, destination_directory)