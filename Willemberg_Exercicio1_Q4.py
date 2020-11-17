rep= []
palavrasecreta = str(input("Digite a palavra chave:"))
print("Você so pode errar 6 vezes")
letracert = []
for i in palavrasecreta:
    letracert.append('_')
enforcar = False
acerta = False
erros = 0
print(letracert)
while(not enforcar and not acerta):
    tent = input("Qual letra:")
    if tent in rep:
        print("Letra já informada, digite outra letra:")
    else:
        rep += tent
    if(tent in palavrasecreta):
        pos = 0
        for let in palavrasecreta:
            if(tent.upper() == let.upper()):
                letracert[pos] = let
            pos = pos + 1
    else:
        erros += 1
    enforcar = erros == 6  
    acerta = '_' not in letracert
    print(letracert)
if(acerta):
    print("Você ganhou")
else:
    print("Você Perdeu")