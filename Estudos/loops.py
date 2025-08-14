for x in range(1, 11): # Equivalente ao for (int x = 1; x >= 11; x++)
    print(x, end=" ") # Vai começar do 1 e ir até 11 (ou seja, 10 números no total serão contados, o output vai sair de 1 a 10)

for y in range(1,6):
    if y == 3:
        continue # isso vai pular o y quando ele for = 3, contando de 1 a 5 (no else) depois de pular o 3 (no if). break quebra o loop.
    else:
        print(y)



# NESTED LOOP DE FOR (quero fazer matrizes)
linhas = int(input("Quantas linhas voce quer sua matrix?: "))
colunas = int(input("Quantas colunas voce quer sua matriz?: "))
for i in range (linhas):
    for j in range (colunas):
        print(1, end="| ")
    print("")
