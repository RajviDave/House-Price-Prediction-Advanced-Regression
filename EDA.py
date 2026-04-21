import pandas as pd
import numpy as np

dataset=pd.read_csv("Dataset/train.csv")

# print(dataset.shape)
# print(dataset.head())

# missing=dataset.isnull()
# print(missing)

#print(dataset['LotFrontage'].isnull()[:25])
# num=[1,2,3,4,5,' ']
# for x in dataset:
#     if x.isnull():
#         print('it has missing values')

null_features=[]
for features in dataset:
    if dataset[features].isnull().sum()>0:
        null_features.append(features)
    
#print(dataset['LotFrontage'].isnull().sum())
for features in null_features:
    print(np.round(dataset[features].isnull().mean(),3),'% missing values')