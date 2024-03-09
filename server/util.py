import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_idx=__data_columns.index(location.lower())
    except:
        loc_idx=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if(loc_idx>=0):
        x[loc_idx]=1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations
def load_saved_artifacts():
    print("Loading Saved Artifacts start")
    global __data_columns
    global __locations
    global __model
    with open(r"C:\Users\sumit\Desktop\Code\python\Machine Learning\project\Bangalore house Price Prediction\server\artifacts\columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]
    
    with open(r"C:\Users\sumit\Desktop\Code\python\Machine Learning\project\Bangalore house Price Prediction\server\artifacts\banglore_home_price_model.pickle",'rb') as f:
        __model=pickle.load(f)
    print("Loading Saved Artifacts Done")

if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
    print(get_estimated_price('Kalhalli',1000,2,2))
    print(get_estimated_price('Ejipura',1000,2,2))