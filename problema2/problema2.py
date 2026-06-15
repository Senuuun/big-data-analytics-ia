print("Bem vindo a calculadora da sua conta de energia:")

tipo = input("Digite o tipo de Instalação (R-Residencial, C-Comercial, I-Industrial): ")
consumo = float(input("Digite a quantidade de energia consumida no mês: "))

tipo = tipo.lower()

preco = 0
imposto = 0

if tipo == 'r': 
    if consumo <= 500:
        preco = 0.40
        imposto = 0.10
    else:
        preco = 0.65
        imposto = 0.12

elif tipo == 'c': 
    if consumo <= 1000:
        preco = 0.55
        imposto = 0.15
    else:
        preco = 0.60
        imposto = 0.16

elif tipo == 'i': 
    if consumo <= 5000:
        preco = 0.55
        imposto = 0.20
    else:
        preco = 0.60
        imposto = 0.22

else:
    print("Tipo de instalação inválido!")
    exit()

valor_sem_imposto = consumo * preco
valor_imposto = valor_sem_imposto * imposto
total = valor_sem_imposto + valor_imposto

print("\nPortanto, para o seu caso:")
print(f"A tarifa por kWh (sem impostos) é de R$ {preco} reais,")
print(f"O imposto é de {imposto * 100}%,")
print(f"e sua conta de energia (com impostos) será de R$ {total} reais.")
