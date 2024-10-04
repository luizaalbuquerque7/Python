def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

while True:
    print("\nMenu de Conversão de Temperaturas:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    print("7. Sair")

    opcao = input("Escolha uma opção (1-7): ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius} graus Celsius são equivalentes a {celsius_para_fahrenheit(celsius)} graus Fahrenheit.")
    
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit} graus Fahrenheit são equivalentes a {fahrenheit_para_celsius(fahrenheit)} graus Celsius.")
    
    elif opcao == '3':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius} graus Celsius são equivalentes a {celsius_para_kelvin(celsius)} Kelvin.")
    
    elif opcao == '4':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin} Kelvin são equivalentes a {kelvin_para_celsius(kelvin)} graus Celsius.")
    
    elif opcao == '5':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit} graus Fahrenheit são equivalentes a {fahrenheit_para_kelvin(fahrenheit)} Kelvin.")
    
    elif opcao == '6':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin} Kelvin são equivalentes a {kelvin_para_fahrenheit(kelvin)} graus Fahrenheit.")
    
    elif opcao == '7':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
+
