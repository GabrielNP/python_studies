# -*-coding:utf-8-*-
# Dicionários = array associativo, ou seja, um determinado valor passa a ser vinculado a uma chave.
# São conjuntos de pares chave-valor
# Ex: dicionario_sites = {"Diego": "diegomariano.com"}

dicionario = {
    "A":"Ameixa",
    "B":"Bola",
    "C":"Cachorro"
}

print(dicionario)

# Erro aqui
# print("Erro aqui: ", dicionario[0])

print(dicionario["A"])
print(dicionario["B"])
print(dicionario["C"])

for chave in dicionario:
    print(chave + ":" + dicionario[chave])

for i in dicionario.items():
    print(i)

for j in dicionario.values():
    print(j)

for z in dicionario.keys():
    print(z)

telefones={"gabriel":1197228521,"tadeu":1197228522,"osvaldo":1197228523}
telefones

# Adicionar
telefones["rita"]=11972228524
telefones

# Remover
del telefones["tadeu"]
telefones


person1 = {"Fulano": 39}
person2 = {"Beltrano": 25}
person3 = {"Ciclano": 42}
print()
people = [person1, person2, person3]

person1["Beltrano"]=25
person1["Ciclano"]=42
print(person1['Fulano'])