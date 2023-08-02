menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[a] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu).lower()

    if opcao == "d": 
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é invalido!")

    elif opcao == "s": 
        valor = float (input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu o limite de saques diario.")

        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print (f"""
----------------EXTRATO----------------
---------------------------------------
{extrato}

Seu saldo é R$ {saldo:.2f}
---------------------------------------
""")

    elif opcao == "q":
        break

    else:
        print ("Operação inválida, por favor selecione novemante a operação desejada.")