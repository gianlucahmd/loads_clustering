import pandas as pd
from building_func import get_building_kind, get_building_state, get_building_city
from make_building_model import make_building_model
from get_peaks import get_peaks


def make_building_feats(file, season = "", days = "all"):
    building_model = make_building_model(file, season = season, days = days)
    
    if "Electricity:Facility [kW](Hourly)" in building_model.columns:
        electricity_cons = building_model["Electricity:Facility [kW](Hourly)"]
        measure = "kW"
    elif "Electricity:Facility [J](Hourly)" in building_model.columns:
        electricity_cons = building_model["Electricity:Facility [J](Hourly)"]
        measure = "J"
        
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
                              "measure" : measure,
                              "file_path" : file,
                             }
    electricity_cons_dict = dict(zip(
            (str(i) for i in range(0, 24)),
            electricity_cons_scaled
        ))

    return dict(electricity_cons_dict, **building_features_dict)