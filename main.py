

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
        c = 2
        q = quantidade

        while c < quantidade:
            r = 2
            r = (r * base) * int(numero[(quantidade - c) - 1])
            c = c + 1

            resultado = resultado + r
    contador = contador + 1
    expoente += 1
print(resultado)


