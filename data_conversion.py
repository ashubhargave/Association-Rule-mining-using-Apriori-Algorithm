import pandas as pd
import numpy as np
#Open the raw data file
automobile_data = pd.read_csv("C:\Data mining\Homework4\Problem 3\\data\l1.txt",delimiter=",")
#Iterate over all the columns
for y in automobile_data.columns:
    #Check the data type of the column. If it is non numberic the create dummy values and save them as binary data.
    if automobile_data[y].dtype == "object":
        automobile_data[y] = pd.get_dummies(automobile_data[y])
    #If it is numberic data 
    elif automobile_data[y].dtype == np.int64:
         # Find the mean of the column
         automobile_data[y].fillna(automobile_data[y].mean())
         # If the value is less than mean then it is set to 0
         automobile_data.loc[automobile_data[y] < automobile_data[y].mean(),y] = 0
         # If the value is greater than mean then it is set to 1
         automobile_data.loc[automobile_data[y] >= automobile_data[y].mean(),y] = 1
new_data = automobile_data
#Save the dataframe as a csv file
new_data.to_csv("C:\Data mining\Homework4\Problem 3\\data\new_data.txt")
