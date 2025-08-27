from enum import unique

import numpy as np
import pandas as pd

df = pd.read_csv("Income.csv")

incomes = df["income"]
minIncome = np.min(incomes)
maxIncome = np.max(incomes)
averageIncome = np.sum(incomes)/len(incomes)

print("MinIncome", minIncome)
print("MaxIncome: ", maxIncome)
print("AverageIncome: ", averageIncome)

csv_usa = df[df["native-country"] == 'United-States']
average_income_over_30 = csv_usa[csv_usa["age"] > 30]["income"].mean()
print(average_income_over_30)

average_income_below_30 = np.mean(csv_usa[csv_usa['age'] <= 30]['income'])
print(average_income_below_30)
print("-----------------------------------------------------------------------")

# what is the average income for each level of education
education_levels = set(df['education'])
average_income_based_on_education_level = []

for education_level in education_levels:
    education_level_average_income = df[df["education"] == education_level]['income'].mean()
    average_income_based_on_education_level.append({
        "education": education_level,
        "avg_income": education_level_average_income
    })

for entry in average_income_based_on_education_level:
    print(f"Education: {entry['education']}, Avg Income: {entry['avg_income']:.2f}")
print("-----------------------------------------------------------------------")

# what is the most frequent occupation

occupations = set(df['occupation'])
occupation_counts = []
for occupation in occupations:
    count = (df['occupation'] == occupation).sum()
    print("Count:", count)
    occupation_counts.append({
        "occupation": occupation,
        "count": count
    })

for entry in occupation_counts:
    print(f"Occupation: {entry['occupation']}, Count: {entry['count']}")

print("Most frequent occupation:", max(occupation_counts, key=lambda x: x['count']) )
print("-----------------------------------------------------------------------")

# create new column high_income if income > 50 000
df_with_high_income = df.copy()
df_with_high_income['high_income'] = df_with_high_income['income'] > 50_000
df_with_high_income.to_csv('income_with_highest_index.csv', index=False)

df_only_highest_income = df_with_high_income[df_with_high_income['high_income'] == True]
df_only_highest_income.to_csv('df_only_highest_income.csv', index=False)

