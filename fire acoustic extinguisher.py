import pandas as pd

df = pd.read_excel("c:/Users/LENOVO/Downloads/Acoustic_Extinguisher_Fire_Dataset/Acoustic_Extinguisher_Fire_Dataset\Acoustic_Extinguisher_Fire_Dataset.xlsx")

print(df.head())
print(df.info())
print(df.describe())
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.get_dummies(df,drop_first=True)
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("FIRE EXTINGUISHER Heatmap")
plt.show()

from sklearn.model_selection import train_test_split


X = df.drop('STATUS', axis=1) 
y = df['FREQUENCY']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

log_preds = log_model.predict(X_test)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, log_preds):.2%}")

from sklearn.tree import DecisionTreeClassifier


dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

dt_preds = dt_model.predict(X_test)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, dt_preds):.2%}")