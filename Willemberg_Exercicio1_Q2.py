valor = float(input("Digite o valor da prestação:"))
taxa = float(input("Digite o valor da taxa:"))
tempo = float(input("Digite a quantidade de dias atrasados:"))

prestação = valor + (valor* ( taxa / 100) * tempo)

print("O valor da prestação em atraso é :", prestação,"$")