rules = """Respeta a los demas. No se permiten insultos ni lenguaje
ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas informacion personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""
kword = input("Ingrese una palabra para buscarla en las reglas ")
rule_list = rules.split("\n")
print([line for line in rule_list if kword in line])
 