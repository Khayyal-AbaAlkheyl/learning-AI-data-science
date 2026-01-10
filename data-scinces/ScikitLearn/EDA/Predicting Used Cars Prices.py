import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import kagglehub

from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

import warnings
warnings.filterwarnings('ignore')

##Read the data 

#download latest version of kaggle 
path = kagglehub.dataset_download("austinreese/craigslist-carstrucks-data")
print("Path to dataset files:", path)

# Load the dataset
cars_path = os.path.join(path, 'vehicles.csv')
df_cars = pd.read_csv(cars_path)

print(f"Dataset shape: {df_cars.shape}")
print(df_cars.head())


# Check data types and structure
print(df_cars.info())

# Analyze missing values
missing_percentage = (df_cars.isnull().sum() / len(df_cars)) * 100
missing_data = pd.DataFrame({
    'Column': missing_percentage.index,
    'Missing_Percentage': missing_percentage.values
})
missing_data = missing_data[missing_data['Missing_Percentage'] > 0].sort_values('Missing_Percentage', ascending=False)

print("Missing Data Analysis:")
print(missing_data.head(10))

# Descriptive statistics for numerical columns
print(df_cars.describe())


# Price distribution (target variable)
plt.figure(figsize=(10, 5))
plt.hist(df_cars['price'].dropna(), bins=50, edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Condition distribution
condition_counts = df_cars['condition'].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(condition_counts.index, condition_counts.values, color='coral')
plt.title('Condition Distribution')
plt.xlabel('Condition')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Transmission distribution
transmission_counts = df_cars['transmission'].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(transmission_counts.index, transmission_counts.values, color='teal')
plt.title('Transmission Distribution')
plt.xlabel('Transmission Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Year distribution
plt.figure(figsize=(10, 5))
plt.hist(df_cars['year'].dropna(), bins=30, edgecolor='black', color='orange')
plt.title('Year Distribution')
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.show()

# Odometer distribution
plt.figure(figsize=(10, 5))
plt.hist(df_cars['odometer'].dropna(), bins=50, edgecolor='black', color='green')
plt.title('Odometer Distribution')
plt.xlabel('Odometer')
plt.ylabel('Frequency')
plt.show()

# Top manufacturers
top_manufacturers = df_cars['manufacturer'].value_counts().head(10)
plt.figure(figsize=(10, 5))
plt.barh(top_manufacturers.index, top_manufacturers.values, color='purple')
plt.title('Top 10 Manufacturers')
plt.xlabel('Count')
plt.gca().invert_yaxis()
plt.show()

#Data cleaning 
# Select relevant columns, we do not select 'model' (too many unique values, too sparse and will hurt the model performance)
cols = ['price', 'year', 'manufacturer', 'condition', 'cylinders', 'fuel', 'odometer', 'transmission', 'type']
df_clean = df_cars[cols].copy()

# Drop rows where target (price) or key features are missing - can't predict without them
print(f"Before: {df_clean.shape}")
df_clean = df_clean.dropna(subset=['price', 'year', 'odometer'])
print(f"After dropping missing price/year/odometer: {df_clean.shape}")

# Fill categorical columns with 'unknown' - missing likely means "not specified"
for col in ['manufacturer', 'condition', 'fuel', 'transmission', 'type']:
    df_clean[col] = df_clean[col].fillna('unknown')

# Fill cylinders with mode - discrete feature, mode is most representative
df_clean['cylinders'] = df_clean['cylinders'].fillna(df_clean['cylinders'].mode()[0])

print("Missing values remaining:", df_clean.isnull().sum().sum())

# Encode categorical columns - converts text to integers
categorical_cols = ['manufacturer', 'condition', 'cylinders', 'fuel', 'transmission', 'type']
for col in categorical_cols:
    le = LabelEncoder()
    df_clean[col] = le.fit_transform(df_clean[col].astype(str))

df_clean.head()


# Car age: older cars typically worth less
df_clean['age'] = 2026 - df_clean['year']

# Mileage per year: high usage = more wear
df_clean['miles_per_year'] = df_clean['odometer'] / (df_clean['age'])


# Interaction: captures combined effect of age and annual mileage
df_clean['age_x_miles_per_year'] = df_clean['miles_per_year'] * df_clean['age']

# Quick preview of engineered features
df_clean[['year', 'age', 'odometer', 'miles_per_year', 'age_x_miles_per_year']].head()

# Define features (X) and target (y)
feature_cols = ['year', 'odometer', 'age', 'miles_per_year',
                'manufacturer', 'condition', 'cylinders', 'fuel', 'transmission', 'type',
             'age_x_miles_per_year']
X = df_clean[feature_cols]
y = df_clean['price']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

print(f"\nFeature ranges - Min: {X_train.min().min():.2f}, Max: {X_train.max().max():.2f}")
X_train.head(3)

# Scale features - fit on train, transform both
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nScaled ranges - Min: {X_train_scaled.min():.2f}, Max: {X_train_scaled.max():.2f}")
pd.DataFrame(X_train_scaled, columns=X_train.columns).head(3)

# Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)
print("Model trained!")

# Predict and evaluate
y_pred = model.predict(X_test_scaled)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"MAE:  ${mae:,.2f}")
print(f"RMSE: ${rmse:,.2f}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(feature_importance['feature'], feature_importance['importance'])
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.gca().invert_yaxis()
plt.show()

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

mae_scores = []
rmse_scores = []

for train_idx, val_idx in kfold.split(X_train_scaled):
    X_fold_train, X_fold_val = X_train_scaled[train_idx], X_train_scaled[val_idx]
    y_fold_train, y_fold_val = y_train.iloc[train_idx], y_train.iloc[val_idx]

    # Train and predict
    model.fit(X_fold_train, y_fold_train)
    y_fold_pred = model.predict(X_fold_val)

    # Calculate metrics
    mae_scores.append(mean_absolute_error(y_fold_val, y_fold_pred))
    rmse_scores.append(np.sqrt(mean_squared_error(y_fold_val, y_fold_pred)))

mae_scores = np.array(mae_scores)
rmse_scores = np.array(rmse_scores)

print(f"5-Fold CV Results:")
print(f"MAE:  ${mae_scores.mean():,.2f}")
print(f"RMSE: ${rmse_scores.mean():,.2f}")