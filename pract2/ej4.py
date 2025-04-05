 numbers = ["1","2","3","4","5","6","7","8","9","0"]
mayus = string.ascii_uppercase
minus = string.ascii_lowercase
valid = True
if(len(user_pw) < 5) or (user_pw.count(mayus) == 0) or (user_pw.count(numbers) == 0):
    valid = False
for letter in user_pw:
    if (not letter in numbers) and (not letter in mayus) and (not letter in minus):
        valid = False
if valid:
print("El nombre de usuario es válido.")
else:
print("El nombre de usuario no cumple con los requisitos.")