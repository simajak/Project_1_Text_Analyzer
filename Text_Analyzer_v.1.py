'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

divider = "-" * 42 # Snad to bude stačit...

reg_users = {"bob" : "123",
             "ann" : "pass123",
             "mike" : "password123",
             "liz" : "pass123"}

# Uživatel zadá jméno a heslo
username = input("Username: ")
password = input("Password: ")

# Kontrola, jestli je uživatel zaregistrovaný
if reg_users.get(username) == password:
    print(divider)
    print(f"Welcome to the app, {username}!")
    print("We have 3 texts to be analyzed.")
    print(divider)

# Když neni zaregistrovaný
else:
    print("Unregistered user, terminating the program...")
    quit()

# Zadání čísla textu (int!)
text_number = input("Enter a number btw. 1 and 3 to select: ")
if text_number.isalpha():
    print("Invalid entry, terminating the program...")
    quit()
elif int(text_number) not in range(1,4):
    print("Invalid entry, terminating the program...")
    quit()
else:
    print(divider)

# Je potřeba upravit číslo textu kvůli indexování v seznamu TEXTS
corrected_text_number = int(text_number) - 1

# Příprava na vyčištěné textu (corrected_text_number = index)
text = TEXTS[corrected_text_number]
cleaned_text = []
cleaned_text_no_lower = []
words = []
numbers = []
word_num = []

for word in text.split(): # seznam slov
    cleaned_text.append(word.strip(".,:;").lower())

# Rozdělení na "slova" a "čísla"
for word in cleaned_text:
    if word.isalpha():
        words.append(word)
    elif word.isnumeric():
        numbers.append(word)
    elif word.isalnum(): # vykopne text, který neni alpha nebo num
        word_num.append(word)
    else:
        continue

# spočítat výskyt pro každé slovo = musim si vyrobit ! slovníky !
word_count = {}
number_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] =+ 1

for number in numbers:
    if word not in number_count:
        number_count[number] = 1
    else:
        number_count[number] =+ 1


# Výpočet slov, čísel, ...
word_upper = []
word_lower = []
word_title = []

word_total = len(words) + len(numbers) + len(word_num)
print(f"There are {word_total} words in the selected text.")

for word in text.split():
    cleaned_text_no_lower.append(word.strip(".,:;"))

for word in cleaned_text_no_lower:
    if word.isalpha() and word.isupper():
        word_upper.append(word)
    elif word.isalpha() and word.islower():
        word_lower.append(word)
    elif word.istitle():
        word_title.append(word)
    else:
        continue


print(f"There are {len(word_title)} titlecase words.")
print(f"There are {len(word_upper)} uppercase words.")
print(f"There are {len(word_lower)} lowercase words.")

num_string = len(numbers)
print(f"There are {num_string} numeric strings.")

num_int = [int(number) for number in numbers]
num_sum = sum(num_int)
print(f"The sum of all the numbers is {num_sum}.")

print(divider)

#Výpis výsledku uživateli

result = dict()
for word in cleaned_text:
    len(word)


print(cleaned_text)
print(word_occ)
print(result)
print(f"LEN|  OCCURENCES  |NR.")

for index, value in enumerate(sorted(word_occ), 1):
    print(f"{index:^3}|{len(value) * '*':<14}|{len(value)}")

