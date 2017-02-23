import pandas as pd
import datetime
from pandas.tseries.offsets import CDay
from pandas.tseries.holiday import Holiday, USFederalHolidayCalendar, USColumbusDay, USMemorialDay, AbstractHolidayCalendar


class WorkCalendar(AbstractHolidayCalendar):
    rules = [
        USMemorialDay,
        USColumbusDay
        ] + USFederalHolidayCalendar.rules
    
WorkCalendar.start_date = datetime.date(2004,1,1)
WorkCalendar.start_date = datetime.date(2004,12, 31)
    
cal = WorkCalendar()

def get_workdays(df, start_date, end_date):
    return pd.DatetimeIndex(start = start_date, end = end_date, freq = CDay(calendar = cal))

def get_all_days(df, start_date, end_date):
    return pd.date_range(start_date,end_date)

def get_not_workdays(df, start_date, end_date):
    workdays = get_workdays(df, start_date, end_date)
    all_days = get_all_days(df, start_date, end_date)
    return all_days - workdays    