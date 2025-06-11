#nome = "Henrique"
#sobrenome = "França"
#nomecompleto = nome +" "+sobrenome
#print(nomecompleto)

#Dicionário (Funciona parecido com o struct em C, mas o valor é colocado direto)
# Chave : Valor
#funcionario = {
#   "Matricula" : 123,
#    "Nome" : "Hilson",
#    "Cargo" : "Docente",
#    "Departamento" : "Eng. de Software",
#    "Instituicao" : "ICEV",
#}
#
#print(funcionario["Nome"])

matricula = int(input("Digite a matrícula: "))
nome = input("Digite o nome: ")
cargo = input("Informe o seu cargo: ")
salario = float(input("Digite o seu salário: "))
salarionovo = salario * 1.1
reajuste = salarionovo - salario
print("="*30)
print("        DADOS DO CONTRACHEQUE       ")
print("-"*30)
print("Matricula......:", matricula)
print("Funcionario....:",nome)
print("Cargo..........:",cargo)
print("Salario antes..:",round(salario,2))
print("Salario depois.:",round(salarionovo,2))
print("Valor Reajustado:",round(reajuste,2))
print("-"*30)
print("     PAG.     ")
print("="*30)