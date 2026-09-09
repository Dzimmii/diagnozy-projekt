import json
import unicodedata
import customtkinter as ctk
import sys
import os

def cesta_k_souboru(nazev_souboru):
    if hasattr(sys, '_MEIPASS'):
        # Program běží jako zabalené .exe
        return os.path.join(sys._MEIPASS, nazev_souboru)
    else:
        # Program běží normálně (z VS Code)
        return nazev_souboru

def odstran_diakritiku(text):
    return ''.join(
        znak for znak in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(znak)
    )

with open(cesta_k_souboru("diagnozy.json"), "r", encoding="utf8") as soubor:
    diagnozy = json.load(soubor)

def hledat():
    vystup.configure(state="normal")  # odemkni, aby šlo vkládat
    vystup.delete("1.0", "end")  # smaže předchozí výsledky
    hledane_slovo = odstran_diakritiku(vstup.get().lower())
    nalezeno = False

    for kod, nazev in diagnozy.items():
        if hledane_slovo in odstran_diakritiku(nazev.lower()):
            vystup.insert("end", f"{kod:<8}{nazev}\n")
            nalezeno = True

    if not nalezeno:
        vystup.insert("end", "Zadaný název diagnózy není v databázi.")

    vystup.configure(state="disabled") 


# --- GUI ---
app = ctk.CTk()
app.title("Vyhledávač diagnóz MKN-10")
app.geometry("700x400")

vstup = ctk.CTkEntry(app, placeholder_text="Zadej název diagnózy")
vstup.bind("<Return>", lambda event: hledat())
vstup.pack(pady=10, padx=10, fill="x")

tlacitko = ctk.CTkButton(app, text="Hledat", command=hledat)
tlacitko.pack(pady=5)

vystup = ctk.CTkTextbox(app, font=("Courier New", 13))
vystup.pack(pady=5, padx=5, fill="both", expand=True)
vystup.configure(state="disabled")  # zase zamkni pro uživatele


app.mainloop()