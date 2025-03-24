edad = input("ingrese su edad")
if edad.isnumeric(): 
    edad = int(edad)
else : exit(1)
if(edad < 100):
    print(f"le falta(n) {100-edad} año(s) para alcanzar los 100 años")
else: print("Usted ya alcanzó los 100 años, felicidades!!!")