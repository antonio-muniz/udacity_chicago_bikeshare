# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# É importante definir "constantes" para valores fixos que precisam ser frequentemente utilizados.
# (Optei por não utilizá-las nos pontos em que são executados os asserts para não fazer nenhuma alteração.)
START_TIME_INDEX = 0
END_TIME_INDEX = 1
TRIP_DURATION_INDEX = 2
START_STATION_INDEX = 3
END_STATION_INDEX = 4
USER_TYPE_INDEX = 5
GENDER_INDEX = 6
BIRTH_YEAR_INDEX = 7

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for sample in data_list[1:21]:
    print(sample)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
[print(sample[GENDER_INDEX]) for sample in data_list[0:20]]


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3


def column_to_list(data_list: list, index: int) -> list:
    """
    Constrói uma lista contendo os valores de todos os exemplos em um determinado índice.
    Argumentos:
        data_list: O conjunto de dados com todos os exemplos.
        index: O índice com o valor a ser selecionado em cada exemplo.
    Retorna:
        Uma lista com o mesmo comprimento do conjunto de dados contendo os valores selecionados.

    """
    return [sample[index] for sample in data_list]


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, GENDER_INDEX)[:20])

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
male = 0
female = 0
for genre in column_to_list(data_list, GENDER_INDEX):
    if genre == 'Male':
        male += 1
    elif genre == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5


def count_gender(data_list: list) -> list:
    """
    Calcula as quantidades de exemplos no conjunto de dados em que 'Gender' tem valor 'Male' ou 'Female'.
    Argumentos:
        data_list: O conjunto de dados com todos os exemplos.
    Retorna:
        Uma lista com duas posições.
        Na primeira posição, o número de exemplos com 'Gender' igual a 'Male'.
        Na segunda posição, o número de exemplos com 'Gender' igual a 'Female'.
    """
    male = 0
    female = 0
    for genre in column_to_list(data_list, GENDER_INDEX):
        if genre == 'Male':
            male += 1
        elif genre == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
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


def most_popular_gender(data_list: list) -> str:
    """
    Identifica o gênero mais frequente no conjunto de dados e retorna o nome do gênero em português.
    Argumentos:
        data_list: O conjunto de dados com todos os exemplos.
    Retorna:
        'Feminino' caso 'Female' seja o gênero mais frequente, ou 'Masculino' caso 'Male' seja o gênero mais frequente.
    """
    male_count, female_count = count_gender(data_list)
    if male_count == female_count:
        answer = 'Igual'
    elif male_count > female_count:
        answer = 'Masculino'
    else:
        answer = 'Feminino'
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


def display_bar_graph(title: str, x_label: str, y_label: str, bar_names: list, bar_values: list):
    """
    Função genérica que exibe um gráfico de barras com as informações passadas.
    Criada para evitar a repetição das funções do matplotlib e simplificar seu uso.
    Argumentos:
        title: O título do gráfico.
        x_label: Identificador do eixo horizontal.
        y_label: Identificador do eixo vertical.
        bar_names: Identificadores de cada barra.
        bar_values: Valores de cada barra.
    """
    bar_indexes = list(range(len(bar_names)))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(bar_indexes, bar_names)
    plt.bar(bar_indexes, bar_values)
    plt.show(block=True)


display_bar_graph(
    title='Quantidade por Gênero',
    x_label='Gênero',
    y_label='Quantidade',
    bar_names=["Male", "Female"],
    bar_values=count_gender(data_list)
)

input("Aperte Enter para continuar...")
# TAREFA 7
print("\nTAREFA 7: Verifique o gráfico!")


def count_user_types(data_list):
    """
    Conta as quantidades de exemplos no conjunto de dados em que 'User Type' tem valor 'Customer' ou 'Subscriber'.
    Argumentos:
        data_list: O conjunto de dados com todos os exemplos.
    Retorna:
        Uma lista com duas posições.
        Na primeira posição, o número de exemplos com 'User Type' igual a 'Customer'.
        Na segunda posição, o número de exemplos com 'User Type' igual a 'Subscriber'.
    """
    customers = 0
    subscribers = 0
    for user_type in column_to_list(data_list, USER_TYPE_INDEX):
        if user_type == 'Customer':
            customers += 1
        elif user_type == 'Subscriber':
            subscribers += 1
    return [customers, subscribers]


