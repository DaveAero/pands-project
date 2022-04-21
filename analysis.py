# project.py
# Author: David Burke
# Data analysis of the Fisher's Iris data set

#improting libaries
from statistics import mean, stdev
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#impoting of the data set
#Attribute Information:
#   1. sepal length in cm
#   2. sepal width in cm
#   3. petal length in cm
#   4. petal width in cm
#   5. class: 
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
irisData =  pd.read_csv('data\iris.data', names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'FlowerClass'])
#print(irisData.head())

# Sererating Flowers into subsets of data for individual analysis
irisSetosa = irisData[irisData['FlowerClass'] == "Iris-setosa"]
irisVersicolour = irisData[irisData['FlowerClass'] == "Iris-versicolor"]
irisVirginica = irisData[irisData['FlowerClass'] == "Iris-virginica"]
#print(irisSetosa.head())

# Setting up a blank text file
filename = "Outputs\TextSummary\Analysis.txt"
f = open(filename,"w")
f.close()

###################### DEFINING FUNCTIONS ######################
# FUnction for outputting a summary to a text file
def textOutput(text, title):
    with open(filename, "a") as f:
        # write takes a string so we need to convert
        f.write(str(title))
        f.write(str("\n"))
        f.write(str(text))
        f.write(str("\n"))
        f.write(str("-----"))
        f.write(str("\n"))
        f.write(str("-----"))
        f.write(str("\n"))

# function for outputting single variable histogram summaries
def variableHist(xAxis):
    plt.subplot(2, 1, 1)
    plt.hist([irisSetosa[xAxis], irisVersicolour[xAxis], irisVirginica[xAxis]], bins= 30, label=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], color = ["cornflowerblue", "mediumseagreen", "firebrick"])
    plt.title(xAxis, size = 15, color = 'black')
    plt.xlabel(xAxis, size = 12, color = 'black')
    plt.grid(axis = 'y')

    # function for subpots on the second row
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

    # outputting the histograms to a saved .png
    plt.tight_layout()
    plt.savefig('Outputs\Histograms\{}.png'.format(col))
    plt.show()

# funtion for outputing a scatter plot of each variable pair
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

    # function for subpots on the second row
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

    # Outputting the Scatter plots and saving as a .png
    plt.tight_layout()
    plt.savefig('Outputs\ScatterPlots\{}Vs{}.png'.format(xAxis, yAxis))
    plt.show()

###################### MAIN CODE ######################
# 1. 
# Creating a text summary for each variable
textOutput(irisData.describe(), "Summary of Iris Data set")
textOutput(irisSetosa.describe(), "Summary of Iris Setosa subset")
textOutput(irisVersicolour.describe(), "Summary of Iris Versicolour subset")
textOutput(irisVirginica.describe(), "Summary of Iris Virginica subset")

# 2.
# Creating histograms for each variable
for col in irisData.columns:
    variableHist(col)

# 3.
# Creating scatter potls for each pair of variables
subplotter("SepalLength", "SepalWidth")

subplotter("PetalLength", "PetalWidth")

subplotter("SepalLength", "PetalWidth")

subplotter("PetalLength", "SepalWidth")

# 4. Extra
# Analysis of the relationship between petal dimetions and the sepal relationships
flowers = ["irisSetosa", "irisVersicolour", "irisVirginica"]

irisDataPetalRatio = irisData["PetalLength"] / irisData["PetalWidth"]
irisDataSepalRatio = irisData["SepalLength"] / irisData["SepalWidth"]

irisSetosaPetalRatio = irisSetosa["PetalLength"] / irisSetosa["PetalWidth"]
irisSetosaSepalRatio = irisSetosa["SepalLength"] / irisSetosa["SepalWidth"]

irisVersicolourPetalRatio = irisVersicolour["PetalLength"] / irisVersicolour["PetalWidth"]
irisVersicolourSepalRatio = irisVersicolour["SepalLength"] / irisVersicolour["SepalWidth"]

irisVirginicaPetalRatio = irisVirginica["PetalLength"] / irisVirginica["PetalWidth"]
irisVirginicaSepalRatio = irisVirginica["SepalLength"] / irisVirginica["SepalWidth"]

z = np.polyfit(irisDataPetalRatio, irisDataSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisDataPetalRatio,p(irisDataPetalRatio), color= "black")

plt.scatter(irisSetosaPetalRatio, irisSetosaSepalRatio, color="cornflowerblue")
z = np.polyfit(irisSetosaPetalRatio, irisSetosaSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisSetosaPetalRatio,p(irisSetosaPetalRatio), color="cornflowerblue")

plt.scatter(irisVersicolourPetalRatio, irisVersicolourSepalRatio, color= "mediumseagreen")
z = np.polyfit(irisVersicolourPetalRatio, irisVersicolourSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisVersicolourPetalRatio,p(irisVersicolourPetalRatio), color="mediumseagreen")

plt.scatter(irisVirginicaPetalRatio, irisVirginicaSepalRatio, color= "firebrick")
z = np.polyfit(irisVirginicaPetalRatio, irisVirginicaSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisVirginicaPetalRatio,p(irisVirginicaPetalRatio), color="firebrick")

plt.title("PetalRatio Vs SepalRatio", size = 20, color = 'black')
plt.xlabel("PetalRatio", size = 12, color = 'black')
plt.ylabel("SepalRatio", size = 12, color = 'black')
plt.savefig('Outputs\Extra\PetalRatioVsSepalRatio.png')
plt.show()

# 5. Extra
# Analyis the relationship between the mean petal lenth and the standard deviation
irisSetosaMean = mean(irisSetosa["PetalLength"])
irisVersicolourMean = mean(irisVersicolour["PetalLength"])
irisVirginicaMean = mean(irisVirginica["PetalLength"])

irisSetosaSD = stdev(irisSetosa["PetalLength"])
irisVersicolourSD = stdev(irisVersicolour["PetalLength"])
irisVirginicaSD = stdev(irisVirginica["PetalLength"])

plt.scatter(irisSetosaMean, irisSetosaSD, color="cornflowerblue")
plt.scatter(irisVersicolourMean, irisVersicolourSD, color= "mediumseagreen")
plt.scatter(irisVirginicaMean, irisVirginicaSD, color= "firebrick")
plt.title("MeanPetalLength Vs SDPetalLength", size = 20, color = 'black')
plt.xlabel("MeanPetalLength", size = 12, color = 'black')
plt.ylabel("SDPetalLength", size = 12, color = 'black')
plt.savefig('Outputs\Extra\MeanPetalLengthVsSDPetalLength.png')
plt.show()