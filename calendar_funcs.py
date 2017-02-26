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


def get_workdays(start_date, end_date):
    days = pd.DatetimeIndex(start = start_date, end = end_date, freq = CDay(calendar = cal))
    return list(days.strftime('%Y-%m-%d'))

def get_all_days(start_date, end_date):
    days = pd.date_range(start_date,end_date)
    return list(days.strftime('%Y-%m-%d'))

def get_not_workdays(start_date, end_date):
    workdays = pd.DatetimeIndex(start = start_date, end = end_date, freq = CDay(calendar = cal))
    all_days = pd.date_range(start_date,end_date)
    days = all_days - workdays    
    return list(days.strftime('%Y-%m-%d'))
