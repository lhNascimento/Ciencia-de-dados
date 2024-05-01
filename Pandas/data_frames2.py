import pandas as pd
lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

dados = list(zip(lista_nomes, lista_idades, lista_emails))
df_dados = pd.DataFrame(data=dados, index=lista_cpfs, columns=['Nome', 'idades', 'E-mail'])


# SELEÇÃO DE COLUNAS EM UM DATAFRAME
'''
 Podemos realizar operações em colunas específicas de um DataFrame ou ainda criar um novo objeto contendo somente as colunas que serão usadas em uma determinada análise. 
 Para selecionar uma coluna, as duas possíveis sintaxes são:

nome_df.nome_coluna # não aceita colunas com espaços entre as palavras.
nome_df[nome_coluna]

!!! Se precisarmos selecionar mais do que uma coluna, então precisamos passar uma lista, da seguinte forma: nome_df[['col1', 'col2', 'col3']] !!!
-> Ao selecionar uma coluna, obtemos uma Series

'''
# CRIANDO UMA SERIES APENAS COM IDADES E CALCULANDO A MEDIA DELA
df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))
print('\nMédia de idades = ', df_uma_coluna.mean())

# CRIANDO UM NOVO DB COM NOMES E IDADES

colunas = ['Nome', 'idades']

df_duas_colunas = df_dados[colunas]
print(type(df_duas_colunas))

print('\n',  df_duas_colunas)