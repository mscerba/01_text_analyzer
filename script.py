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

uzivatel = {
    'bob' : 123,
    'ann' : 'pase123',
    'mike' : 'password123',
    'liz' : 'pass123'
}

def oddelovac():
    print("-" * 50)


words_title = 0
words_upper = 0
words_lower = 0
words_number = 0


# P1 Pozdrav uzivatele
oddelovac()
print("Vítáme Tě v naši aplikaci, zadej přihlašovací údaje.")


# P2 Pozadejte uzivatele o zadani uzivatelskeho hesla a jmena
name = input("Uživatelské jméno: ")
password = input("Heslo: ")
oddelovac()


# P3 Zkontrolujte jestli uzivatelske jmeno a hesle patri mezi registrovane
def user_check():
    for name_user in uzivatel:
        if name_user == name and str(uzivatel[name_user]) == password:
            return True
    return False


# P4 Pozadejte uzivatele, aby vybral text ze tri moznosti
if user_check() == False:
    print("Zadali jste chybně jméno nebo heslo.")
    exit()
else:
    text_number = int(input("Vyberte jednu z možností textu a zadejte číslo 1 - 3: "))


oddelovac()


# P5 Vypocitat statistiky pro vybrany text
text_lst = TEXTS[text_number-1].split(" ")
text_modified = []

for word in text_lst:
    text_modified.append(word.strip(",.\n"))


# celkovy pocet slov
length_text = len(text_modified)


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

print("Počet všech slov v textu je: {}".format(length_text))
print("Počet slov s počátečním velkým písmenem je: {}".format(words_title))
print("Počet slov s velkými písmeny je: {}".format(words_upper))
print("Počet slov s malými písmeny je: {}".format(words_lower))
print("Počet slov pouze s čísly: {}".format(words_number))

oddelovac()


# P6 Vytvorte sloupcove grafy znazornujici cetnost delek slov
length_words = []
freq_words = {}

for word in text_modified:
    length_words.append(len(word))

length_words.sort()
freq_words = dict.fromkeys(length_words,0)

for word in length_words:
    freq_words[word] = freq_words.get(word, 0) + 1

for key in freq_words:
    print(key, ':', '*' * freq_words[key], freq_words[key])

oddelovac()


# P7 Vypocitejte soucet vsech ciselnych hodnot
suma_number_text = 0

for word in text_modified:
    if word.isdigit():
        suma_number_text += int(word)


print("Součet všech čísel v textu je: {}".format(suma_number_text))


