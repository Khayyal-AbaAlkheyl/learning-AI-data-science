# Import Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Download dataset from Kaggle
path = kagglehub.dataset_download("jayaantanaath/student-habits-vs-academic-performance")

# Load CSV file
df = pd.read_csv(f"{path}/student_habits_performance.csv")

# Separate Features and Target
target_column = "exam_score"

X = df.drop(target_column, axis=1)
y = df[target_column]

print("\nDataset Shapes")
print("X:", X.shape)
print("y:", y.shape)

#Encode categorical features
label_encoder=LabelEncoder()
for col in X.select_dtypes(include=['object']).columns:
    X[col] = label_encoder.fit_transform(X[col])

# Feature Scaling
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

#define model
model=LinearRegression()

#K-Fold Cross Validation
kfold=KFold(n_splits=5,shuffle=True,random_state=42)

mse_scores = []
mae_scores = []

for fold , (train_idx,test_idx) in enumerate (kfold.split(X_scaled)):
    X_train, X_test = X_scaled[train_idx], X_scaled[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    # Train model
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluation metrics
    mse_scores.append(mean_squared_error(y_test, y_pred))
    mae_scores.append(mean_absolute_error(y_test, y_pred))
# Print Evaluation Metrics
print("\nModel Evaluation Metrics (K-Fold)\n" + "-"*40)
print(f"MSE : {np.mean(mse_scores):.2f}")
print(f"MAE : {np.mean(mae_scores):.2f}")
print(f"RMSE: {np.sqrt(np.mean(mse_scores)):.2f}")
print("-"*40)

# Plot Predictions vs Ground Truth
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--",
    linewidth=2
)
plt.xlabel("Actual Exam Scores (Ground Truth)")
plt.ylabel("Predicted Exam Scores")
plt.title("Linear Regression: Predictions vs Ground Truth")
plt.grid(True)

plt.tight_layout()
plt.show()