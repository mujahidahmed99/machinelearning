import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('rf_model.pkl','rb'))

df = pd.read_csv('rndm_forest_fixtures.csv')

predictions = model.predict(df)

pred = pd.DataFrame(predictions, columns = ['Predictions'])
pred.to_csv('rf_predictions.csv', index=False)
pred.to_json("predictions_json.json", orient="columns")
print(predictions)
