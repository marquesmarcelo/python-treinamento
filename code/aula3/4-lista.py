nome = ["marcelo", "vania", "catia", "vanda", "laura"]
salario = [100.0, 50.0, 30.0, 40.0, 60.0]

print (nome[1])
print (nome[1:4])
print (nome[-1])
print (nome[-2])
print ("Marcelo" in nome)
nome[0] = "diego"
del nome[4]
print (list(nome))

nomes_adicionais = ["joão", "pedro", "isaque"]

print (nome + nomes_adicionais)

texto = "Que raça de cachorro pula mais alto que um prédio? Qualquer uma, ué. Prédio não pula."
print(texto)
print(texto[0:4])

print (texto.upper())
print (texto.capitalize())
print (texto.split("?"))
print (texto.split(" "))
print (texto.replace("de", ""))

# tupla

produtos = ("arroz", "feijão" , "macarrão")
print (produtos)
print (produtos[0])
