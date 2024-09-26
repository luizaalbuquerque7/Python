a = float(input("Digite o valor de A"))

while a <= 0:
    print("Valor não aceito, tente novamente.")
    a = float(input("Digite o valor de A:"))

    b= float(input("Digite o valor de B:"))
    c= float(input("Digite o valor de C:"))

# Calcule o discriminante
delta = b ** 2-4 * a * c 

# Verifique o valor do discrominante
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print("A equação possui uma rais real: x =",x)
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print("A equação possui duas raízes reais: x1 =", x1 ," x2 =  ", x2)