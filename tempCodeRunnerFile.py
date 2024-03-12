primeiro_valor = 0
segundo_valor = 1
proximo_valor = 0
fibonacci = 0
encontrar = int(input("Digite o número que você deseja encontar: "))
while fibonacci != encontrar: 
    proximo_valor += (primeiro_valor + segundo_valor)
    fibonacci = primeiro_valor + segundo_valor
    if fibonacci > encontrar:
        print("O número {} não pertence à sequência fibonacci".format(encontrar))
        break
    elif fibonacci == encontrar:
        print("O numéro {} foi encontrado!".format(encontrar))