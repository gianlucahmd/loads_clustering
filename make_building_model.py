import pandas as pd
import numpy as np
from sklearn.preprocessing import minmax_scale

from make_df import make_df
from make_calendar_df import get_business_df, get_not_working_df


def make_building_model(folder, file, **optional):
    df = make_df(folder + file)
    if optional:
        if optional["days"] == "business":
            df = get_business_df(df)
        elif optional["days"] == "not_working":
            df = get_not_working_df(df)
            
    building_model=  pd.DataFrame(columns = df.columns.tolist(),
                                  index = range(0,24))
    
    for column in df.columns.tolist():
        for hour in range(0,24):
            building_model.loc[hour, column] = df.loc[df.index.hour == hour,column].mean()
        building_model[column] = minmax_scale(np.float64(building_model[column].values))
    
    return building_model