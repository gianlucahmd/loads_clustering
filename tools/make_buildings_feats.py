import pandas as pd
from explorer import get_files, get_folders, get_subroots, count_files
from building_func import get_building_kind, get_building_state, get_building_city
from make_building_model import make_building_model
from get_peaks import get_peaks
import progressbar


def make_buildings_feats(root, season = "", days = "all"):
    buildings_feats = pd.DataFrame()
    subroots = get_subroots(root)
    bar = progressbar.ProgressBar(maxval=count_files(root), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    i=0
    
    for subroot in subroots:
        print(subroot)
        for folder in get_folders(root + subroot):
            print(folder)
            for file in get_files(root + subroot + folder):
                bar.update(i)
                i+=1
                
                building_model = make_building_model(root + subroot + folder, file, season = season, days = days)
                electricity_cons = building_model["Electricity:Facility [kW](Hourly)"]
                #electricity_cons_scaled = minmax_scale(np.float64(electricity_cons.values))
                electricity_cons_scaled = electricity_cons / electricity_cons.max()
                peaks = get_peaks(electricity_cons)

                building_features_dict = {"building_kind" : get_building_kind(file),
                                          "building_state" : get_building_state(file),
                                          "building_city" : get_building_city(file),
                                          "n_peaks" : peaks["number"],
                                          "time_peaks" : peaks["times"],
                                          "std_dev" : electricity_cons.std(),
                                          "consumption_max" : electricity_cons.max(),
                                          "consumption_avg" : electricity_cons.mean(),
                                          "highest_peak_time" : electricity_cons.idxmax(),
                                          "file_path" : file,
                                         }
                electricity_cons_dict = dict(zip(
                        (str(i) for i in range(0, 24)),
                        electricity_cons_scaled
                    ))

                row = dict(electricity_cons_dict, **building_features_dict)
                buildings_feats = buildings_feats.append(row, ignore_index = True)

    print("DONE")
    return buildings_feats