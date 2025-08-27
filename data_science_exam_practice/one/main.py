numbers = [1,12,65,34,85,234,634,12,86,231,546]

# sum of last 5 numbers from the list

sum_of_last_5_numbers = sum(numbers[len(numbers)-5:])
print(sum_of_last_5_numbers)

# average of the lowest 3 numbers
sorted_numbers = sorted(numbers)
average = sum(sorted_numbers[:3])/3
print(average)

# odd numbers
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)

# dictionary
students = [
    {"name":"Ionescu","grade": 4},
    {"name":"Popescu","grade": 9},
    {"name":"Georgescu","grade": 7}
]

passed_students = [student for student in students if student["grade"] >=5]
print(passed_students)

# 2 lists for vowel and consonants
basic_vowels = ["a", "e", "i", "o", "u"]
phrase = "Timpul petrecut de profesor pentru a explica ceva este invers proportional cu informatia retinuta de studenti."

words = phrase.split()
words_start_vowel = [word for word in words if word[0].lower() in basic_vowels]
words_start_consonant = [word for word in words if word[0].lower() not in basic_vowels]

print("Words starting with a vowel:", words_start_vowel)
print("Words starting with a consonant:", words_start_consonant)
