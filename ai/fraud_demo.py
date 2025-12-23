import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

data = pd.DataFrame([
    {"tx_count_24h": 8,   "unique_counterparties": 2,  "price_volatility": 0.10, "is_fraud": 0},
    {"tx_count_24h": 12,  "unique_counterparties": 3,  "price_volatility": 0.15, "is_fraud": 0},
    {"tx_count_24h": 50,  "unique_counterparties": 30, "price_volatility": 0.85, "is_fraud": 1},
    {"tx_count_24h": 80,  "unique_counterparties": 45, "price_volatility": 0.90, "is_fraud": 1},
    {"tx_count_24h": 5,   "unique_counterparties": 1,  "price_volatility": 0.05, "is_fraud": 0},
    {"tx_count_24h": 120, "unique_counterparties": 60, "price_volatility": 0.95, "is_fraud": 1},
])

X = data[["tx_count_24h", "unique_counterparties", "price_volatility"]]
y = data["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42, stratify=y
)

model = RandomForestClassifier(random_state=42, n_estimators=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("=== Classification Report (POC) ===")
print(classification_report(y_test, y_pred))

accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

joblib.dump(model, "fraud_model.joblib")

sample = pd.DataFrame([{"tx_count_24h": 90, "unique_counterparties": 40, "price_volatility": 0.92}])
proba = model.predict_proba(sample)[0][1]
risk_score_0_100 = int(round(proba * 100))
print(f"Sample risk score (0-100): {risk_score_0_100}")