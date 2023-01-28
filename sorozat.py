import random

szam_lista = []

def egyjegyuek_szama():
    i = 0
    szamok = ""

    while i < 5:
        vel = int(random.random() * 89) + 1
        szam_lista.append(vel)
        szamok += str(vel)
        if i != 4:
            szamok += ";"

        i += 1
    #print("-".join(szam_lista))
    print(f"II/A, B, C\n\t {szamok}")


def egyjegyuek():
    i = 0
    egyjegy_darab = 0
    while i < len(szam_lista):
        if szam_lista[i] < 10:
            egyjegy_darab += 1
        i += 1
    return egyjegy_darab


def konzol_kiir():
    print(f"II/D, E: \n\t 	Az egyjegyűek száma : {egyjegyuek()}")


def file_kiir():
    fajl = open("szamok.txt", "w", encoding="utf-8")
    fajl.write(f"II/F:\n\t Az egyjegyűek száma : {egyjegyuek()}")
    fajl.close()