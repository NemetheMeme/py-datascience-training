import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder

# 1. determine the correlation between the 3 scores
# take combination of 2 for all 3
# select the ones that have the best correlation

data = pd.read_csv("exams.csv")
fig, subplots = plt.subplots(1,3)
fig.set_size_inches((10,7))
columns = ['math score','reading score','writing score']
subplots = subplots.flatten()
# for i in range (3):
#     for j in range (3):
#         subplots[i,j].plot(data[columns[i]], data[columns[j]])
#         subplots[i,j].set_title(columns[i] + " " + columns[j])

k = 0
for i in range(len(columns)):
    for j in range(i+1, len(columns)):
        subplots[k].scatter(data[columns[i]], data[columns[j]], alpha=0.6)
        sns.regplot(x=data[columns[i]], y=data[columns[j]], data=data, scatter=False, color='red', ax=subplots[k])

        subplots[k].set_xlabel(columns[i])
        subplots[k].set_ylabel(columns[j])
        subplots[k].set_title(f"{columns[i]} vs {columns[j]}")
        k += 1

# fig.tight_layout()
# plt.show()

best_corr = -1
best_pair = None

for i in range(len(columns)):
    for j in range(i+1, len(columns)):
        corr = data[columns[i]].corr(data[columns[j]])
        print(f"Correlation between {columns[i]} și {columns[j]}: {corr:.2f}")
        if corr > best_corr:
            best_corr = corr
            best_pair = (columns[i], columns[j])

print(f"\nBest correlation happens between {best_pair[0]} and {best_pair[1]}: {best_corr:.2f}")

# observe the distribution on classes of binary/categorical variables and distribution of continuous variables, using the right graphs

categorical_columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
dependent_vars = columns.copy()

# for categorical columns = piechart or barplot

fig, axes = plt.subplots(2,len(categorical_columns), figsize=(25,10))
axes = axes.flatten()
for i, column in enumerate(categorical_columns):
    sns.countplot(x=column, data=data, ax=axes[i])
    axes[i].set_title(f'Distribution {column}')
    axes[i].tick_params(axis='x', rotation=45)

    counts = data[column].value_counts() # counts every value for the specified column
    axes[i+len(categorical_columns)].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    axes[i+len(categorical_columns)].set_title(f'Pie: {column}')


# plt.tight_layout()
# plt.show()

# continue values
continue_figure, continue_axes = plt.subplots(1, len(dependent_vars), figsize=(15, 5))
continue_axes = continue_axes.flatten()
for i, column in enumerate(dependent_vars):
    sns.histplot(data=data, x = data[column], ax=continue_axes[i], bins=5, kde=True, color='red')
    continue_axes[i].set_title(f'Distribution {column}')
    continue_axes[i].tick_params(axis='x', rotation=45)

# plt.tight_layout()
# plt.show()

# using boxplots, show the distribution of each score based on every category

box_figures, box_axes = plt.subplots(len(dependent_vars), len(categorical_columns), figsize=(25, 15))
box_axes = box_axes.flatten()

k = 0
for i, score in enumerate(dependent_vars):
    for j, column in enumerate(categorical_columns):
        sns.boxplot(data=data, x=column, y=score, ax=box_axes[k])
        box_axes[k].set_title(f'{score} vs {column}')
        box_axes[k].tick_params(axis='x', rotation=45)
        k += 1

# plt.tight_layout()
# plt.show()

# extra: visualize the datas in a way more 'elegant way'
# histogram and kde curve
plt.figure()
# sns.displot(data['math score'], rug=True, kind = 'hist', kde=True, color='red')
sns.displot(data['math score'], rug=True, kind = 'ecdf', color='red')
# plt.show()

# encode categorical values and show the correlations between each

dataframe_encoded = data.copy()
for column in categorical_columns:
    le=LabelEncoder()
    dataframe_encoded[column] = le.fit_transform(dataframe_encoded[column])

# create the correlation matrix
corr_matrix = dataframe_encoded.corr()
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt= ".4f")
plt.title("Correlation Matrix")

# identify the best 3 correlations

for dep in dependent_vars:
    correlations = corr_matrix[dep].drop(dependent_vars)
    top3 = correlations.abs().sort_values(ascending=False).head(3)
    print(f'Top 3 correlations for {dep}')
    print(top3)
    print()

plt.show()