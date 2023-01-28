from Auto import Auto
auto_lista = []

def beolvas():
    fajl = open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    #print(sorok)

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        auto_lista.append(Auto(sor))
        i += 1
    #print(auto_lista[1].datum)
    return auto_lista


def auto_szama():
    return len(auto_lista)


def legfiatalabb_auto(): #itt telt le az 1 óra
    i = 0
    fiatalabb = auto_lista[0]
    while i < len(auto_lista):
        if auto_lista[i].datum > fiatalabb.datum:
            fiatalabb = auto_lista[i]
        i += 1
    return fiatalabb