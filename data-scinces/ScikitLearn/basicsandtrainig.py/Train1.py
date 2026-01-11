import pandas as pd
import numpy as np

#Spliting the data for training and testing
from sklearn.model_selection import train_test_split,GridSearchCV

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

import matplotlib.pyplot as  plt
import seaborn as sns

data = pd.read_csv(r"c:\Users\khayy\OneDrive\Documents\GitHub\learning-AI-data-science\data-scinces\ScikitLearn\basicsandtrainig.py\titanc.csv")
data.info()#take a lokk at your data 
print(data.isnull().sum())#searching for missing values


#Data cleaning
def pre_preocess_data(df):
    df.drop(columns=["PassengerId","Name","Ticket","Cabin"],inplace=True)
    
    fill_missing_ages(df)
    #conver gender
    df["Sex"]=df["Sex"].map({"male":1,"female":0})
    df["FamilySize"]=df["SibSp"]+df["Parch"]
    df["IsAlone"]=np.where(df["FamilySize"]==0,1,0)
    df["FareBin"]=pd.qcut(df["Fare"],4,labels=False)
    df["AgeBin"]=pd.cut(df["Age"],bins=[0,12,20,30,40,60,np.inf],labels=False )
    df['Embarked'] = df['Embarked'].fillna('S') 
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    return df

def fill_missing_ages(df):

    age_fill_map={}
    for pclass in df["Pclass"].unique():
        if pclass not in age_fill_map:
            age_fill_map[pclass]=df[df["Pclass"]==pclass]["Age"].median()
    df["Age"]=df.apply(lambda row :age_fill_map[row ["Pclass"]] if pd.isnull(row["Age"])else row["Age"],axis =1)



data =pre_preocess_data(data)
data.info()#take a lokk at your data 
print(data.isnull().sum())#searching for missing values



X= data.drop(columns=["Survived"])
y=data["Survived"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

scaler=MinMaxScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


def tune_model(X_train,y_train):
    param_grid={
        "n_neighbors":range(1,21),
        "metric":["eculidean","manhattan","minkowski"],
        "weights":["uniform","distance"]
    }
    model=KNeighborsClassifier()
    grid_Search=GridSearchCV(model,param_grid,cv=5,n_jobs=-1)
    grid_Search.fit(X_train,y_train)
    return grid_Search.best_estimator_


best_model=tune_model(X_train,y_train)

def evaluate_model(model,X_test,y_test):
    predication=model.predict(X_test)
    accuracy=accuracy_score(y_test,predication)
    return accuracy

accuracy =evaluate_model(best_model,X_test,y_test)

print(f'acccuracy:{accuracy*100:.2f}')

