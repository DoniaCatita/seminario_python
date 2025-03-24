print("Ingrese una lista de números")
act = int(input("Agregue un número a la lista (0 para terminar): "))
numeros = []
while act: 
    numeros.append(act)
    act = int(input("Agregue un numero a la lista (0 para terminar): "))
for i in numeros:
    if i < 0: break
    else: print(f"{i} ",end="")
