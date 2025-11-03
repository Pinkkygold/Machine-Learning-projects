import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.model_selection import train_test_split
import joblib 


data = pd.read_csv('/Users/awabe/Documents/ML foundation to Advance/Certisured course/Machine Learning/HappinessIndex/income.data.csv').drop('Unnamed: 0', axis=1) 
data.head() 



X = data[['income']]
y = data['happiness'] 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

#Intializing the model
model = LinearRegression() 
model.fit(X_train, y_train) 

#Pred
y_pred = model.predict(X_test) 


mse = mean_squared_error(y_test, y_pred) 
r2 = r2_score(y_test, y_pred) 


print(f"The Squared mean error (MSE): {mse: .2f}")
print(f"R-Squared (R): {r2: .4f}") 


#Saving the model 
joblib.dump(model, 'linear_regression_model.pkl') 
