# Initializez lista pentru cărti
carti = []

# Funcția pentru adăugarea unei cărți
def adauga_cartea(carti):
    while True:
        try:
            titlu = input("Introdu titlul cărții: ")
            autor = input("Introdu numele autorului: ")
            evaluare = int(input("Introdu evaluarea cărții (1-5): "))
            if evaluare < 1 or evaluare > 5:
                raise ValueError("Evaluarea trebuie să fie între 1 și 5")
            cartea = {"titlu": titlu, "autor": autor, "evaluare": evaluare}
            carti.append(cartea)
            print("Cartea a fost adăugată cu succes!")
            break
        except ValueError as e:
            print(f"Input invalid! {e}. Încercați din nou.")

# Funcția pentru afișarea cărților
def afiseaza_cartile(carti):
    if not carti:
        print("Nu există cărți adăugate în listă!")
    else:
        print("\nLista cărților: ")
        for i, item in enumerate(carti, start=1):
            print(f"{i}. Titlul: {item['titlu']}, Numele autorului: {item['autor']}, Evaluarea ta: {item['evaluare']}")

# Funcția pentru ștergerea unei cărți după titlu
def sterge_cartea(carti):
    titlu_de_sters = input("Introdu titlul cărții care dorești să fie ștearsă din listă: ")
    numarul_cartilor_initiale = len(carti)
    carti[:] = [item for item in carti if item['titlu'] != titlu_de_sters]
    if len(carti) < numarul_cartilor_initiale:
        print(f"Cartea cu titlul '{titlu_de_sters}' a fost ștearsă din listă!")
    else:
        print("Nu există în lista ta cartea cu titlul introdus!")

# Funcția pentru căutarea unei cărți
def cauta_cartea(carti):
    carte_cautata = input("Introdu titlul cărții pe care o cauți: ")
    gasit = False
    for item in carti:
        if item['titlu'] == carte_cautata:
            print(f"Titlul: {item['titlu']}, Numele autorului: {item['autor']}, Evaluarea ta: {item['evaluare']}")
            gasit = True
            break
    if not gasit:
        print("Nu există în lista ta cartea cu titlul introdus!")

# Meniu principal
def main():
    while True:
        print("\n--- Jurnal de cărți ---")
        print("1. Adaugă o carte")
        print("2. Afișează toate cărțile")
        print("3. Șterge o carte")
        print("4. Caută o carte")
        print("5. Ieșire")
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            adauga_cartea(carti)
        elif optiune == "2":
            afiseaza_cartile(carti)
        elif optiune == "3":
            sterge_cartea(carti)
        elif optiune == "4":
            cauta_cartea(carti)
        elif optiune == "5":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă, încearcă din nou!")

# Rulez meniul principal
main()

