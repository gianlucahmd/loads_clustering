import pandas as pd
from explorer import get_files, get_folders, get_subroots, count_files
from make_building_feats import make_building_feats
import progressbar


def make_buildings_dataset(root, season = "", days = "all"):
    buildings_feats = pd.DataFrame()
    subroots = get_subroots(root)
    bar = progressbar.ProgressBar(maxval=count_files(root), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    i=0
    
    for subroot in subroots:
#        print(subroot)
        for folder in get_folders(root + subroot):
#            print(folder)
            for file in get_files(root + subroot + folder):
                bar.update(i)
                i+=1
    
                row = make_building_feats(root + subroot + folder + file)
                buildings_feats = buildings_feats.append(row, ignore_index = True)

    print("DONE")
    return buildings_feats