import sys
# Algorytm realizujący map reduce dla macierz-wektor
#   Pobierz wektor w postaci [wiersz] [wartość]
#   Pobierz niezerowe elementy macierzy w postaci [kolumna] [wiersz] [wartość]
#       Dla każdego elementu wywal na wyjście [kolumna] [wartość macierzy] [wartość wektora]
#   Sortuj po pierwszym elemencie wejścia
#   W reduce sumuj wszystkie wejścia pomnożone dla wiersza macierzy przemnożone przez wektor z tego samego wejścia

vector = dict()
# Wczytanie i obrobienie linii.
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    # Jeśli to wektor dopisz do wektora klucz o numerze [wiersz] i dopisz wartość [wartość].
    if len(line) == 2:
        vector[line[0]] = line[1]
        continue
    # Jeśli to macierz pobierz kolumnę, wiersz, wartość.
    column = line[0]
    row = line[1]
    value = line[2]
    result = str(int(value) * int(vector[column]))

   # print(' w wierszu ' + str(row ) +' wartosc wektora ' + str(vector[column])  )
   # print(' W macierzy w kolumnie ' + str(column) + 'mam wartosc ' + str(value) + 'co po przemnozeniu powinno byc ' + str(result))
    print(column + '\t' + result)

#previous_row = -1
#result = 0
#for line in sys.stdin:
#    line = line.strip()
#    line = line.split()
#    row = line[0]
#    print(row)
#    if row == previous_row:
#        pass