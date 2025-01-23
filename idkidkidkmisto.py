class Misto:
    def __init__(self, nazev, popis, predmety=None):
        self.nazev = nazev
        self.popis = popis
        self.predmety = predmety if predmety else []

    def popsat(self):
        print(f"{self.nazev}\n{'-' * len(self.nazev)}")
        print(self.popis)
        if self.predmety:
            print("\nVidíš následující předměty:")
            for predmet in self.predmety:
                print(f"- {predmet}")
        else:
            print("\nNení zde žádný předmět.")

    def odebrat_predmet(self, predmet):
        if predmet in self.predmety:
            self.predmety.remove(predmet)
            return predmet
        else:
            return None

def navstiv_misto():
    print("Cestuješ neznámou krajinou, když se před tebou objeví zajímavé místo...")

    misto = Misto(
        nazev="Zapomenutá svatyně",
        popis="Stará kamenná svatyně, obklopená mechem a kapradím. Vzduch je chladný a vlhký, a všude panuje zvláštní ticho.",
        predmety=["svícen", "starý svitek", "zlatý prsten"]
    )

    misto.popsat()

    while True:
        akce = input("\nCo chceš udělat? (napiš 'vezmi [předmět]' nebo 'konec'): ").strip().lower()
        if akce == "konec":
            print("Odcházíš z místa. Díky za návštěvu!")
            break
        elif akce.startswith("vezmi "):
            nazev_predmetu = akce.split("vezmi ", 1)[1]
            predmet = misto.odebrat_predmet(nazev_predmetu)
            if predmet:
                print(f"Vzal jsi {predmet}.")
            else:
                print(f"{nazev_predmetu} zde není.")
        else:
            print("Neplatná akce. Zkus 'vezmi [předmět]' nebo 'konec'.")

if __name__ == "__main__":
    navstiv_misto()
