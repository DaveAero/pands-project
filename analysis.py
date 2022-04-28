# project.py
# Author: David Burke
# This program is used to analysis of the Fisher's Iris data set. 
# It will load the data each time and produce scatterplots, Histograms and a text summary.

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


# Reading data as a CSV and saving the data as a python database 
# Adding column names as these were now includeded as part of the database
irisData =  pd.read_csv('data\iris.data', names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'FlowerClass'])
#print(irisData.head())

# Seperating Flowers into subsets of data for individual analysis
# Using a logical test in the flower class column
irisSetosa = irisData[irisData['FlowerClass'] == "Iris-setosa"]
irisVersicolour = irisData[irisData['FlowerClass'] == "Iris-versicolor"]
irisVirginica = irisData[irisData['FlowerClass'] == "Iris-virginica"]
#print(irisSetosa.head())

# Setting up a blank text file at the start
filename = "Outputs\TextSummary\Analysis.txt"
f = open(filename,"w")
f.close()

###################### DEFINING FUNCTIONS ######################
# Function for outputting a text summary to a .txt file
def textOutput(text, title):
    # Using append as to allow this function to be run multiple times
    with open(filename, "a") as f:
        # write takes a string so we need to convert
        f.write(str("{} \n".format(title)))
        # creating a large space between each text input so each database can be quickly identified
        f.write(str("{} \n----- \n----- \n".format(text)))

# Function for outputting histogram summaries
# This function only requires 1 input to run, we must specify which column to plot on the histogram
def variableHist(xAxis):
    #Subplots will be used, the sub plot function need to be told the desired output as follows (Columns, Rows, current grapths position starting top left moving right then down)
    plt.subplot(2, 1, 1)
    # All 3 flower classes are added to the histogram seperatly to allow them to be coloured individually.
    # bin size 30 was found to be well suited through trial and error
    plt.hist([irisSetosa[xAxis], irisVersicolour[xAxis], irisVirginica[xAxis]], bins= 30, label=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], color = ["cornflowerblue", "mediumseagreen", "firebrick"])
    # Adding a title and label and gridlines as part of the function
    plt.title(xAxis, size = 15, color = 'black')
    plt.xlabel(xAxis, size = 12, color = 'black')
    plt.grid(axis = 'y')

    # function for subpots on the second row
    # This function is run inside of the VariableHist function
    # This fucntion takes 4 inputs to output the graphs
    def subvariableHist(flower, xAxis, graphcolor, flowerName):
        plt.hist(flower[xAxis], bins= 10, color= graphcolor)
        # Adding a title and label and gridlines as part of the function
        plt.title(flowerName, size = 15, color = 'black')
        plt.xlabel(xAxis, size = 9, color = 'black')
        plt.grid(axis = 'y')

    # Iris Setosa subplot using the subvariableHist function
    # the subplot location is confirmed before calling the subvariableHist function 
    plt.subplot(2, 3, 4)
    subvariableHist(irisSetosa, xAxis, "cornflowerblue", "Iris Setosa")

    # Iris Versicolour subplot using the subvariableHist function
    plt.subplot(2, 3, 5)
    subvariableHist(irisVersicolour, xAxis, "mediumseagreen", "Iris Versicolour")

    # Iris Virginica subplot using the subvariableHist function
    plt.subplot(2, 3, 6)
    subvariableHist(irisVirginica, xAxis, "firebrick", "Iris Virginica")

    # outputting the histograms to a saved .png and also printing a copy to user
    plt.tight_layout()
    # File path is given as relative to the analysis.py program
    plt.savefig('Outputs\Histograms\{}.png'.format(col))
    plt.show()

# Funtion for outputing a scatter plot of each variable pair
# This function requires 2 inputs to confirm the two variables being plotted
def subplotter(xAxis, yAxis):
    plt.subplot(2, 1, 1)
    # Each flower is plotted individually as to allow different colours to be selcted
    plt.scatter(irisSetosa[xAxis], irisSetosa[yAxis], color="cornflowerblue")
    plt.scatter(irisVersicolour[xAxis], irisVersicolour[yAxis], color= "mediumseagreen")
    plt.scatter(irisVirginica[xAxis], irisVirginica[yAxis], color= "firebrick")
    # This function is used to creat a line of best fit for the data
    # Polyfit is used to return the coefficents in the equation of best fit
    z = np.polyfit(irisData[xAxis], irisData[yAxis], 1)
    # Poly1d is used to return a vector for the equation of the line of best fit
    p = np.poly1d(z)
    # The line of best fit is then plotted, this is done by plotting the given data on the x-axis
    # And then the value for the corrisponding y point is found by using passing each value through the equation created
    plt.plot(irisData[xAxis],p(irisData[xAxis]), color='black')
    # Adding a title and label and gridlines as part of the function
    plt.yticks([0,1,2,3,4,5])
    plt.title("{} Vs {}".format(xAxis, yAxis), size = 20, color = 'black')
    plt.xlabel(xAxis, size = 12, color = 'black')
    plt.ylabel(yAxis, size = 12, color = 'black')

    # function for subpots on the second row
    # This function is run inside of the subplotter function
    # This fucntion takes 5 inputs to output the graphs
    def subplotterbot(flower, xAxis, yAxis, graphcolor, flowerName):
        plt.scatter(flower[xAxis], flower[yAxis], color= graphcolor)
        # Again the line of best function is used here
        z = np.polyfit(flower[xAxis], flower[yAxis], 1)
        p = np.poly1d(z)
        plt.plot(flower[xAxis],p(flower[xAxis]),"black")
        # Adding a title and label and gridlines as part of the function
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
# Creating a text summary for each variable using the textOutput function defined above
# The two inputs required are the text to be output and the title for the summary
textOutput(irisData.describe(), "Summary of Iris Data set")
textOutput(irisSetosa.describe(), "Summary of Iris Setosa subset")
textOutput(irisVersicolour.describe(), "Summary of Iris Versicolour subset")
textOutput(irisVirginica.describe(), "Summary of Iris Virginica subset")

