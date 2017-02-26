import pandas as pd
import datetime


def make_df(path):
    df = pd.read_csv(path)
    
    #add year and change midnight from 24 to 00 as pandas wants
    df["Date/Time"] = "2004/" + df["Date/Time"].str.replace("24:","00:").str.replace(" ","")
    df["Date/Time"] = pd.to_datetime(df["Date/Time"], format ="%Y/%m/%d%H:%M:%S")
    
    #remove only datapoint of 2005 and use it to fill missing datapoint of 2004-1-1 at midnight
    df.set_index("Date/Time", inplace=True)
    
    #set time = 0 as first hour of next day
    df.index += pd.to_timedelta((df.index.hour == 0) * datetime.timedelta(days=1))
    
    #fix problem with 29 of February
    df.index += pd.to_timedelta(((df.index.day == 29) & (df.index.month == 2)) * datetime.timedelta(days=1))
    
    #make last row the first
    first_row = df.ix[[-1]]
    first_row.index -= pd.to_timedelta(datetime.timedelta(days=366))
    df = pd.concat([first_row, df.ix[0:-1]])
    
    #fix daylight time shifts and make dataset consistent 
    # Daylight Saving Time starts the 12 of March and ends the 5 of november
    df = pd.concat([df[:"2004-03-11"],
                 df["2004-03-12":"2004-11-5"].shift(1),
                 df["2004-11-6":]])
    df.fillna(method="bfill",inplace=True)
    
    # ATTENTION! the dataset is all shifted by 4 days, in fact by doing that you 
    # can see that on weekends energy demand is lower, as well as on public holidays
    # (check Martin Luther king day on January 19)
    df = df.shift(3 * 24)

    return df.dropna(axis = 1, how = "all").dropna(how = "all")  