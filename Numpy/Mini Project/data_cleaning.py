# Importing necessary libraries
import pandas as pd
import numpy as np


# loading the dataset 
data = pd.read_csv("Pakistan_employees.csv")
# print(data.head(4))

# Checking missing values in the dataset
print("Missing values in the each columne : ", data.isnull().sum())




