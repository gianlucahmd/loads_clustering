def get_building_kind(filename):
    return filename.split(str(2004))[0].split("RefBldg")[1]

def get_building_state(filename):
    return filename.split("USA_")[1].split("_")[0]

def get_building_city(filename):
    return filename.split(get_building_state(filename))[1][1:-4]