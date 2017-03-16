import matplotlib
import matplotlib.pyplot as plt
from make_df import make_df
from calendar_funcs import get_workdays, get_all_days, get_not_workdays

def plot_range(path, start_date, end_date, **kwargs):
    df = make_df(path)
    
    workdays = get_workdays(start_date, end_date)
    all_days = get_all_days(start_date, end_date)
    not_workdays = get_not_workdays(start_date, end_date)
    
    for day in all_days:
        plt.subplot(131)
        plt.plot(df[day].index.hour,
                 df[day]['Electricity:Facility [kW](Hourly)'], color=(0,0,0,0.1))
        plt.xlim([0, 23])
    plt.xlabel("Hour of the day")
    plt.ylabel("Load profile")
    
    for day in workdays:
        plt.subplot(132)
        plt.plot(df[day].index.hour,
                 df[day]['Electricity:Facility [kW](Hourly)'], color=(0,0,0,0.1))
        plt.xlim([0, 23])
        plt.xlabel("Hour of the day")
        plt.ylabel("Load profile")

    plt.title(path.split("/")[-1] + " (all, working, weekends)", fontsize = 20)
    
    for day in not_workdays:
        plt.subplot(133)
        plt.plot(df[day].index.hour,
                 df[day]['Electricity:Facility [kW](Hourly)'], color=(0,0,0,0.1))
        plt.xlim([0, 23])
        plt.xlabel("Hour of the day")
        plt.ylabel("Load profile")

    if "output_folder" in kwargs: 
        save_path = folder + kwargs["output_folder"]
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(save_path + "/" + file_input.split(".")[0] + "_loads.png")
        
    plt.rcParams["figure.figsize"] = (50,8)
    
    return plt.show()

def plot_day(df, days, line_color="blue"):
    for day in days:
        plt.plot(df[day].index.hour,
                         df[day]['Electricity:Facility [kW](Hourly)'], color = line_color)
        plt.xlim([0, 23])
        plt.xlabel("Hour of the day")
        plt.ylabel("Load profile")
        
    plt.show()