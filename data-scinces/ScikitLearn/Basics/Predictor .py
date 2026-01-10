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

#_____________________________________________________________________
#Predoctor
# Import base linear model for regression (Linear Regression)
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Use previously generated random regression data
X, y = X_reg.copy(), y_reg.copy()

# split ratio (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42,shuffle=True)

model = LinearRegression()          # instantiate
model.fit(X_train, y_train)         # fit
y_pred = model.predict(X_test)      # predict

# Plot for Linear Regression Predictions vs. Ground Truth
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--', linewidth=2)
plt.xlabel("Actual y_test (Ground Truth)")
plt.ylabel("Predicted y_pred (Linear Regression)")
plt.title("Linear Regression: Predictions vs. Ground Truth")
plt.grid(True)

plt.tight_layout()
plt.show()

# Logistic Regression


# Import base linear model for classification (Logistic Regression)
from sklearn.linear_model import LogisticRegression

# Use previously generated random classification data
X, y = X_clf.copy(), y_clf.copy()

# split ratio (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # 20% for test, remaining 80% for train
    random_state=42,      # reproducible output
    shuffle=True,         # representative splits
    stratify=y            # preserve class distribution
)

model = LogisticRegression()     # instantiate
model.fit(X_train, y_train)      # fit
y_pred = model.predict(X_test)   # predict

     

# lets use confusion matrix to visualize the predictions
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

# use ConfusionMatrixDisplay for visualization
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

disp.plot()
plt.show()

#sklearn.tree
#DecisionTreeRegressor
# Import tree-based model for regression (Decision Tree Regressor)
from sklearn.tree import DecisionTreeRegressor

# Use previously generated random regression data
X, y = X_reg.copy(), y_reg.copy()

# Split ratio (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42,shuffle=True)

# Train Decision Tree Regressor
model = DecisionTreeRegressor(random_state=42)  # instantiate
model.fit(X_train, y_train)                     # fit
y_pred = model.predict(X_test)                  # predict

     

# Plot for Decision Tree Regression Predictions vs. Ground Truth
plt.figure(figsize=(6, 4))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)],
         [min(y_test), max(y_test)],
         'r--', linewidth=2)

plt.xlabel("Actual y_test (Ground Truth)")
plt.ylabel("Predicted y_pred (Decision Tree)")
plt.title("Decision Tree Regression: Predictions vs. Ground Truth")
plt.grid(True)

plt.tight_layout()
plt.show()

#DecisionTreeClassifier
# Import tree-based model for classification (Decision Tree Classifier)
from sklearn.tree import DecisionTreeClassifier

# Use previously generated random classification data
X, y = X_clf.copy(), y_clf.copy()

# Split ratio (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42,shuffle=True)

# Train Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42) # instantiate
model.fit(X_train, y_train)                     # fit
y_pred = model.predict(X_test)                  # predict
     

# lets use confusion matrix to visualize the predictions
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

# use ConfusionMatrixDisplay for visualization
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

disp.plot()
plt.show()