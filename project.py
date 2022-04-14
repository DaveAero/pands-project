# project.py
# Author: David Burke
# Data analysis of the Fisher's Iris data set

#improting libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#impoting of the data set
irisData =  pd.read_csv('data\iris.data')
#print(irisData.head())

#irisNames = pd.read_csv('data\irisnames.data', sep="\t")
#print(irisNames)

#Attribute Information:
#   1. sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm
#   5. class: 
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica

# Assigning column names
irisData.columns =['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'FlowerClass']
#print(irisData.head())

# Sererating Followes into subsets of data for individual analysis
irisSetosa = irisData[irisData['FlowerClass'] == "Iris-setosa"]
irisVersicolour = irisData[irisData['FlowerClass'] == "Iris-versicolor"]
irisVirginica = irisData[irisData['FlowerClass'] == "Iris-virginica"]
#print(irisSetosa)



plt.scatter(irisSetosa["SepalLength"], irisSetosa["SepalWidth"], color='r')
z = np.polyfit(irisSetosa["SepalLength"], irisSetosa["SepalWidth"], 1)
p = np.poly1d(z)
plt.plot(irisSetosa["SepalLength"],p(irisSetosa["SepalLength"]),"r-")

plt.scatter(irisVersicolour["SepalLength"], irisVersicolour["SepalWidth"], color='g')
z = np.polyfit(irisVersicolour["SepalLength"], irisVersicolour["SepalWidth"], 1)
p = np.poly1d(z)
plt.plot(irisVersicolour["SepalLength"],p(irisVersicolour["SepalLength"]),"g-")

plt.scatter(irisVirginica["SepalLength"], irisVirginica["SepalWidth"], color='b')
z = np.polyfit(irisVirginica["SepalLength"], irisVirginica["SepalWidth"], 1)
p = np.poly1d(z)
plt.plot(irisVirginica["SepalLength"],p(irisVirginica["SepalLength"]),"b-")

z = np.polyfit(irisData["SepalLength"], irisData["SepalWidth"], 1)
p = np.poly1d(z)
plt.plot(irisData["SepalLength"],p(irisData["SepalLength"]))


plt.show()