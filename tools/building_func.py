def get_building_kind(filename):
    if "RefBldg" in filename:
        return filename.split(str(2004))[0].split("RefBldg")[1]
    else:
        return "residential"

def get_building_state(filename):
    return filename.split("USA_")[1].split("_")[0]

def get_building_city(filename):
    if "RefBldg" in filename:
        return filename.split(get_building_state(filename))[1][1:-4]
    else:
        return ", ".join(filename.split("_")[2].split(".")[0:-2])