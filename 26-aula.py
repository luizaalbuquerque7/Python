# solicita os 5 numeross aos usuarios
numeros = []

for i in range(5):
    num = int(input(f"digite o{i+1} numero:"))
    numeros.append(num)   

#calcula o maior, o menor e a soma    
maior_num = max(numeros)
menor_num = min (numeros)
soma_num = sum (numeros)

# exibe os resultados 

print(f"o maior numero:{maior_num}")
print(f"o menor numero:{menor_num}")
print(f"a soma total:{soma_num}")
