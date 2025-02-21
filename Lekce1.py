slovo = "indexování"

#Prvních 5 písmen slova 'indexování'
#posledních 5 písmen slova 'indexování',
#každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i"),
#všechny výstupy zapiš přímo do funkce print,

#Prvních 5 písmen:
#index
#Posledních 5 písmen:
#ování
#Každé 3. písmeno (počínaje prvním) od 'i':
#ieví

print(slovo[0:5])
print(slovo[5:])
print(slovo[0:10:3])


kg_lb = 2.20 #
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80 #
km_pocet = 54
l_pocet = 5

kg_prepocet = kg_lb * kg_pocet
print(f"{kg_pocet} kg je {kg_prepocet} lb")

km_prepocet = km_mile * km_pocet
print(f"{km_pocet} km je {km_prepocet} mil")

l_prepocet = l_gal * l_pocet
print(f"{l_pocet}l je {l_prepocet} galonů")

mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = (rolls_royce * 2) + (vybava * 2)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

print(f"Sleva na Mercedes: {sleva_merc}")
print(f"Cena za dva Mercedesy je: {cena_2_merc}")
print(f"Cena za Mercedes a Rolls-Royce: {cena_merc_rolls}")
print(f"Cena za dva Rolls-Royce s příplatkovou výbavou: {cena_2_rolls_s_vybavou}")
print(f"Cena za Mercedes s příplatkovou výbavou: {cena_merc_s_vybavou}")
print(f"Cena za Mercedes po slevě: {merc_se_slevou}")


jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = cele_jmeno #len
print(cele_jmeno)
print(len(delka_jmena))
print(6 * "=")
print(cele_jmeno)
print(6 * "=")