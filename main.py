

# Projeto 1 - Criar um programa que calcule o número decimal com base a inserção binária

exp = 0
base = 2
cont = 0
aux = 0
basex = 0

print("Digite 8 algarismos em binário")
num = input()
qtd = len(num)
num = num[::-1]
print(num)

while cont <= qtd:
    if exp == 0:
        aux = aux + (1 * cont)
        cont = cont + 1
        exp = exp + 1
    elif exp == 1:
            aux = aux + (base * cont)
            cont = cont + 1
            exp = exp + 1
    else:
        aux = aux * base * int(num[cont])
        cont = cont + 1
        exp = exp + 1


print("aux = ", aux)
print("cont = ", cont)
print("exp = ", cont)










