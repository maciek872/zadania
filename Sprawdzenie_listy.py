def sprawdz_liste(lista , liczby_do):
    return [el for el in range(liczby_do) if el not in lista]


print(sprawdz_liste([2,3,4,5,8,6,4,11,23,],23))