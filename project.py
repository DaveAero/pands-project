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


# funtion for subplotting
def subplotter(xAxis, yAxis):
    plt.subplot(2, 1, 1)
    plt.scatter(irisSetosa[xAxis], irisSetosa[yAxis], color='r')
    plt.scatter(irisVersicolour[xAxis], irisVersicolour[yAxis], color='g')
    plt.scatter(irisVirginica[xAxis], irisVirginica[yAxis], color='b')
    z = np.polyfit(irisData[xAxis], irisData[yAxis], 1)
    p = np.poly1d(z)
    plt.plot(irisData[xAxis],p(irisData[xAxis]), color='black')
    plt.yticks([0,1,2,3,4,5])
    plt.title("Iris Data", size = 20, color = 'black')
    plt.xlabel(xAxis, size = 12, color = 'black')
    plt.ylabel(yAxis, size = 12, color = 'black')

    # function for subpots
    def subplotterbot(flower, xAxis, yAxis, graphcolor, flowerName):
        plt.scatter(flower[xAxis], flower[yAxis], color= graphcolor)
        z = np.polyfit(flower[xAxis], flower[yAxis], 1)
        p = np.poly1d(z)
        plt.plot(flower[xAxis],p(flower[xAxis]),"black")
        plt.yticks([0,1,2,3,4,5])
        plt.title(flowerName, size = 15, color = 'black')
        plt.xlabel("Sepal Length", size = 9, color = 'black')
        plt.ylabel("Sepal Width", size = 9, color = 'black')


    # Iris Setosa subplot
    plt.subplot(2, 3, 4)
    subplotterbot(irisSetosa, xAxis, yAxis, "r", "Iris Setosa")

    # Iris Versicolour subplot
    plt.subplot(2, 3, 5)
    subplotterbot(irisVersicolour, xAxis, yAxis, "g", "Iris Versicolour")

    # Iris Virginica subplot
    plt.subplot(2, 3, 6)
    subplotterbot(irisVirginica, xAxis, yAxis, 'b', "Iris Virginica")

    plt.tight_layout()
    plt.show()

# Iris Data Subplot
subplotter("SepalLength", "SepalWidth")

subplotter("PetalLength", "PetalWidth")