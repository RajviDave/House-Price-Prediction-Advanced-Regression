import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("Dataset/train.csv")


null_features=[]
for features in dataset:
    if dataset[features].isnull().sum()>0:
        null_features.append(features)
    

for features in null_features:
    print(np.round(dataset[features].isnull().mean(),3),'% missing values')

print(len(null_features))

numerical_values=[]

for  feature in dataset:
    if dataset[feature].dtype!='str':
        numerical_values.append(feature)

# print(numerical_values)
# print(len(numerical_values))

categorical_value=[]

for feature in dataset:
    if dataset[feature].dtype=='str':
        categorical_value.append(feature)

# print(categorical_value)
# print(len(categorical_value))

#numerical values EDA
for feature in numerical_values:
    dataset[feature]=np.where(dataset[feature].isnull(),1,0)
    for i in dataset[feature]:
        if dataset[feature][i]==0:
            print(i)



