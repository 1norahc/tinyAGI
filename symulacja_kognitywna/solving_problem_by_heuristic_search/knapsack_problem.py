"""Przykład kodu w Pythonie, który rozwiązuje problem plecakowy (knapsack problem) za pomocą heurystycznego przeszukiwania przestrzeni stanów. """

"""
W problemie plecakowym mamy zestaw przedmiotów o określonych wartościach i wagach, 
a celem jest wybranie takich przedmiotów, aby maksymalizować sumę wartości przy zachowaniu 
ograniczenia wagi plecaka.
"""

import random

# Dane wejściowe
n = 10 # Liczba dostepnych przedmiotow
pojemnosc_plecaka = 50

# Generowanie losowych danych dla przedmiotów (wartości i wagi)
random.seed(0) # ustawienie ziarna losowości dla reprodukowalności

wartosci = [random.randint(1, 50) for _ in range(n)]
wagi = [random.randint(1,10) for _ in range(n)]

def heurystyczne_rozwiazanie(pojemnosc, wartosci, wagi):
    n = len(wartosci)
    rozwiazanie = [0] * n  # Początkowe rozwiazanie - wszystkie przedmioty są odrzucane
    pozostala_pojemnosc = pojemnosc

    # Sortowanie przedmiotów według stosunku wartości do wagi (najlepsze stosunki na początek)
    stosunek = [v / w for v, w in zip(wartosci, wagi)]
    uporzadkowane_indeksy = sorted(range(n), key=lambda i: stosunek[i], reverse=True)

    for i in uporzadkowane_indeksy:
        if wagi[i] <= pozostala_pojemnosc:
            rozwiazanie[i] = 1  # Przedmiot jest wybierany
            pozostala_pojemnosc -= wagi[i]

    return rozwiazanie

# Rozwiązanie problemu plecakowego za pomocą heurystyki
rozwiazanie = heurystyczne_rozwiazanie(pojemnosc_plecaka, wartosci, wagi)

# Obliczanie łącznej wartości i wagi wybranych przedmiotów
suma_wartosci = sum(wartosci[i] for i in range(n) if rozwiazanie[i])
suma_wag = sum(wagi[i] for i in range(n) if rozwiazanie[i])

# Wyświetlenie wyników
print("Wybrane przedmioty:", rozwiazanie)
print("Maksymalna wartość:", suma_wartosci)
print("Suma wag:", suma_wag)


"""
Ten kod generuje losowe dane dla elementów, a następnie wykorzystuje heurystykę 
do sortowania elementów według wartości/wagi w kolejności malejącej. 
Następnie wybierze przedmioty, zaczynając od tych z najwyższą stawką, 
aż do osiągnięcia maksymalnej pojemności plecaka. Ostateczne rozwiązanie zawiera 
informację o wybranych elementach, wartości maksymalnej  oraz łącznej masie wybranych 
elementów. To  tylko prosty przykład, ale ilustruje, jak można wykorzystać heurystyczne 
przeszukiwanie przestrzeni stanów  do rozwiązywania problemów optymalizacyjnych.
"""