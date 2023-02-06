import pickle
import json
import numpy as np
__locations =None
__data_columns=None
__model=None


def get_estimated_price(location, Total_Area, bhk, Baths):
    try:    
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    
    x=np.zeros(len(__data_columns))
    x[0]=Total_Area
    x[1]=bhk
    x[2]=Baths
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations
    global __data_columns

    with open("artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations=__data_columns[3:]
    
    global __model
    with open("artifacts/property_price_prediction.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Attibele Bangalore', 1800, 4, 4))