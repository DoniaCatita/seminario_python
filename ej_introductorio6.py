numeros = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1001]
pares = []
impares = []
for n in numeros:
    if n%2==0:
         pares.append(n)
    else: impares.append(n)
print(pares)
print(impares)