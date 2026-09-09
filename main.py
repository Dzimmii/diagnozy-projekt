import json
import unicodedata

def odstran_diakritiku(text):
    return ''.join(
        znak for znak in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(znak)
    )

with open("diagnozy.json", "r", encoding="utf8") as soubor:
    diagnozy = json.load(soubor)

hledane_slovo = odstran_diakritiku(input("Zadej název diagnózy: ").lower())
nalezeno = False

for kod, nazev in diagnozy.items():
    if hledane_slovo in odstran_diakritiku(nazev.lower()):
        print(f"{kod:<8}   {nazev}")
        nalezeno = True

if not nalezeno:
    print("Zadaný název diagnózy není v databázi.")
          
    