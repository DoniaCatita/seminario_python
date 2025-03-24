numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 6, 9, 300, 33333333333333]
texto = ""
for n in numeros:
    if(n % 3 != 0):
        texto += str(n)
        texto += " - "
texto = texto[0:-3:1]
print(texto)