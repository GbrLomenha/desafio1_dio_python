
menu = '''
[Q] - Saque
[D] - Depósito
[S] - Saldo
[X] - Extrato
[E] - Sair
'''
LIMITE = 3
LIMITE_SAQUE = 500
sacado = 0
saques = 0
saldo = 150
extrato = "=============EXTRATO============\n"

while True:
    opcao = input(menu)
    opcao = opcao.lower()

    if opcao == 'q':
        saque = float(input("Digite o valor do saque: "))

        excedeu_saques = saques > LIMITE
        excedeu_valor = saque+sacado > LIMITE_SAQUE
        excedeu_saldo = saque > saldo

        if excedeu_saques or excedeu_valor:
            print("Operação inválida. Não é possível sacar mais de R$500.00 e 3 saques por dia.")
        
        elif excedeu_saldo:
            print("Operação inválida. O valor do saque excedeu o saldo disponível.")
        
        elif saque <= 0:
            print("Operação inválida. Escolha um valor positivo e não nulo.")

        else:
            saques +=1
            sacado += saque
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            print("Saque realizado!")
            
    

    if opcao == 'd':
        deposito = float(input('Digite o valor do depósito: '))
        if deposito <= 0:
            print("Não é possível depositar valores nulos ou menores que zero.")
        else:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("Deposito realizado!")
    

    if opcao == 'x':
        if extrato == "=============EXTRATO============\n":
            print("\n\
=============EXTRATO============\n\
 Nenhuma operação foi realizada\n")

        else:   
            print(extrato)
        print("================================")
    if opcao == 's':
        print(f"Seu saldo é de R${saldo:.2f}.")

    if opcao == 'e':
        break