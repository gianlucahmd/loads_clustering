import os


def get_folders(root):
    return [folder + "/" for folder in os.listdir(root) if folder.startswith(".") == False]

def get_files(folder):
    return [file for file in os.listdir(folder) if file.endswith(".csv")]

def get_subroots(root):
    return [folder + "/" for folder in os.listdir(root) if 
            (folder.startswith(".") == False and folder.endswith(".tar.gz") == False)]

def count_files(root):
    i = 0
    for subroot in get_subroots(root):
        for folder in get_folders(root + subroot):
            for file in get_files(root + subroot + folder):
                i += 1
    return i