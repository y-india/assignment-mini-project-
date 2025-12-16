
import joblib
import numpy as np



model = joblib.load("LogisticRegression.pkl")





# Age,Income (in 1000s),Credit Score,Loan Amount (in 1000s),Approved
x_new = [[24,45,700,22]]

x2_new = [[55,45,400,60]]


prediction = model.predict(x_new)
prediction_2 = model.predict(x2_new)


print(f"prediction 1 is {prediction}")

print(f"prediction 2 is {prediction_2}")