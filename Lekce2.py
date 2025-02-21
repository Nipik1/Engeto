# 1
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]

posledni_index = len(zamestnanci) - 1
print(f"Na indexu 2 je {zamestnanci[2]}")
print(f"Na {posledni_index} indexu je: {zamestnanci[-1]} ")
print(f"Na indexu od 2 do 5 je: {zamestnanci[2:6]}")
print(f"Každý třetí člen je {zamestnanci[::3]}")

## 2

jmeno = "Tomáš"
vaha = 80
vyska = 200
prepocet = vyska / 100
bmi = vaha / prepocet ** 2

if bmi > 40:
    kategorie = "těžká obezita"
elif bmi > 30:
    kategorie = "obezita"
elif bmi > 25:
    kategorie = "mírná nadváha"
elif bmi > 18.5:
    kategorie = "zdravá váha"
else:
    kategorie = "podvýživa"

print(f"{jmeno}e tvo BMI je {bmi} což spadá do kategorie {kategorie}")

### 3 

zamestnanci = ["František", "Anna", "Jakub", "Klára"]
print(f"Zaměstnanci na začátku {zamestnanci}")

zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")

print(f"Nová jména přidána {zamestnanci_a}")

zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")

print(f"Nová jména vložena {zamestnanci_b}")

#### 4 

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = 3

if cislo_dne in vstupni_cisla:
    print("Správní vstupní hodnota")
    
    den_tydne = tyden[cislo_dne - 1]

    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        print("Správné písmeno")
    else:
        print("Špatné číslo")
else:
    print("Neplatný vstup")