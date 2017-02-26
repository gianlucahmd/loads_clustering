import os


def get_folders(root):
    return [folder for folder in os.listdir(root) if folder.startswith(".") == False]

def get_files(folder):
    return [file for file in os.listdir(folder) if file.endswith(".csv")]