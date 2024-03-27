import pandas
from sklearn import linear_model

data = pandas.read_csv('data.csv')

xArray = data[['Weight', 'Volume']]
yArray = data['CO2']

regression = linear_model.LinearRegression()
regression.fit(xArray, yArray)

predictionCO2 = regression.predict([[3300, 1300]])

print(predictionCO2)
print(regression.coef_) #1kg/1cm³ erhöhung -> Steigerung um den Koeffizienten des Ergebnisses

