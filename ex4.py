valor = int(input("Qual valor da compra: R$"))
vip = input("Você é cliente Vip? (S/n): ")

if valor > 100 or vip == "S":
    print("Parabéns! Você ganhou FRETE GRÁTIS!")
else:
    Print("O frete ficará em R$28,00")