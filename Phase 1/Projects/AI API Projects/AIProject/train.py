from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

data=load_iris()

x=data.data
y=data.target

model= RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(x,y)

joblib.dump(model,'iris_model.pkl')
joblib.dump(data.target_names,'iris_classes.pkl')

print("Model Saved Sucessfully")