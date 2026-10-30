import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("data.csv")
df = pd.get_dummies(df.drop(columns=["RowNumber", "CustomerId", "Surname"]),
                    drop_first=True)

X = df.drop("Exited", axis=1)
y = df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

m = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300,
                  early_stopping=True, random_state=42)
m.fit(X_train, y_train)
p = m.predict(X_test)

print("Accuracy:", accuracy_score(y_test, p))
print("Confusion Matrix:\n", confusion_matrix(y_test, p))