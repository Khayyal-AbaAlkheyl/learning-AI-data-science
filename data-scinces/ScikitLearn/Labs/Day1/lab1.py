#Preprocessing OneHotEncoder ,LabelEncoder, SatnderScaler, MinMaxScaler 
import pandas as pd 
categories  =pd.DataFrame({"Animal":['cat','mouse','dog','bird','cat']})

print("Before Encoding :")
print(categories)

from sklearn.preprocessing import OneHotEncoder

onehot_encoder=OneHotEncoder(sparse_output=False)

data_oneHotEncoded=onehot_encoder.fit_transform(categories)
#first it sort them in alphapatical order then it put them in a mtrix where it converts them to 0 and 1 Bird -Cat -Dog -Mouse
print("After Encoding :")
print(data_oneHotEncoded)


from sklearn.preprocessing import LabelEncoder

print("Before Encoding :")
print(categories)

label_encoder=LabelEncoder()
labels_encoded=label_encoder.fit_transform(categories["Animal"])

print("After Encoding :")
print(labels_encoded)


from sklearn.preprocessing import StandardScaler
# Random data generation for scaling
data_for_scale = pd.DataFrame({"Feature_1": [11, 40, 19,12],"Feature_2": [2384, 439, 3282,576]})

print("Before scaling:")
print(data_for_scale)
scaler=StandardScaler()
scalred_data=scaler.fit_transform(data_for_scale)
print("Before scaling:")
print(scalred_data)

from sklearn.preprocessing import MinMaxScaler

minmax=MinMaxScaler()
data_minmaxed=minmax.fit_transform(data_for_scale)
print("Before scaling:")
print(data_for_scale)
print("After scaling:",data_minmaxed)


#data spliting 
import numpy as np 

np.random.seed(42)
#Creating an input and output for regression 
X_reg=pd.DataFrame({'Feature1':np.random.randn(500)})#500 random number but there means is approx 0 and std approx 1 
y_reg=3*X_reg["Feature1"] +np.random.randn(500)*0.5

#Creating an input and output for classification
X_clf=pd.DataFrame({'Feature1':np.random.randn(500)})#500 random number but there means is approx 0 and std approx 1 
y_clf=(X_clf["Feature1"]>0).astype(int)# labels as class 0 or 1
print(y_clf)

from sklearn.model_selection import train_test_split
# Use previously generated random data (example: classification data)
X,y=X_clf.copy(),y_clf.copy()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True,stratify=y)

# Print shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.model_selection import KFold 

X,y=X_reg.copy(),y_reg.copy()
kf=KFold(n_splits=5,shuffle=True,random_state=42)

for fold , (train_idx,test_idx) in enumerate (kf.split(X),start=1):
    X_train,X_test=X.iloc[train_idx],X.iloc[test_idx]
    y_train,y_test=y.iloc[train_idx],y.iloc[test_idx]
    print(f"Fold {fold}:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

from sklearn.model_selection import StratifiedKFold
X,y= X_clf.copy(),y_clf.copy()

full_ratio=(y.value_counts(normalize=True)*100).sort_index()
print("Full Dataset Class Distribution")
print(" y class persentage :",{k:f"{v:.2f}%"for k,v in full_ratio.items()})


skf=StratifiedKFold(n_splits=5,shuffle=True,random_state=42)


for fold ,(train_idx,test_idx) in enumerate(skf.split(X,y),start=1):
    X_train,X_test=X.iloc[train_idx],X.iloc[test_idx]
    y_train,y_test=y.iloc[train_idx],y.iloc[test_idx]
    print(f"Fold {fold}:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)
    train_ratio=(y_train.value_counts(normalize=True)*100).sort_index()
    test_ratio=(y_test.value_counts(normalize=True)*100).sort_index()
    
    print("y_train class persentage :",{k:f"{v:.2f}%"for k,v in train_ratio.items()})
    
    print("y_test class persentage :",{k:f"{v:.2f}%"for k,v in test_ratio.items()})
