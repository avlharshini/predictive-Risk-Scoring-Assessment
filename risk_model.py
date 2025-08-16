from sklearn.ensemble import IsolationForest
import numpy as np

# Example training data (you should use your real dataset instead)
training_data = np.array([
    [2, 9, 0],
    [8, 12, 3],
    [1, 14, 0],
    [10, 22, 5],
    [3, 11, 1]
])

# Initialize and train the Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(training_data)

# Function to predict risk
def predict_risk(user_data):
    try:
        features = np.array([
            user_data['failed_logins'],
            user_data['login_hour'],
            user_data['sensitive_file_accesses']
        ]).reshape(1, -1)
        
        prediction = model.predict(features)[0]
        return 1 if prediction == -1 else 0  # 1 = risky, 0 = normal
    except KeyError as e:
        print(f"Missing key in input: {e}")
        return None
