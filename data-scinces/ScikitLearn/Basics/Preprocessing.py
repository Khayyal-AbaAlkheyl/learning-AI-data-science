# Random data generation for encoding
import pandas as pd

categories = pd.DataFrame({"Animal": ['cat', 'dog', 'cat', 'bird', 'dog']}) # DataFrame of one column

print("Before encoding:")
print(categories)



# One-Hot Encoding using Scikit-Learn
from sklearn.preprocessing import OneHotEncoder
print('data before encoding:\n', categories) #show before encoding
onehot_encoder=OneHotEncoder(sparse_output=False)# create the encoder we put sparse_output to false to get a dense array insted of sparse matrix
data_onehot_encoded=onehot_encoder.fit_transform(categories)# fit and transform the data'
print('data after encoding:\n', data_onehot_encoded) #show after encoding



#LabelEncoder 
from sklearn.preprocessing import LabelEncoder
print('data before encoding:\n', categories) #show before encoding
Label_encoder=LabelEncoder()# create the encoder
data_label_encoded=Label_encoder.fit_transform(categories['Animal'])# fit and transform the data'
print('data after encoding:\n', data_label_encoded) #show after encoding



# StandardScaler
# Random data generation for scaling
data_for_scale = pd.DataFrame({"Feature_1": [11, 40, 19,12],"Feature_2": [2384, 439, 3282,576]})
print("Before scaling:")
print(data_for_scale)
# Standard Scaling using Scikit-Learn
from sklearn.preprocessing import StandardScaler
stander_scaler=StandardScaler() # create the scaler
data_stander_scaled=stander_scaler.fit_transform(data_for_scale) # fit and transform the data
print("After standard scaling:")        
print(data_stander_scaled)


# MinMaxScaler
#it sets the values between 0 and 1 and the leatst value to 0 and the highest to 1 and the rest between them
from sklearn.preprocessing import MinMaxScaler
print("Before scaling:")
print(data_for_scale)
minmax_scaler=MinMaxScaler()# Instantiate  the scaler
data_minmax_scaled=minmax_scaler.fit_transform(data_for_scale) #Apply fit_transform to the copied data
print("After Min-Max scaling:")
print(data_minmax_scaled)


