import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv("diabetes.csv")
X, y = df.drop("Outcome", axis=1), df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

m = KNeighborsClassifier(n_neighbors=5)
m.fit(X_train, y_train)
p = m.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, p))
print("Accuracy:", accuracy_score(y_test, p))
print("Error Rate:", 1 - accuracy_score(y_test, p))
print("Precision:", precision_score(y_test, p, zero_division=0))
print("Recall:", recall_score(y_test, p, zero_division=0))