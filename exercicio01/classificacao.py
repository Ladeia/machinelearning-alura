porco1    = [1, 1, 0]
porco2    = [1, 1, 0]
porco3    = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 1, 0]
misterioso4 = [0, 0, 0]
misterioso5 = [0, 0, 1]

marcacoes_teste = [-1, 1, 1, 1, -1]
from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misteriosos = [misterioso1, misterioso2, misterioso3, misterioso4, misterioso5]
resultado = modelo.predict(misteriosos)

print(resultado)

erros = resultado - marcacoes_teste
print(erros)

acertos = [erro for erro in erros if erro == 0]
print(acertos)

total_acertos = len(acertos)
total_elementos = len(misteriosos)

print("Total de elementos: "+str(total_elementos))
print("Total de acertos: "+str(total_acertos))

taxa_acertos = 100.0 * (total_acertos / total_elementos)

print("Taxa de acerto: "+str(taxa_acertos))
