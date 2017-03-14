import matplotlib
import matplotlib.pyplot as plt
from make_df import make_df
from calendar_funcs import get_workdays, get_all_days, get_not_workdays

def plot_range(folder, file_input, start_date, end_date, **kwargs):
    print(file_input)
    df = make_df(folder + file_input)
    
    workdays = get_workdays(start_date, end_date)
    all_days = get_all_days(start_date, end_date)
    not_workdays = get_not_workdays(start_date, end_date)
    
    for day in all_days:
        plt.subplot(131)
        plt.plot(df[day].index.hour,
                 df[day]['Electricity:Facility [kW](Hourly)'], color=(0,0,0,0.1))
    
    for day in workdays:
        plt.subplot(132)
        plt.plot(df[day].index.hour,
                 df[day]['Electricity:Facility [kW](Hourly)'], color=(0,0,0,0.1))
    
    plt.title(file_input + " (all, working, weekends)", fontsize = 30)
    
    for day in not_workdays:
        plt.subplot(133)
        plt.plot(df[day].index.hour,
                 df[day]['Electricity:Facility [kW](Hourly)'], color=(0,0,0,0.1))
        
    if "output_folder" in kwargs: 
        save_path = folder + kwargs["output_folder"]
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(save_path + "/" + file_input.split(".")[0] + "_loads.png")
        
    plt.rcParams["figure.figsize"] = (50,8)
    
    return plt.show()

def plot_day(df, days):
    for day in days:
        plt.plot(df[day].index.hour,
                         df[day]['Electricity:Facility [kW](Hourly)'])
    plt.show()