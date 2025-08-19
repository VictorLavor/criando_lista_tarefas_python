lista = []
contador = 0

while contador <= 5:
    item = input(f'Escreva sua lista de tarefas {contador+1}: ')
    lista.append(item)
    contador += 1

print('\n')

print(f'Sua lista de tarefas:{lista}')