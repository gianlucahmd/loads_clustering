import pandas as pd
from calendar_funcs import get_workdays, get_not_workdays


def get_business_df(df):
    business_df = pd.DataFrame()
    workdays = get_workdays(str(df.ix[[1]].index.strftime('%Y-%m-%d')[0]), 
            str(df.ix[[-1]].index.strftime('%Y-%m-%d')[0]))
    for day in workdays:
        business_df = business_df.append(df[day])
    return business_df

def get_not_working_df(df):
    not_working_df = pd.DataFrame()
    workdays = get_not_workdays(str(df.ix[[1]].index.strftime('%Y-%m-%d')[0]), 
            str(df.ix[[-1]].index.strftime('%Y-%m-%d')[0]))
    for day in workdays:
        not_working_df = not_working_df.append(df[day])
    return not_working_df