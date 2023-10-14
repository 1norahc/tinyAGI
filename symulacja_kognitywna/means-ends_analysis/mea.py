# Dobry omlet, proba symulacji programu means-ends_analysis

# skladniki potrzebne do zrobienia dobrego omleta
S = {
    "e": 2, # Ilosc jajek 2
    "s": 22.0, # Ilosc cukru (g)
    "p": 15.0, # Ilosc pieprzu (g)
    "c": 5.0, # Ilosc cukru (g) 
}

def omlet(skladniki: dict, 
          rodzaj_patelni: str, 
          dlugosc_pieczenia: int, # 0.05 oznacza 5 minut 
          kuchenka: bool): # True - indukcja, False - gazowa
    
    return skladniki, rodzaj_patelni, dlugosc_pieczenia, kuchenka




print(omlet(skladniki=S, rodzaj_patelni="teflon", dlugosc_pieczenia=0.08, kuchenka=True))
