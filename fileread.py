import os

def list_files_and_directories(folder_path):
    with os.scandir(folder_path) as entries:
        for entry in entries:
            print(entry.name)

folder_path = 'your_folder_path_here'
list_files_and_directories(folder_path)


import os

def list_files_and_directories(folder_path):
    with os.scandir(folder_path) as entries:
        for entry in entries:
            print(entry.name)

folder_path = 'D:/'
list_files_and_directories(folder_path)

