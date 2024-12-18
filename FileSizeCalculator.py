import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

def list_files_and_folders_by_size(folder_path):
    items = []
    
    # Get files in the folder
    for f in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, f)):
            size = os.path.getsize(os.path.join(folder_path, f))
            items.append((f, size, 'file'))
    
    # Add folders and their sizes
    for f in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, f)):
            folder_size = get_folder_size(os.path.join(folder_path, f))
            print(f"Folder {f} is being calculated... Size: {folder_size / (1024**3):.2f} GB")
            items.append((f, folder_size, 'folder'))
    
    # Sort files and folders by size (largest to smallest)
    items.sort(key=lambda x: x[1], reverse=True)
    
    # Print the list
    print("\nResults (Sizes are shown in GB):")
    print("Name".ljust(50), "Size (GB)", "Type")
    print("-" * 70)
    
    for name, size, item_type in items:
        size_in_gb = size / (1024**3)
        print(name.ljust(50), f"{size_in_gb:.2f}", item_type)

if __name__ == "__main__":
    Tk().withdraw()  # Hide Tkinter window

    while True:
        # Ask user to select a folder
        folder_path = askdirectory(title="Please select a folder")
        
        if folder_path:
            print(f"\nSelected Folder: {folder_path}")
            list_files_and_folders_by_size(folder_path)
        else:
            print("No folder selected!")

        # Ask if the user wants to recalculate
        user_input = input("Press 'r' to recalculate. Press any other key to exit: ").lower()

        if user_input != 'r':
            print("Exiting the program...")
            break
