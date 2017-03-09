import pandas as pd
import numpy as np
from sklearn.preprocessing import minmax_scale

import seasons
from make_df import make_df
from make_calendar_df import get_business_df, get_not_working_df


def make_building_model(file, days = "all", season = ""):
    df = make_df(file)

    if days == "business":
        df = get_business_df(df)
    elif days == "not_working":
        df = get_not_working_df(df)

    if season == "summer":
        df = df[seasons.summer_start : seasons.summer_end]
    elif season == "spring":
        df = df[seasons.spring_start : seasons.spring_end]
    elif season == "autumn":
        df = df[seasons.autumn_start : seasons.autumn_end]
    elif season == "winter":
        df = pd.concat([df[:seasons.winter_end], df[seasons.winter_start:]])

    building_model=  pd.DataFrame(columns = df.columns.tolist(),
                                  index = range(0,24))
    
    for column in df.columns.tolist():
        for hour in range(0,24):
            building_model.loc[hour, column] = df.loc[df.index.hour == hour,column].mean()
        #building_model[column] = minmax_scale(np.float64(building_model[column].values))
    
    return building_model