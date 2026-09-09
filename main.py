import json

with open("diagnozy.json", "r", encoding="utf8") as soubor:
    diagnozy = json.load(soubor)

hledane_slovo = input("Zadej název diagnózy: ")
nalezeno = False

for kod, nazev in diagnozy.items():
    if hledane_slovo.lower() in nazev.lower():
        print(f"{kod}   {nazev}")
        nalezeno = True

if not nalezeno:
    print("Zadaný název diagnózy není v databázi.")
          
    