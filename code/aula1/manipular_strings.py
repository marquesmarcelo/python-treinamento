texto = "    estamos tentando trabahar com strings, olha que lega!   "

print (texto)

print ("Fatia 10 ate 15:", texto[10:15])

print ("Tamanho:", len(texto))

print ("split:", texto.split(","))

print("Replace:", texto.replace("tentando", "buscando"))

print("Strip:", texto.strip())

print ("Upper case:", texto.upper())

print ("Procurar", texto.find("olha"))

print ("Count letras a:", texto.count("a"))