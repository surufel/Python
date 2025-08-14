
def Entrada():
    global num1, num2 # global permite que eu uso a variável em um escopo global (ou seja, em qualquer lugar)
    num1 = int(input("Digite o primeiro valor...:" )) # naturalmente, vai ficar no escopo da função, ou seja, só acessível dentro da função
    num2 = int(input("Digite o segundo valor....:" ))

def Somar():
        global res
        res = num1 + num2

def Subtrair():
        global res
        res = num1 - num2

def Multiplicar():
        global res
        res = num1 * num2

def Dividir():
        global res
        if num1>0 or num2>0:
            res = num1 / num2
        else:
            print("Informe um valor maior que zero")

def Saida():
      print("O resultado da operação é: ", round(res,2))

def MenuCalculadora():
    while True:
        print(" ")
        print("#"*60)
        print(" ")
        print("CALCULADORA SIMPLES     ")
        print(" ")
        print("1 - SOMAR; 2 - SUBTRAIR; 3 - MULTIPLICAR; 4 - DIVIDIR")
        print(" ")
        print("#"*60)
        global opMenu
        opMenu = input("Digite uma opção ou zero para sair: ")
        if opMenu == "0":
          print("Finalizando o calculo")
          break
        elif opMenu =="1":
            Entrada()
            Somar()
            Saida()
        elif opMenu == "2":
             Entrada()
             Subtrair()
             Saida()
        elif opMenu == "3":
             Entrada()
             Multiplicar()
             Saida()
        elif opMenu == "4":
             Entrada()
             Dividir()
             Saida()

if __name__ == "__main__":
     MenuCalculadora()