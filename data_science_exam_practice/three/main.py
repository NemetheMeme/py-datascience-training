import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import scatter

data = pd.read_csv('exams.csv')

# histogram
# shows the value distribution of a numerical value -
# plt.figure(figsize=(7,5))
# sns.histplot(data=data, x="math score", bins=5, kde=True, color='blue')
# kde = Kernel Density Estimation - the curve  that shows the estimated distribution
# bins = number of boxes, lower - see the global dependency, higher - see more detailed
# x = the column on which we're doing the distribution
# plt.title("Math Score distribution")
# plt.xlabel("Math Score")
# plt.ylabel("Student number")
# plt.show()

# boxplot - data distribution using a median, quarters and the extremities
# used to compare groups -> for example math scores per gender
# sns.boxplot(data=data, x="gender", y="math score")
# plt.title("Math Score distribution per gender")
# plt.ylabel("Math Score")
# plt.show()
## How to read a boxplot:
# the box represents 50% of the data from Q1 to Q3, that means the middle side of the data
# the line from the box represents the median value - middle value if you order all the data
# the "whiskers"  go to data that are considerate normal
# the isolated points / out-liners - unusual low/high values
# "tendency"

# scatterplot - point graphic
# x and y are 2 variables each point represents a student, the position shows what score they have on those 2 scores
# correlation = relationship between two variables
# + positive correlation -> when one raises, the other one also raises
# - negative correlation ->  when one raises, the other one goes down
# no correlation -> no pattern -> for example, sock color and math grade
# correlation has a value between [-1,1] ->
#
# how to read the graph -> ascending line -> positive correlation
#                       -> descending line -> negative correlation
#                       -> chaotic -> no correlation
# plt.figure(figsize=(7,5))
# sns.scatterplot(x="math score", y="reading score", data=data, hue="gender")
# sns.regplot(x="math score", y="reading score", data=data, scatter=False, color='red')
# plt.title("Correlation between math scores and reading scores")
# plt.show()
# hue -> color the points based on gender

# to make some lines for both genders -> get the genders data, colors for each, iterate through genders  and do a sns.regplot
# genders = data["gender"].unique()
# colors = {"male": "blue", "female": "red"}
# for g in genders:
#     subset = data[data["gender"] == g]
#     sns.regplot(x="math score", y="reading score", data=subset, scatter=False, color=colors[g])
#
# plt.title("Correlation between math scores and reading scores by gender")
# plt.show()

## heatmap - to show the correlation between numerical values as colors
# plt.figure(figsize=(6,5))
## each color represents the correlation between 2 scores
## this is a matrix of 3x3 with combinations of each
# corr = data[["math score","reading score","writing score"]].corr()
## annot = True -> writes the values into each cell
## cmap = "coolwarm" -> uses a color pallet from blue/cold to red/warm
## vmin and vmax -> correlation limits of colors between them
# sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
# plt.title("Corelația dintre scoruri")
# plt.show()

#
# barplot - visual representation of medium values(or other statistics) for categories
# plt.figure(figsize=(7,5))
# sns.barplot(x="gender", y="reading score", data=data, ci=None, palette="muted", hue="race/ethnicity")
# # x - categories, y - values
# # ci = confidence interval
# # can also filter by specifying the hue
# plt.title("Reading score average per gender")
# plt.show()

#pie chart - view proportions of a column/dataset
data['gender'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()

