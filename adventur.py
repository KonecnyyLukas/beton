def tajemny_les():
    print("\nDorazil jsi do Tajemného lesa. Kolem tebe se rozprostírá hustá mlha a slyšíš podivné šepoty.")
    print("Na zemi leží starodávná mapa a o kousek dál vidíš lesknoucí se amulet.")
    volba = input("Co uděláš? (1 = Zvedneš mapu, 2 = Půjdeš prozkoumat amulet): ")

    if volba == "1":
        print("Zvedáš mapu a odhaluješ skrytý průchod lesem. Získáváš 2 body.")
        return 2
    elif volba == "2":
        print("Přiblížíš se k amuletu, ale ten tě oslepí jasným světlem! Ztrácíš 1 bod.")
        return -1

tajemny_les()
