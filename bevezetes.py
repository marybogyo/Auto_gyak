def auto_adat():
    auto_nev = input("I/A:\n\t Autó neve: ")
    gyartasi_ev = int(input("\t Gyártási dátum: "))
    if gyartasi_ev == 2023:
        print(f"I/B: \n\t Ez az {auto_nev} friss gyártás.")
    elif gyartasi_ev < 2000:
        print(f"I/B: \n\t Ez az {auto_nev} öreg autó.")
    else:
        print(f"I/B: \n\t Ez az {auto_nev} átlagos korú.")