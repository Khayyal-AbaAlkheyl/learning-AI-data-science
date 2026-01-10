import numpy as np 
import pandas as pd
np.random.seed(42) # for reproducbility

# Generating random data for regression 
X_reg = pd.DataFrame({"Feature_1": np.random.randn(500)}) # inputs 
y_reg = 3 * X_reg["Feature_1"] + np.random.randn(500) * 0.5  # what we want to predict,np.random.randn(500) * 0.5 adds some noise

#Generating random data for classification
X_clf = pd.DataFrame({"Feature_1": np.random.randn(500)}) # inputs
y_clf = (X_clf["Feature_1"] > 0).astype(int) # what we want to predict, if Feature_1 > 0 then class 1 else class 0

from sklearn.model_selection import train_test_split
X, Y = X_clf.copy(), y_clf.copy()# choose either regression or classification data here claddification data is chosen

# split ratio (80% train, 20% test)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=0.2,random_state=42,shuffle=True,stratify=Y)# random_state for reproducibility
# Print shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", Y_train.shape)
print("y_test shape:", Y_test.shape)


#K-Fold Cross Validation
from sklearn.model_selection import KFold
# Use previously generated random data (example: regression data)
X, y = X_reg.copy(), y_reg.copy()
kfold=KFold(n_splits=5,shuffle=True,random_state=42)# create the kfold object

for fold ,(train_idx,test_idx) in enumerate (kfold.split(X,Y),start=1):
    X_reain=X.iloc[train_idx]
    X_test=X.iloc[test_idx]
    y_train=y.iloc[train_idx]       
    y_test=y.iloc[test_idx]
   
    print(f"Fold {fold}")
    print("  X_train shape:", X_train.shape)
    print("  X_test shape :", X_test.shape)
    print("  y_train shape:", Y_train.shape)
    print("  y_test shape :", Y_test.shape)
    print("-" * 30)


#Stratified K-Fold Cross Validation
from sklearn.model_selection import StratifiedKFold

# Use previously generated random classification data
X, y = X_clf.copy(), y_clf.copy()

# Show full dataset class distribution
full_ratio = (y.value_counts(normalize=True) * 100).sort_index()
print("Full Dataset Class Distribution")
print("  y class percentages:", {k: f"{v:.2f}%" for k, v in full_ratio.items()})
print("-" * 40)

# Define Stratified K-Fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("Stratified K-Fold Cross Validation\n" + "-"*40)

for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), start=1):
    # indexing for each fold
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    print(f"Fold {fold}")
    print("  X_train shape:", X_train.shape)
    print("  X_test shape :", X_test.shape)
    print("  y_train shape:", y_train.shape)
    print("  y_test shape :", y_test.shape)

    # showing class distribution
    train_ratio = (y_train.value_counts(normalize=True) * 100).sort_index()
    test_ratio = (y_test.value_counts(normalize=True) * 100).sort_index()

    print("  y_train class percentages:", {k: f"{v:.2f}%" for k, v in train_ratio.items()})
    print("  y_test class percentages :", {k: f"{v:.2f}%" for k, v in test_ratio.items()})

    print("-" * 40)