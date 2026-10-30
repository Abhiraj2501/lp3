import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("data.csv").dropna()
df = df[(df.fare_amount > 0) & (df.passenger_count > 0)]
df = df[df.pickup_longitude.between(-180, 180) &
        df.dropoff_longitude.between(-180, 180) &
        df.pickup_latitude.between(-90, 90) &
        df.dropoff_latitude.between(-90, 90)]

q1, q3 = df.fare_amount.quantile([0.25, 0.75])
iqr = q3 - q1
out = (df.fare_amount < q1 - 1.5*iqr) | (df.fare_amount > q3 + 1.5*iqr)
print("Outliers:", out.sum())
df = df[~out]

print(df.select_dtypes("number").corr())

X = df[["pickup_longitude", "pickup_latitude", "dropoff_longitude",
        "dropoff_latitude", "passenger_count"]]
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

for m in [LinearRegression(), RandomForestRegressor(n_estimators=50, random_state=42)]:
    m.fit(X_train, y_train)
    p = m.predict(X_test)
    print(type(m).__name__,
          "R2:", r2_score(y_test, p),
          "RMSE:", np.sqrt(mean_squared_error(y_test, p)))