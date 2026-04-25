from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create folder if not exists
os.makedirs("app/models", exist_ok=True)

# Dummy data
X = [[1, 2], [2, 3], [3, 4], [5, 6]]
y = [0, 0, 1, 1]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "app/models/model32.pkl")

print("Model saved at app/models/model32.pkl")