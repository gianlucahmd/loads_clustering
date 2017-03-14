from explorer import get_folders, get_files, get_subroots


files = []
root = "RESIDENTIAL/"
for subroot in get_subroots(root):
    for folder in get_folders(root + subroot):
        for file in get_files(root + subroot + folder):
            files.append(file)