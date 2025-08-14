# Eu aprendi algumas coisas, não cheguei a colocar tudo em outros arquivos sequer em commits, mas utilizarei do que eu conseguir.
# Tentarei utilizar de várias estruturas.

while True:
    print("#"*30)
    print(" ")
    print(" APROVACAO DE ESTUDANTE ")
    print(" ")
    print("#"*30)
    P1 = float(input("Insira a primeira nota: "))
    P2 = float(input("Agora, insira a segunda nota: "))
    MED = (P1 + P2)/2
    print(" ")
    if MED >= 7:
        print(f"Sua nota e de: {MED}.")
        print("*"*30)
        print("VOCE FOI APROVADO POR MEDIA")
        print("*"*30)
        print(" ")
        continuar = input("Deseja continuar o programa? (Y/N)")
        if continuar == "Y" or continuar == "y":
            pass
        elif continuar == "N" or continuar == "n":
            break
        else:
            print("Resposta invalida, reiniciando programa")
            pass
    else:
        print(f"Sua nota e de: {MED:.1f}.")
        print("*"*30)
        print("VOCE FOI REPROVADO POR MEDIA")
        print("*"*30)
        print(" ")
        continuar = input("Deseja continuar o programa? (Y/N)")
        if continuar == "Y" or continuar == "y":
            pass
        elif continuar == "N" or continuar == "n":
            break
        else:
            print("Resposta invalida, reiniciando programa")
            pass