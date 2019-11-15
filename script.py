TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

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

UZIVATEL = {
    'bob': '123',
    'ann': 'pase123',
    'mike': 'password123',
    'liz': 'pass123'
}


ODDELOVAC = "-" * 50


# P1 Pozdrav uzivatele
print(ODDELOVAC)
print("Vítáme Tě v naši aplikaci, zadej přihlašovací údaje.")


# P2 Pozadejte uzivatele o zadani uzivatelskeho hesla a jmena + overeni
swith = True

while swith:
    name = input("Uživatelské jméno: ")
    password = input("Heslo: ")

    if name not in UZIVATEL.keys():
        print("Zadali jste chybně jméno")
    elif UZIVATEL[name] != password:
        print('Zadali jste chybně heslo')
    else:
        text_number = int(input("Vyberte jednu z možností textu a zadejte číslo 1 - 3: "))
        swith = False

print(ODDELOVAC)


# P5 Vypocitat statistiky pro vybrany text
text_lst = TEXTS[text_number-1].split()
text_modified = []

text_modified = [word.strip(",.\n") for word in text_lst]



# celkovy pocet slov
length_text = len(text_modified)
words_title = 0
words_upper = 0
words_lower = 0
words_number = 0
length_words = []
freq_words = {}
i = 0

while i < length_text:
    # pocet slov zacinajici velkym pismenem
    if text_modified[i].istitle():
        words_title += 1
        i += 1
    # pocet slov velkymi pismeny
    elif text_modified[i].isupper() and text_modified[i].isalpha():
        words_upper += 1
        i += 1
    # pocet slov malymi pismeny
    elif text_modified[i].islower() and text_modified[i].isalpha():
        words_lower += 1
        i += 1
    # pocet samostatnych cisel v textu
    elif text_modified[i].isdigit():
        words_number += 1
        i += 1
    else:
        i += 1

text_result = ['Počet všech slov v textu je: ',
               'Počet slov s počátečním velkým písmenem je: ',
               'Počet slov s velkými písmeny je: ',
               'Počet slov s malými písmeny je: ',
               'Počet slov pouze s čísly: ']

text_value = [length_text, words_title, words_upper, words_lower, words_number]

for index, text in enumerate(text_result):
    print(text, text_value[index])

print(ODDELOVAC)


# P6 Vytvorte sloupcove grafy znazornujici cetnost delek slov
suma_number_text = 0

for word in text_modified:
    length_words.append(len(word))
    if word.isdigit():
        suma_number_text += int(word)

length_words.sort()
freq_words = dict.fromkeys(length_words, 0)

for word in length_words:
    freq_words[word] = freq_words.get(word, 0) + 1

for key in freq_words:
    if key < 10:
        key_str = '0' + str(key)
    print(key_str, ':', '*' * freq_words[key], freq_words[key])

print(ODDELOVAC)

print(text_modified)
print(length_words)


print("Součet všech čísel v textu je: {}".format(suma_number_text))
