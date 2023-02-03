

# Projeto 1 - Criar um programa que calcule o número decimal com base a inserção binária
print('CONVERSOR BINÁRIO PARA DECIMAL')
print('********************************')
print('Digite 8 algarismos sendo 0 e 1')

numero = input()
c = 0
a = 0
base = 2

while c < 8:
    if c == 0 and int(numero[7]) == 0:
        a += 0
        c += 1
    elif c == 0 and int(numero[7]) == 1:
        a += 1
        c += 1

    if c == 1 and int(numero[6]) == 0:
        a += 0
        c += 1
    elif c == 1 and int(numero[6]) == 1:
        a += 2
        c += 1

    co = 0
    t = 1

    while co < c:
        t *= base
        co += 1
    t = t * int(numero[8 - (c + 1)])
    a += t

    c += 1

print('O resultado é: ', a)



















# quantidade = 0
# contador = 0
# expoente = 0
# base = 2
# resultado = 0
#
# print("Digite 8 algarismos em binário")
# numero = input()
# quantidade = len(numero)
#
# while contador <= quantidade:
#     if expoente == 0:
#          resultado = (1 * int(numero[quantidade - 1]))
#     elif expoente == 1:
#          resultado = resultado + (base * int(numero[quantidade - 2]))
#     else:
#        c = 0
#        r = 1
#        while c < expoente:
#            r = r * base
#            c = c + 1
#        res = r * int(numero[(quantidade - expoente)-1])
#        resultado = resultado + res
#     contador = contador + 1
#     expoente = expoente + 1
# print(resultado)


