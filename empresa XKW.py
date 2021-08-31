nome_func = (input("Digite o nome do funcionário:"))
salario = int(input("Digite o salário do funcionário:"))
tempo_trab = int(input("Digite o tempo de trabalho:"))
bonus_20 = salario * 0.20
bonus_10 = salario * 0.10
if (tempo_trab >=5):
  print("O funcionário vai receber o bônus de 20%:", bonus_20)
else:
  print("O funcionário vai receber o print de 10%:",bonus_10)