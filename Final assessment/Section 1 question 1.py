#The code here in will attempt to provide an accurate prediction for the cost of insurance. 

"The independant variables: "
"age, sex, bmi (body mass index), children, smoker or non-smoker, and the region, will be used to predict the charge of the insurance."


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data=pd.read_csv("Section1-Question1-InsurranceData.csv")


#printing basic informations 

#head
print("data.head():  \n",data.head())

#shape
print("data.shape: \n" , data.shape)

#description
print("data.describe().round(2).T:    \n",data.describe().round(2).T)

#for additional information
print('info:', data.info())

#to find data type
print('dtypes:', data.dtypes)

#columns in csv file
print('Columns Names:', data.columns)

#print colume age
print(data['age'].max())

# Don't need to find values because not a single one is missing.

# Correlation Between Numerical Values Of Data
print('Correlation Between Numerical Values')
print(data.corr(numeric_only=True))


print('HeatMap To see The Graphical Represention of Correlation Between Numerical Values')

sns.heatmap(data.corr(numeric_only=True),annot=True,linewidth=2,square=2,fmt='.1f')
plt.show()



categorical_columns = [var for var in data.columns if data[var].dtypes == 'object']
numerical_columns = [var for var in data.columns if data[var].dtypes != 'object']



X = data[['age','bmi','children','charges']]



#  DATA ANALYSIS

variables = ['age','bmi','children']
for var in variables:
    plt.figure()
    sns.regplot(x=var, y='charges', data=data).set(title=f'Regression plot of {var} and Charges');
    plt.show()



# graphical represntation of column 'region'
print('unique values of columns region:',data['region'].nunique())
print('Value Counts of region:',data['region'].value_counts())

print(data['region'].value_counts())
sns.countplot(data,x='region')
plt.xticks(rotation=75,fontsize=7)
plt.show()


#piechart of dataset
plt.pie(data['region'].value_counts(),labels=['southwest','northeast','southeast','northwest'],autopct='%1.f%%',pctdistance=0.85,explode=(0.2,0,0,0))
centre_circle = plt.Circle((0,0),0.75,fc='white')


# graphical represntation of column 'smoker'
print(data['smoker'].value_counts())
sns.countplot(data,x='smoker')
plt.xticks(rotation=75,fontsize=7)
plt.show()


# Charges distribution all over dataset
plt.figure(figsize=(8,4))
sns.histplot(data['charges'], kde=True, color='blue')
plt.title("Insurance Charges Distribution")
plt.show()
 
#  Graphical Representation of Dataset Using Seaborn 
import plotly.express as px
import plotly.io as pio

# Region wise distribution
sns.countplot(x='region', data=data, palette='viridis')
plt.title("Region-wise data count")
plt.show()


# Let's find the reltionship between dependent and independent variables

g = sns.scatterplot(data=data,x='bmi',y='charges', hue='sex')
g.figure.suptitle("scatterplot")
g.figure.show()


# showing graphics of column 'sex'
print(data['sex'].value_counts())
sns.countplot(data,x='sex')
plt.xticks(rotation=75,fontsize=7)
plt.show()


'---------------Machine Learning------------'


X = data.drop('charges',axis=1)
Y = data['charges']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.20,random_state=42)


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#
Lr = LinearRegression()
Decision_Tree = DecisionTreeRegressor(criterion='squared_error',splitter='best',max_depth=2,)
Random_Forest = RandomForestRegressor()
GradientBoosting_Regressor = GradientBoostingRegressor(loss='squared_error',max_depth=2,learning_rate=0.1)

preprocessor = ColumnTransformer([
    ('ohe',OneHotEncoder(drop='first',sparse_output=False,handle_unknown='ignore'),['sex','smoker','region'])
],remainder='passthrough')






# use the Randomized Search CV to get the best Parameters to acieve higher accuracy


# Random Forest Regressor Regressor Model

from sklearn.model_selection import RandomizedSearchCV
max_depth = [1,2,4,5,7,10,20,30,40,50,100,150,200,250,300]
n_estimators = [1,2,4,5,6,7,10,20,30,40,50,100,150,200]
criterion = ['squared_error']

param_grid = {'max_depth':max_depth,
              'n_estimators':n_estimators,
              'criterion':criterion}
rfr_grid = RandomizedSearchCV(Random_Forest,param_grid,cv=5,verbose=2)

RandomForest_pipe = Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('rfr_grid',rfr_grid)
])

RandomForest_pipe.fit(X_train,y_train)
predictions = RandomForest_pipe.predict(X_test)

# Accuracy of Random Forest Regressor by using RandomizedSearchCV

print('Accuracy for Random Forest Regressor')

mae = mean_absolute_error(y_test,predictions)
mse = mean_squared_error(y_test,predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,predictions)

print(f'mean absolute error: {mae:.2f}')
print(f'mean squared error: {mse:.2f}')
print(f'root mean squared error: {rmse:.2f}')
print(f'r2 score: {r2:.2f}')


# Linear Regression
pipe1 = Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('linearRegression',Lr)
])


# Decision Tree
pipe2 = Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('DecisionTreeRegressor',Decision_Tree)
])




# Gradient Boosting Regressor
pipe4 = Pipeline(steps=[
    ('preprocessor',preprocessor),
    ('Gradient Boosting Regressor',GradientBoosting_Regressor)
])


pipe1.fit(X_train,y_train)
pipe2.fit(X_train,y_train)
pipe4.fit(X_train,y_train)


y_pred = pipe1.predict(X_test)
y_pred1 = pipe2.predict(X_test)
y_pred4 = pipe4.predict(X_test)

# Accuracy for linear Regression

mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred)

print('Accuracy For Linear Regression')

print(f'mean absolute error: {mae:.2f}')
print(f'mean squared error: {mse:.2f}')
print(f'root mean squared error: {rmse:.2f}')
print(f'r2 score: {r2:.2f}')


#  To find Accuracy for Decision Tree
print('Accuracy For Decision tree')

mae = mean_absolute_error(y_test,y_pred1)
mse = mean_squared_error(y_test,y_pred1)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred1)

print(f'mean absolute error: {mae:.2f}')
print(f'mean squared error: {mse:.2f}')
print(f'root mean squared error: {rmse:.2f}')
print(f'r2 score: {r2:.2f}')




print('Accuracy For Gradient Boosting Regressor')

mae = mean_absolute_error(y_test,y_pred4)
mse = mean_squared_error(y_test,y_pred4)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred4)

print(f'mean absolute error: {mae:.2f}')
print(f'mean squared error: {mse:.2f}')
print(f'root mean squared error: {rmse:.2f}')
print(f'r2 score: {r2:.2f}')



import pickle

# saving data by  Gradient Boosting because it shows good results
pickle.dump(pipe4, open('insurance_model.pkl', 'wb'))
print("\nModel saved successfully!")










