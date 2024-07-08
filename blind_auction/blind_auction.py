from art import logo

# Función para pedir las ofertas de los participantes
def ask_bidders():
    global name_key, bid_value
    # Solicita el nombre del participante
    name_key = input("What is your name?--> ")
    # Solicita la oferta del participante
    bid_value = input("What is your bid?--> ")
    # Almacena la oferta en el diccionario 'dict' con el nombre como clave
    dict[name_key] = int(bid_value)

# Imprime el logo de la subasta
print(logo)

# Inicializa un diccionario vacío para almacenar las ofertas
dict = {}

# Mensaje de bienvenida
print("Welcome to the secret auction program")

# Llama a la función para pedir las ofertas
ask_bidders()

# Bucle para gestionar múltiples participantes
while True:
    # Imprime el diccionario actual de ofertas
    print(dict)
    # Pregunta si hay más participantes
    more_bidders = input("Are there any other bidders? - Type --> yes/no\n").upper()
    if more_bidders == "YES":
        # Si hay más participantes, vuelve a pedir las ofertas
        ask_bidders()
        continue
    elif more_bidders == "NO":
        # Si no hay más participantes, encuentra la oferta máxima y el ganador
        dict_values = list(dict.values())
        maximo = max(dict_values)
        dict_keys = list(dict.keys())
        # Imprime el ganador y la oferta máxima
        print(f"The winner is {dict_keys[dict_values.index(maximo)]} with a bid of {maximo}")
    else:
        # Si la entrada no es válida, solicita intentarlo de nuevo
        print("try again, please!")
        continue
    # Rompe el bucle después de encontrar el ganador
    break
