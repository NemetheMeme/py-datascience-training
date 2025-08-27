import pandas as panda
import numpy

data = panda.read_csv('Income.csv')

# compare income average for persons below 30 and over 50
under_30 = data[data['age'] < 30]
over_50 = data[data['age'] > 50]

print(f"Comparison: under 30: {under_30['income'].mean():.2f} vs over 50: {over_50['income'].mean():.2f}")

# first 5 occupations with  biggest average capital-gain
# First way - longer
data_filtered_by_capital_gain = data[data['capital-gain'] > 0]
# for each occupation get the capital gain average
occupations = set(data_filtered_by_capital_gain['occupation'])

average_capital_gain_per_occupation = []

for occupation in occupations:
    average_capital_gain = data_filtered_by_capital_gain[data_filtered_by_capital_gain['occupation'] == occupation]['capital-gain'].mean()
    average_capital_gain_per_occupation.append({"occupation": occupation, "avg-capital-gain": average_capital_gain})

average_capital_gain_per_occupation = sorted(average_capital_gain_per_occupation, key= lambda x : x['avg-capital-gain'], reverse=True)

for entry in average_capital_gain_per_occupation[:5]:
    print(f"Occupation: {entry['occupation']}, Count: {entry['avg-capital-gain']}")

# second way - faster
top5_capital_gain = (
    data[data['capital-gain']>0]  # filter the data -> data that has capital-gain
    .groupby('occupation')['capital-gain'] # for each occupation, gather the capital-gain -> select capital-gain column for each occupation and group them together
    # looks like: Doctor -> capital-gain[100,200,300]
    #             Engineer -> capital-gain[500,1000,200]
    .mean() # get the average
    .sort_values(ascending=False)
    .head(5) # takes the first 5 values from the head
)

print(top5_capital_gain)

# differences between average income of women vs average income of men
income_by_gender = data.groupby('gender')['income'].mean()
print(income_by_gender)

# how many persons with an education of Bachelors earn over 50k
bachelors_income_over_50k_count = data[(data['education'] == 'Bachelors') & (data['income'] > 50000)].shape[0]
# shape[1] takes the number of columns, shape[0]takes the number of rows
# if using .count() -> will also count the NaN rows, count is used on a specific column
# usually len(data..) is also used
print(bachelors_income_over_50k_count)
print('Persons with a Bachelor\'s education that earn over 50000: ',bachelors_income_over_50k_count)