import csv
import matplotlib.pyplot as plt
import datetime
import time


# Vamos ler os dados como uma lista
print("Lendo o documento...")


def create_data_list(filename):
    # Função abre o arquivo e retorna uma lista de dados do arquivo 'chicago.csv'
    data_list = []
    with open(filename) as file_read:
        for line in file_read:
            file_lines = line.split(',')
            data_list.append(file_lines)
    return data_list


data_list = create_data_list('/Users/Alexandre/Documents/chicago.csv')

print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados.
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")


def data_list20(data_list=[]):
    # Função recebe uma lista, e mostra apenas os 20 primeiros dados.
    lista20 = []
    for i in data_list[:20]:
        lista20.append(i)
    return lista20


def print_list():
    # Função para imprimir os dados enumeradosm, Solicitados.
    for c, lista in enumerate(data_list20(data_list), 1):
        print('\n\n{}º  --- Dado Solicitado ---\n {}'.format(c, list(lista)))


print_list()
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")


# Função que percorre pela coluna 'genero' e adiciona os dados em uma lista
def data_genero(data_list):
    genero = []
    for gen in [j[-2] for j in data_list]:
        genero.append(gen)
    return genero


def print_genero():
    # Função que imprime e enumera os generos
    for i, line in enumerate(data_list[:20], start=1):
        print(f"Linha : {i}\tGênero: {line[-2]}")


print_genero()
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem


def column_to_list(data, index):
    # Funcao que guarda os dados de uma coluna 'x', e retorna em uma lista
    column_list = []
    for i in [j[index] for j in data]:
        column_list.append(i)
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])


# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)
            ) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)
           ) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(
    data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.


male = 0
female = 0
# Laço for que faz as contagens de homens e mulheres
for gen in column_to_list(data_list, -2):
    if gen.lower() == 'male':
        male += 1
    elif gen.lower() == 'female':
        female += 1


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("\n\nAperte Enter para continuar...\n")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    # Função que retorna a contagem de gênero, male e famamle.
    male_count = 0
    female_count = 0
    for gen in column_to_list(data_list, -2):
        if gen.lower() == 'male':
            male_count += 1
        elif gen.lower() == 'female':
            female_count += 1
    return [male_count, female_count]


print("TAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)
            ) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)
           ) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.


def most_popular_gender(data_list):
    # Função que recebe um gênero, e retorna uma 'string' com o gênero mais popular.
    male, female = count_gender(data_list)
    if male > female:
        answer = 'Masculino'
    elif female > male:
        answer = 'Feminino'
    else:
        answer = 'Igual'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)
            ) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(
    data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


def count_types(data_list):
    # Função que conta os tipos da coluna 'types' para montar o gráfico Tarefa 7
    type_list1 = []
    type_list2 = []
    for types in column_to_list(data_list, -3):
        if types.lower() == 'subscriber':
            type_list1.append(types)
        elif types == 'Customer':
            type_list2.append(types)
    return [len(type_list1), len(type_list2)]


# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

# Gráfico
user_types = column_to_list(data_list, -3)
types = ['Subscriber', 'Customer']
quantity = count_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Types')
plt.xticks(y_pos, types)
plt.title('Quantidade por Types')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = ("Não é verdadeira, pois o a soma desses dois elementos de uma coluna não representam o tamanho total data_list, obs: existem espaços 'em branco' .")
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().

# Variável que recebe uma função, e retorna uma lista de coluna.
trip_duration_list = column_to_list(data_list, 2)

min_trip = int(sorted(trip_duration_list)[0])
max_trip = int(sorted(trip_duration_list)[-1])
mean_trip = 0.
median_trip = 0.

size = len(trip_duration_list)
total_time = 0



for i in range(0, size):
    # Laço for que encontra o maior e o menor valor da coluna 'trip_duration'.
    time = int(trip_duration_list[i])
    total_time += int(time)
    if time >= max_trip:
        max_trip = time
    if time <= min_trip:
        min_trip = time

# Lista ordenada criada por um dicionario com chave int.
ord_list = sorted(trip_duration_list, key=int)
size = len(trip_duration_list)
i = int((size) // 2)

if (size % 2 == 0):
    # Condicional que calcula a mediana da coluna 'trip_duration'.
    median_trip = eval((ord_list[i] + ord_list[i + 1]) / 2.0)
else:
    median_trip = int(ord_list[i])

# calculo da média da coluna 'trip_duration'
mean_trip = int(round(total_time/size))

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip,
      "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = column_to_list(data_list, 3)
user_types = set(user_types)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#   """
#   Função de exemplo com anotações.
#   Argumentos:
#       param1: O primeiro parâmetro.
#       param2: O segundo parâmetro.
#   Retorna:
#       Uma lista de valores x.

#   """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
# Função retorna os tipos e quantidade de cada um deles,
# Declaro um dicionário item_types e crio as listas apartir da
# Chave 'keys()' e dos valores 'values()'.
    item_types = {}
    for i in column_list:
        if str(i) in item_types.keys():
            item_types[str(i)] += 1
        else:
            item_types[str(i)] = 1
    
    types = list(item_types.keys())
    count_items = list(item_types.values())

    return [types, count_items]


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
