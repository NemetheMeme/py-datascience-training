# Formatting print, declaration of inline object/dictionary and accessing its fields,
# placeholders can also be used, and also used in multiple places
print('This is an example of number: {first}, an example of a String: {second},'
      ' and an example of an object: {object[number_factor]}, and another number: {first}'
      .format(first=12, second="Andrei", object={"name": "DefaultName",
                            "number_factor": "DefaultNumber"})
      )

print('This is an example of number: {}, an example of a String: {}, and an example of an object: {object}'
      .format(12, "Andrei", object={"name": "DefaultName",
                            "number_factor": "DefaultNumber"}['name'])
      )
# accessing a sequence from an array
# for example for strings
full_array = 'this_is_a_full_character_sequence'
characters_between_indexes = full_array[5:12]  # index 12 not included
characters_starting_with_index = full_array[5:] # index 5 is included
characters_until_index = full_array[:10] # index 10 not included
all_characters_without_last_index = full_array[:-1]
last_index = full_array[-1]

print('full_array - ', full_array)
print('characters_between_indexes_5_and_12 - ', characters_between_indexes)
print('characters_starting_with_index_5 - ', characters_starting_with_index)
print('characters_until_index_10 - ', characters_until_index)
print('all_characters_without_last_index - ', all_characters_without_last_index)

# inversing a String
inverted_full_array = full_array[::-1]
# can also be used with different steps :
# reverse step ::-step - ::-2 abcdef => fdb
# normal step ::step - ::2 abcdef => ace
print("inverted_full_array - ", inverted_full_array)

# returns a set of the array
array_set = set({1,2,3,4,5,6,6,67,})
print(array_set)

# boolean operators and, or to check multiple conditions
if (1 > 2) or  (3 < 4):
    print("true")

# tuple:
t = (1,2,3) # immutable
# dictionary can be modified

# for loop
for num in {1,2,3,4,6}:
    print(num)
i = 1
while i < 5:
    print(i)
    i = i + 1

# for a specified amount of times
for j in range(0,5):
    print("j is {j}".format(j = j))

# can make a list of the range:
ranged_list = list(range(0, 4))
print(ranged_list)

# important - LIST COMPREHENSION
#[ do this for element in list] and append each element to a list

comprehended_list = [x * 3 for x in [1, 2, 3, 4]]
print("list_comprehension: ", comprehended_list)

# or [appendedElementOrWhatItReturns for element in elements if condition]
##odd_numbers = [number for number in numbers if number % 2 == 1]

# functions
def func(param):
    print("Function: ", param)
func(12)

# map
# map(func, iterable) -> applies the func over all items of the iterable
# to actually get a list from it => list(map(func, iterable))

# lambda expressions
lambdanum = lambda num: num*3
lambda_list = list(map(lambdanum, [1,2,3,4,5]))
print("lambda_list: ", lambda_list)

# filter -> filter(lambda or func, iterable)

# split, splits a string based on either space or specified character