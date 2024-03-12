
primeiro_valor = 0
segundo_valor = 1
proximo_valor = 0
fibonacci = 0

encontrar = int(input("Digite o número que você deseja encontrar na sequência Fibonacci: "))

while fibonacci <= encontrar: 
    if fibonacci == encontrar:
        print("O número {} foi encontrado na sequência Fibonacci!".format(encontrar))
        break
     
    proximo_valor = primeiro_valor + segundo_valor
    primeiro_valor = segundo_valor
    segundo_valor = proximo_valor
    fibonacci = proximo_valor

if fibonacci > encontrar:
    print("O número {} não pertence à sequência Fibonacci.".format(encontrar))