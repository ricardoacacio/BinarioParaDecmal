

# Projeto 1 - Criar um programa que calcule o número decimal com base a inserção binária

quantidade = 0
expoente = 0
base = 2
contador = 0
resultado = 0

print("Digite 8 algarismos em binário")
numero = input()
quantidade = len(numero)


while contador <= quantidade:
    if expoente == 0:
         resultado = (1 * int(numero[quantidade - 1]))
    elif expoente == 1:
         resultado = resultado + (base * int(numero[quantidade - 2]))
    else:
       c = 0
       r = 1
       while c < expoente:
           r = r * base
           c = c + 1
       res = r * int(numero[(quantidade - expoente)-1])
       resultado = resultado + res
    contador = contador + 1
    expoente = expoente + 1
print(resultado)


