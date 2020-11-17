nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))
frequencia = int(input("Digite o percentua de freqüência:")) 

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and frequencia >= 75 :
    print("Aluno Aprovado")
    print("Média:", media)
    print("Freqüência:", frequencia,"%")

if media < 7 or frequencia < 75:
    print("Aluno Reprovado")
    print("Média:", media)
    print("Freqüência:", frequencia,"%")
