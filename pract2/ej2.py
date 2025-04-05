
titles = [
"Speedrun de Super Mario en tiempo record",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Musica en vivo: improvisaciones al piano"
]
title_words = []
max_len = 0
ans = ""
for title in titles:
word_list = title.split(" ")
if len(word_list) > max_len:
max_len = len(word_list)
ans = title
 
print("el titulo mas largo es: {}".format(ans))
 