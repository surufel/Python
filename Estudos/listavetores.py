numeros = [1,2,3,4,5,6,7]
print(numeros[0])

vetor = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(vetor[0][0])

for i in range(len(vetor)):
    for j in range(len(vetor)):
        print(vetor[i][j], end="") # Isso vai listar todos os indices, do vetor

print(" ")
print("*"*30)
print(" ")

for x in range(0, 3):
    for y in range(0, 3):
        print(vetor[x][y], end=" |")
    print("")
