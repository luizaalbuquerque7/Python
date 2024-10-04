# variáveis
opcao = 0

# inicio do codigo
while opcao != 6:
    print ("MENU DE OPERAÇÕES BÁSICAS")
    print ("1. Soma")
    print ("2. Subtração")
    print ("3. Multiplicação")
    print ("4. Divisão")
    print ("5. Resto de Divisão")
    print ("6. Sair...")
    opcao = input ("Digite a opção escolhida:")

    if opcao == 1:
        print("Você escolheu a Opção 1, Operação de Soma")
        num1 = int (input("Digite o primeiro valor:"))
        num2 = int (input("Digite o segundo valor:"))
        resultado = num1 + num2 
        print (f"A Soma dos Valores: {resultado}")
    
    elif opcao == 2:
        print("Você escolheu a Opção 2, Operação de Subtração")
        num1 = int (input("Digite o primeiro valor:"))
        num2 = int (input("Digite o segundo valor:"))
        resultado = num1 - num2 
        print (f"A Subtração dos Valores: {resultado}")
    
    elif opcao == 3:
        print("Você escolheu a Opção 3, Operação de Multiplicação")
        num1 = int (input("Digite o primeiro valor:"))
        num2 = int (input("Digite o segundo valor:"))
        resultado = num1 * num2 
        print (f"A Multiplicação dos Valores: {resultado}")

    elif opcao == 4:
        print("Você escolheu a Opção 4, Operação de Divisão")
        num1 = int (input("Digite o primeiro valor:"))
        num2 = int (input("Digite o segundo valor:"))
        resultado = num1 / num2 
        print (f"A Divisão dos Valores: {resultado}")

    elif opcao == 5:
        print ("Você escolheu a Opção 5, Resto de Divisão")
        num1 = int (input("Digite o primeiro valor:"))
        num2 = int (input("Digite o segundo valor:"))
        resultado = num1 % num2 
        print (f"O resto da Divisão dos Valores: {resultado}")
    
    elif opcao == 6:
        print ("Saindo...")

    else:
        print ("Opção Invalida")
