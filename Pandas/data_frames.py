import pandas as pd
# pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# Somente um é obrigatório para se criar um DataFrame com dados, o parâmetro data=XXXX. 
# Pode receber, um objeto iterável, como uma lista, tupla, um dicionário ou um DataFrame, vejamos os exemplos.

# CONSTRUTOR DATAFRAME COM LISTA

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

dados = list(zip(lista_nomes, lista_idades, lista_emails )) # cria uma lista de tuplas # ('howard', 32, 'risus.varius@dfictumPhasellusin.ca') 

print(dados)

db = pd.DataFrame(data = dados, index = lista_cpfs, columns=['Nome', 'idade', 'E-mail'])

print(db)