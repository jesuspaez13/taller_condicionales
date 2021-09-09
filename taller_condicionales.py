# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:03:17 2021

@author: USER
"""
# Problema 1
numero_camisas = int(input('Digite la cantidad de camisas: '))
if(numero_camisas >= 3):
    precio_camisas = int(input('Digite el precio de las camisas: '))
    valor_sin_descuento = numero_camisas * precio_camisas
    print(f'El precio total sin descuento es: {valor_sin_descuento}')
    descuento = valor_sin_descuento * 0.3
    total = valor_sin_descuento - descuento
    print(f'El valor total serían: {total}')
elif(numero_camisas < 3 and numero_camisas > 0):
    precio_camisas = int(input('Digite el precio de las camisas: '))
    valor_sin_descuento = numero_camisas * precio_camisas
    print(f'El precio total sin descuento es: {valor_sin_descuento}')
    descuento = valor_sin_descuento * 0.1
    total = valor_sin_descuento - descuento
    print(f'El valor total serían: {total}')
else:
    print('El numero de camisas es equivocado')

# Problema 2
numero_al_azar = int(input('Digite el numero que le salío: '))
if(numero_al_azar < 74 and numero_al_azar >= 0):
    valor_compra = int(input('Digite el precio de su compra: '))
    descuento = valor_compra * 0.15
    total = valor_compra - descuento
    print(f'El valor total de su compra es: {total}')
elif(numero_al_azar >= 74):
    valor_compra = int(input('Digite el precio de su compra: '))
    descuento = valor_compra * 0.2
    total = valor_compra - descuento
    print(f'El valor total serían: {total}')
else:
    print('Ese numero es equivocado')

# Problema 3
monto = int(input('Digite el monto de la fianza: '))
if(monto < 50000 and monto > 0):
    porcentaje = monto * 0.03
    cuota = monto + porcentaje
    print(f'La cuota a pagar va ser de: {cuota}')
elif(monto >= 50000):
    porcentaje = monto * 0.02
    cuota = monto + porcentaje
    print(f'La cuota a pagar va ser de: {cuota}')
else:
    print('El monto ingresado es equivocado')

# Problema 4
puntos = int(input('Digite la cantidad de puntos acumulados: '))
ganancias = int(input('Digite la cantidad de ganancias obtenidas: '))
if(puntos > 170):
    multa = ganancias * 0.5
    perdida = ganancias - multa
    print(f'La perdida es de ${perdida}')
else:
    print('No tiene sancion, por tanto no tiene perdidas')
