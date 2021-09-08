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
