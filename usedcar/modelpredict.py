## Developed By Manaranjan Pradhan
## Used Car Price Prediction Model

import pandas as pd
import numpy as np
import joblib
import warnings
from io import BytesIO
import requests
warnings.filterwarnings('ignore')

model_path = 'https://github.com/manaranjanp/usedcarprice/blob/main/usedcar/carmodel.pkl?raw=true'
        
class UsedcarPricePredictor():
    
    class CarPredictionModel():
    
        def __init__(self, pipeline, all_features, cat_features, num_features, rmse):
            self.pipeline = pipeline
            self.all_features = all_features
            self.cat_features = cat_features
            self.num_features = num_features
            self.rmse = rmse
    
    def __init__(self):
        model_file = BytesIO(requests.get(model_path).content)
        self.model = joblib.load(model_file)
        
    def predict(self, 
                km_driven, 
                fuel_type,
                age,
                transmission,
                owner,
                seats,
                make,
                model,
                mileage,
                engine,
                power,
                location):
        
        car_data = {}
        
        car_data['KM_Driven'] = km_driven
        car_data['Fuel_Type'] = fuel_type
        car_data['age'] = age
        car_data['Transmission'] = transmission
        car_data['Owner_Type'] = owner
        car_data['Seats'] = seats
        car_data['make'] = make
        car_data['model'] = model        
        car_data['mileage_new'] = mileage
        car_data['engine_new'] = engine
        car_data['model'] = model
        car_data['power_new'] = power
        car_data['Location'] = location 
                
        df = pd.DataFrame(car_data, index = [0])
        
        return np.round(self.model.pipeline.predict(df)[0], 2)
