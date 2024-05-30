import random

# Função para embaralhar os números
def shuffle_numbers():
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers

# Função para criar um teclado numérico com os números embaralhados
def create_numeric_keyboard(numbers):
    keyboard = []
    for i in range(0, 10, 2):
        keyboard.append([numbers[i], numbers[i+1]])
    return keyboard

# Função para imprimir o teclado numérico formatado
def print_numeric_keyboard(keyboard):
    for row in keyboard:
        print(f"| {row[0]} ou {row[1]} |", end=" ")
    print()

# Gerar e imprimir três exemplos
for i in range(3):
    numbers = shuffle_numbers()
    keyboard = create_numeric_keyboard(numbers)
    print(f"Exemplo {i+1}:")
    print_numeric_keyboard(keyboard)