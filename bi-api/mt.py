import pickle 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv('btc_done.csv')


with open('model_1.pickle', 'rb') as f: 
    model = pickle.load(f)

X_train, X_test, y_train, y_test = train_test_split(df['0'], df['answer'].to_numpy(), test_size=0.2, random_state=2)

print(model.score(X_test,y_test))
print(model.predict(my['aabb']))