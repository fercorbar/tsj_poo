# Ciclos o bucles

# for
for i in range(5):
    print(i)

# for con break
for i in range(5):
    if i == 3:
        break
    print(i)

# for con lista
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

# for con diccionario
diccionario = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
for key, value in diccionario.items():
    print(key, value)


# while
i = 0
while i < 5:
    print(i)
    i += 1

