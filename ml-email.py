import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("data.csv").dropna()
X = df["text"]
y = df["spam"]

X = TfidfVectorizer().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

for m in [KNeighborsClassifier(), SVC()]:
    m.fit(X_train, y_train)
    p = m.predict(X_test)
    print(type(m).__name__)
    print("Accuracy:", accuracy_score(y_test, p))
    print("Confusion Matrix:\n", confusion_matrix(y_test, p))