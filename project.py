# project.py
# Author: David Burke
# Data analysis of the Fisher's Iris data set

#improting libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#impoting of the data set
irisData =  pd.read_csv('data\iris.data', names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'FlowerClass'])
#print(irisData.head())

#Attribute Information:
#   1. sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm
#   5. class: 
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica

#print(irisData.head())

# Sererating Followes into subsets of data for individual analysis
irisSetosa = irisData[irisData['FlowerClass'] == "Iris-setosa"]
irisVersicolour = irisData[irisData['FlowerClass'] == "Iris-versicolor"]
irisVirginica = irisData[irisData['FlowerClass'] == "Iris-virginica"]
#print(irisSetosa.head())

###################### DEFINING FUNCTIONS ######################


#single variable histogram summaries
def variableHist(xAxis):
    plt.subplot(2, 1, 1)
    plt.hist([irisSetosa[xAxis], irisVersicolour[xAxis], irisVirginica[xAxis]], bins= 15, label=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], color = ["cornflowerblue", "mediumseagreen", "firebrick"])
    plt.title(xAxis, size = 15, color = 'black')
    plt.xlabel(xAxis, size = 12, color = 'black')
    plt.grid(axis = 'y')

    # function for subpots
    def subvariableHist(flower, xAxis, graphcolor, flowerName):
        plt.hist(flower[xAxis], bins= 10, color= graphcolor)
        plt.title(flowerName, size = 15, color = 'black')
        plt.xlabel(xAxis, size = 9, color = 'black')
        plt.grid(axis = 'y')

    # Iris Setosa subplot
    plt.subplot(2, 3, 4)
    subvariableHist(irisSetosa, xAxis, "cornflowerblue", "Iris Setosa")

    # Iris Versicolour subplot
    plt.subplot(2, 3, 5)
    subvariableHist(irisVersicolour, xAxis, "mediumseagreen", "Iris Versicolour")

    # Iris Virginica subplot
    plt.subplot(2, 3, 6)
    subvariableHist(irisVirginica, xAxis, "firebrick", "Iris Virginica")

    plt.tight_layout()
    plt.savefig('Outputs\Histograms\{}.png'.format(col))
    plt.show()

# funtion for subplotting
def subplotter(xAxis, yAxis):
    plt.subplot(2, 1, 1)
    plt.scatter(irisSetosa[xAxis], irisSetosa[yAxis], color="cornflowerblue")
    plt.scatter(irisVersicolour[xAxis], irisVersicolour[yAxis], color= "mediumseagreen")
    plt.scatter(irisVirginica[xAxis], irisVirginica[yAxis], color= "firebrick")
    z = np.polyfit(irisData[xAxis], irisData[yAxis], 1)
    p = np.poly1d(z)
    plt.plot(irisData[xAxis],p(irisData[xAxis]), color='black')
    plt.yticks([0,1,2,3,4,5])
    plt.title("{} Vs {}".format(xAxis, yAxis), size = 20, color = 'black')
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
        plt.xlabel(xAxis, size = 9, color = 'black')
        plt.ylabel(yAxis, size = 9, color = 'black')

    # Iris Setosa subplot
    plt.subplot(2, 3, 4)
    subplotterbot(irisSetosa, xAxis, yAxis, "cornflowerblue", "Iris Setosa")

    # Iris Versicolour subplot
    plt.subplot(2, 3, 5)
    subplotterbot(irisVersicolour, xAxis, yAxis, "mediumseagreen", "Iris Versicolour")

    # Iris Virginica subplot
    plt.subplot(2, 3, 6)
    subplotterbot(irisVirginica, xAxis, yAxis, "firebrick", "Iris Virginica")

    plt.tight_layout()
    plt.savefig('Outputs\ScatterPlots\{} Vs {}.png'.format(xAxis, yAxis))
    plt.show()

###################### MAIN CODE ######################
# 1. 
# Creating a text summary for each variable
print("The minimum is {}".format(min(irisData['SepalLength'])))

# 2.
# Creating histograms for each variable
#for col in irisData.columns:
#    variableHist(col)

# 3.
# Creating scatter potls for each pair of variables
#subplotter("SepalLength", "SepalWidth")

#subplotter("PetalLength", "PetalWidth")

#subplotter("SepalLength", "PetalWidth")

#subplotter("PetalLength", "SepalWidth")