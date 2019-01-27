def wygeneruj_liste(od, do):
    for num in range(od, do + 1):
        yield num, num + 0.5

for result in wygeneruj_liste(2,5):
    for num in result :
        print(float(num))

lista = [ float(num) for result in wygeneruj_liste(2,5) for num in result]
print(lista)
