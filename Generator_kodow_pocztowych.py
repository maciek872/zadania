def generator_kodów(str_1, str_2):
    str_1 = int(''.join([el for el in str_1 if el != '-']))
    str_2 = int(''.join([el for el in str_2 if el != '-']))
    for num in range(str_1, str_2 + 1):
        num = str(num)
        yield '-'.join((num[:2],num[2:]))


for result in generator_kodów("79-900", "80-155"):
    print(result)

lista_kodów = [result for result in generator_kodów('79-900', '80-155')]
print(lista_kodów)
