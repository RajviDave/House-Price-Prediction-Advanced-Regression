import pandas as pd

dataset=pd.read_csv("Dataset/train.csv")

# print(dataset.shape)
# print(dataset.head())

# missing=dataset.isnull()
# print(missing)

print(dataset['HouseStyle'].isnull()[:25])
num=[1,2,3,4,5,' ']
for x in dataset:
    if x.isnull():
        print('it has missing values')



# for features in dataset:
    