display_bar_graph(
    title='Quantidade por tipo de usuário',
    x_label='Tipo de usuário',
    y_label='Quantidade',
    bar_names=['Customer', 'Subscriber'],
    bar_values=count_user_types(data_list)
)

input("Aperte Enter para continuar...")
# TAREFA 8
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem exemplos sem valor na coluna 'Gender' e também em outras colunas. A função 'count_gender' simplesmente contabiliza os exemplos que tenham 'Male' ou 'Female' como valor, desconsiderando qualquer outro valor como, no caso, a string vazia."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9

trip_duration_list = [int(duration)
                      for duration in column_to_list(data_list, TRIP_DURATION_INDEX)]

min_trip = trip_duration_list[0]
max_trip = 0.

trip_duration_sum = 0
for trip_duration in trip_duration_list:
    if trip_duration < min_trip:
        min_trip = trip_duration
    if trip_duration > max_trip:
        max_trip = trip_duration
    trip_duration_sum += trip_duration

mean_trip = trip_duration_sum / len(trip_duration_list)

# É necessário ordenar a lista para obter a mediana.
trip_duration_list.sort()
median_trip_index = int(len(trip_duration_list) / 2)
median_trip = trip_duration_list[median_trip_index]

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
user_types = set()

start_station_list = column_to_list(data_list, START_STATION_INDEX)
for start_station in start_station_list:
    user_types.add(start_station)

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
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

# TAREFA 12 - Desafio! (Opcional)
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list) -> list:
    """
    Identifica os valores únicos da coluna fornecida e conta as ocorrências de cada valor.
    Argumentos:
        column_list: A coluna cujos valores devem ser contados.
    Retorna:
        Uma lista com duas posições.
        Na primeira posição, uma lista contendo os valores únicos encontrados na coluna.
        Na segunda posição, uma lista contendo o número de ocorrências do respectivo valor.
    """
    count_dictionary = {}
    for item in column_list:
        # Inicializa o contador como zero antes de contabilizar a primeira ocorrência
        current_count = count_dictionary.setdefault(item, 0)

        count_dictionary[item] = current_count + 1

    # Chaves de dicionário são únicas, como em um set
    item_types = list(count_dictionary.keys())
    count_items = [count_dictionary[item_type]
                   for item_type in item_types]

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------

input("Aperte Enter para continuar...")

print("\nExtra: Encontrando uma quantidade arbitrária de valores mais frequentes usando funções genéricas\n")


def most_frequent_items(column_list: list, amount: int) -> list:
    """
    Obtem um determinado número de valores mais frequentes dentro de uma dada coluna.
    Argumentos:
        column_list: A coluna cujos valores serão avaliados.
        amount: O número de valores a retornar. Por exemplo, se amount = 3, a função retornará os 3 valores mais frequentes.
    Retorna:
        Uma lista de comprimento igual a 'amount'.
        Cada elemento da lista é uma tupla contendo o valor e o respectivo número de ocorrências.
        A lista é retornada em ordem decrescente pelo número de ocorrências.
    """

    types, counts = count_items(column_list)
    occurrences = list(zip(types, counts))

    # Ordenando decrescentemente pelo número de ocorrências
    occurrences.sort(key=lambda occurrence: occurrence[1], reverse=True)

    return occurrences[0:amount]


start_stations = column_to_list(data_list, START_STATION_INDEX)
most_frequent_start_stations = most_frequent_items(start_stations, 5)
print("\nAs cinco start stations mais frequentes:\n")
for index, (name, trip_count) in enumerate(most_frequent_start_stations):
    print('#{0}: {1}, com {2} viagens.'.format(index+1, name, trip_count))

end_stations = column_to_list(data_list, END_STATION_INDEX)
most_frequent_end_stations = most_frequent_items(end_stations, 5)
print("\nAs cinco end stations mais frequentes:\n")
for index, (name, trip_count) in enumerate(most_frequent_end_stations):
    print('#{0}: {1}, com {2} viagens.'.format(index+1, name, trip_count))

input("Aperte Enter para continuar...")
