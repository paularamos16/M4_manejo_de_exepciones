print('Juego de adivinar un número')
print('---------------------------\n')

num_secreto = 3

try:
    eleccion = int(input('Dime tu número: '))
    if eleccion == num_secreto:
        print('Has adivinado mago!')
    else: 
        print('Fallaste')
except ValueError: # Captura el error 
    print('Yapo, ingresa un número, no otra cosa!!!')

print('fin')


