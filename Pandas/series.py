import pandas as pd

# CRIANDO SERIES A PARTIR DE LISTA

lista_nome = "Luiz Henrique Nascimento Dantas".split()
print(pd.Series(lista_nome))

# CRIANDO SERIES A PARTIR DE DICIONÁRIOS

dados = {'nome1' :  'Luiz', 'nome2' : 'Henrique', 'nome3': 'Nascimento',
         'nome4' : 'Dantas'
         }

print(pd.Series(dados))

# PASSANDO O ROTULO QUE DESEJO USAR COMO INDICE

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44'.split()

print(pd.Series(lista_nome, index = cpfs))

'''Rotular as Series (e como veremos os DataFrames), é interessante para facilitar a localização e manipulação dos dados. 
Por exemplo, se quiséssemos saber o nome da pessoa com cpf 111.111.111-11, poderíamos localizar facilmente essa informação 
com o atributo loc, usando a seguinte sintaxe: series.loc[rotulo], onde rótulo é índice a ser localizado.'''

#   LOCALIZANDO COM LOC

dados2 = pd.Series(lista_nome, index=cpfs)

print(dados2.loc['222.222.222-22']) # retorna o valor

# EXTRAINDO INFORMAÇÕES DE UMA SERIES

series_dados = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas
print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series
