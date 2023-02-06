import pickle
import json
__locations =None
__data_columns=None
__model=None

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations
    global __data_columns

    with open("C:/Users/Dinesh/OneDrive/Documents/Projects_Portfolio/Property_Price_Prediction/Server/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations=__data_columns[3:]
    
    with open("C:/Users/Dinesh/OneDrive/Documents/Projects_Portfolio/Property_Price_Prediction/Server/artifacts/property_price_prediction.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())