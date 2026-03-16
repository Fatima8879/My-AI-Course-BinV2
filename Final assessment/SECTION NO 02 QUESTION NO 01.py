'PROJECT: South Korean Air Pollution Analysis'
'DATASET: Air Quality (PM2.5, PM10, O3, NO2) & Weather Data'
'GOAL: To analyze pollution trends, correlations between pollutants, and the impact of meteorological factors on air quality in South Korea.'
'AUTHOR: Fatima Ali'
"DATE: March 2026"



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Bidirectional, GRU
from keras.optimizers import Adam
from keras.metrics import Precision, Recall

data=pd.read_csv('c:\GitHub\My-AI-Course-BinV2\Final assessment\south-korean-pollution-data.csv')

'-------Basic Functions--------'
# printing first 5 columns 
print(data.head())

#shape 
print("data.shape: \n" , data.shape)

#To find data type of column
print('Column dtype:', data.dtypes)

# drop unwanted column 
df = data.drop(columns=['Unnamed: 0'])

#description
print("data.describe().round(2).T:    \n",data.describe().round(2).T)

#columns in dataset
print('column of the data:', df.columns)


'----------data cleaning---------'
#The percentage of missing values 
print('Missing Values:', df.isnull().mean()*100)



#The percentage of duplicated values 
print('Duplicated Values:', df.duplicated().sum())

data['date']=pd.to_datetime(data['date'])
data['year'] = pd.to_datetime(df['date']).dt.year
data['month'] = pd.to_datetime(df['date']).dt.month

'----------ANALYZING DATA----------'

# DISTRIBUTION OF POLLUTION
plt.figure(figsize=(10, 5))
sns.histplot(data['pm25'], kde=True, color='red')
plt.title('PM2.5 Levels of Distribution')
plt.xlabel('PM2.5 Concentration')
plt.show()

#  CITY-WISE ANALYSIS 
plt.figure(figsize=(12, 6))
city_avg = data.groupby('City')['pm25'].mean().sort_values(ascending=False)
city_avg.plot(kind='bar', color='skyblue')
plt.title('Average PM2.5 Levels by City')
plt.ylabel('Average PM2.5')
plt.show()



# TIME TRENDS (Line Graph)
plt.figure(figsize=(14, 6))
data_daily = data.groupby('date')['pm25'].mean().reset_index()
plt.plot(data_daily['date'], data_daily['pm25'], marker='o', linestyle='-', color='purple')
plt.title('Daily PM2.5 Levels Trend')
plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In Which Year South Korea have most air Pollution
year = data.groupby('year').max()['pm25'].sort_values(ascending=False)
print(year)


#In which city of south korea have most pollution in 2019 because it's the most polluted year
year_most_pollution = data[data['year'] == 2019]
most_polluted_city = year_most_pollution.groupby('City').max()['pm25'].sort_values(ascending=False)
print(most_polluted_city)

#AIR QUALITY INDEX
city_pollution = data.groupby('City')['pm25'].mean().sort_values()
print("Average PM2.5 by City:\n", city_pollution)

#Correlation HEATMAP(Pollutants RELATIONS WITH EACH OTHER)
pollutants = ['pm25', 'pm10', 'o3', 'no2', 'so2', 'co']
corr_matrix = df[pollutants].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu')
plt.title('Correlation between different Pollutants')
plt.show()

'-------------LTSM MODEL------------------'
pm25 = data['pm25'].astype(int).values.reshape(-1, 1)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(pm25)

window_size = 12
X = []
y = []
target_values = data.index[window_size:]

for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i - window_size:i, 0])
    y.append(scaled_data[i, 0])

X = np.array(X)
y = np.array(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test, train_values, test_values = train_test_split(
    X, y, target_values, test_size=0.1, shuffle=False
)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))


model = Sequential()
model.add(LSTM(units=128, return_sequences=True,
          input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_predictions = scaler.inverse_transform(train_predictions).flatten()
test_predictions = scaler.inverse_transform(test_predictions).flatten()
y_test = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

from sklearn.metrics import r2_score
rmse = np.sqrt(np.mean((y_test - test_predictions)**2))
print(f'RMSE: {rmse:.2f}')

from sklearn.metrics import r2_score
r2_score = r2_score(y_test,test_predictions)
print(r2_score)

plt.figure(figsize=(12, 6))
plt.plot(test_values, y_test, label='Actual Values')
plt.plot(test_values, test_predictions, label='Predicted Values')
plt.title('Actual vs Predicted Values')
plt.xlabel('date')
plt.ylabel('pm25')
plt.legend()
plt.show()

# Plot predictions
plt.figure(figsize=(10, 6))

# Plot actual data
plt.plot(df.index[window_size:], df['pm25'][window_size:], label='Actual', color='blue')

# Plot training predictions
plt.plot(df.index[window_size:window_size+len(train_predictions)], train_predictions, label='Train Predictions',color='green')

# Plot testing predictions
test_pred_index = range(window_size+len(train_predictions), window_size+len(train_predictions)+len(test_predictions))
plt.plot(df.index[test_pred_index], test_predictions, label='Test Predictions',color='orange')

plt.title('South Korea Pollution Time Series Forecasting')
plt.xlabel('date')
plt.ylabel('pm25')
plt.legend()
plt.show()

forecast_period = 15
forecast = []

# Use the last sequence from the test data to make predictions
last_sequence = X_test[-1]

for _ in range(forecast_period):
    # Reshape the sequence to match the input shape of the model
    current_sequence = last_sequence.reshape(1, window_size, 1)
    # Predict the next value
    next_prediction = model.predict(current_sequence)[0][0]
    # Append the prediction to the forecast list
    forecast.append(next_prediction)
    # Update the last sequence by removing the first element and appending the predicted value
    last_sequence = np.append(last_sequence[1:], next_prediction)

# Inverse transform the forecasted values
forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))
print(forecast)
# Plot the forecasted values
plt.figure(figsize=(10, 6))
plt.plot(df.index[-len(pm25):], scaler.inverse_transform(pm25), label='Actual')
plt.plot(pd.date_range(start=df.index[-1], periods=forecast_period, freq='M'), forecast, label='Forecast')
plt.title('South Korea Pollution (30-day Forecast)')
plt.xlabel('date')
plt.ylabel('pm25')
plt.legend()
plt.show()

'--------------Gated Recurrent Unit (GRU)-----------------'

data = pd.read_csv('south-korean-pollution-data.csv')
print(data.head())

data['date'] = pd.to_datetime(data['date'])

data = data[['date','pm25']]
data.set_index('date',inplace=True)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data.values)

def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0]) 
        y.append(data[i + time_step, 0]) 
    return np.array(X), np.array(y)

time_step = 100 
X, y = create_dataset(scaled_data, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)

model1 = Sequential()
model1.add(GRU(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model1.add(GRU(units=50))


model1.add(Dense(units=1)) 

METRICS = metrics=['accuracy', 
                   Precision(name='precision'),
                   Recall(name='recall')]

model1.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error', metrics = METRICS)


model1.fit(X, y, epochs=10, batch_size=32)


input_sequence = scaled_data[-time_step:].reshape(1, time_step, 1)
predicted_values = model1.predict(input_sequence)


predicted_values = scaler.inverse_transform(predicted_values)
print(f"The predicted pm25 for the next day is: {predicted_values[0][0]:.2f}")

'-----------DUMP LTSM MODEL--------------'

import pickle
pickle.dump(data,open('df.pkl','wb'))
pickle.dump(model,open('model.pkl','wb'))