# 2.
# Creating histograms for each variable using the variableHist function defined above
# the function will be run 4 times, for each of the columns in the database
for col in irisData.columns:
    variableHist(col)

# 3.
# Creating scatter potls for each pair of variables using the subplotter function
subplotter("SepalLength", "SepalWidth")
subplotter("PetalLength", "PetalWidth")
subplotter("SepalLength", "PetalWidth")
subplotter("PetalLength", "SepalWidth")

####################### 4. Extra ######################
# Analysis of the relationship between petal dimetions and the sepal relationships
# This relationship will be defined as the Petal Lenth / the Petal Width 
# over the Sepal Lenth / Sepal Width
flowers = ["irisSetosa", "irisVersicolour", "irisVirginica"]

# defining the ratio for each of the databases
# Full irisData base
irisDataPetalRatio = irisData["PetalLength"] / irisData["PetalWidth"]
irisDataSepalRatio = irisData["SepalLength"] / irisData["SepalWidth"]

# Each of the 3 flower classes
irisSetosaPetalRatio = irisSetosa["PetalLength"] / irisSetosa["PetalWidth"]
irisSetosaSepalRatio = irisSetosa["SepalLength"] / irisSetosa["SepalWidth"]
irisVersicolourPetalRatio = irisVersicolour["PetalLength"] / irisVersicolour["PetalWidth"]
irisVersicolourSepalRatio = irisVersicolour["SepalLength"] / irisVersicolour["SepalWidth"]
irisVirginicaPetalRatio = irisVirginica["PetalLength"] / irisVirginica["PetalWidth"]
irisVirginicaSepalRatio = irisVirginica["SepalLength"] / irisVirginica["SepalWidth"]

# plotting data for the irisSetosa and the trend line for this data
plt.scatter(irisSetosaPetalRatio, irisSetosaSepalRatio, color="cornflowerblue")
z = np.polyfit(irisSetosaPetalRatio, irisSetosaSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisSetosaPetalRatio,p(irisSetosaPetalRatio), color="cornflowerblue")

# plotting data for the irisVersicolour and the trend line for this data
plt.scatter(irisVersicolourPetalRatio, irisVersicolourSepalRatio, color= "mediumseagreen")
z = np.polyfit(irisVersicolourPetalRatio, irisVersicolourSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisVersicolourPetalRatio,p(irisVersicolourPetalRatio), color="mediumseagreen")

# plotting data for the irisVirginica and the trend line for this data
plt.scatter(irisVirginicaPetalRatio, irisVirginicaSepalRatio, color= "firebrick")
z = np.polyfit(irisVirginicaPetalRatio, irisVirginicaSepalRatio, 1)
p = np.poly1d(z)
plt.plot(irisVirginicaPetalRatio,p(irisVirginicaPetalRatio), color="firebrick")

# Adding a title and label and gridlines as part of the function
plt.title("PetalRatio Vs SepalRatio", size = 20, color = 'black')
plt.xlabel("PetalRatio", size = 12, color = 'black')
plt.ylabel("SepalRatio", size = 12, color = 'black')
plt.savefig('Outputs\Extra\PetalRatioVsSepalRatio.png')
plt.show()

####################### 5. Extra ######################
# Analyis the relationship between the mean petal lenth
# and the standard deviation for that flower class

# First finding each mean petal lenth
irisSetosaMean = mean(irisSetosa["PetalLength"])
irisVersicolourMean = mean(irisVersicolour["PetalLength"])
irisVirginicaMean = mean(irisVirginica["PetalLength"])

# next finding the standard deviation for each petal lenth
irisSetosaSD = stdev(irisSetosa["PetalLength"])
irisVersicolourSD = stdev(irisVersicolour["PetalLength"])
irisVirginicaSD = stdev(irisVirginica["PetalLength"])

# Plotting each of the results
plt.scatter(irisSetosaMean, irisSetosaSD, color="cornflowerblue")
plt.scatter(irisVersicolourMean, irisVersicolourSD, color= "mediumseagreen")
plt.scatter(irisVirginicaMean, irisVirginicaSD, color= "firebrick")
# Adding a title and label and gridlines as part of the function
plt.title("MeanPetalLength Vs SDPetalLength", size = 20, color = 'black')
plt.xlabel("MeanPetalLength", size = 12, color = 'black')
plt.ylabel("SDPetalLength", size = 12, color = 'black')
plt.savefig('Outputs\Extra\MeanPetalLengthVsSDPetalLength.png')
plt.show()