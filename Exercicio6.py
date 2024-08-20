m = float(input("Digite o primeiro numero (m): "))
n = float(input("Digite o segundo numero (n): "))
produto = m * n
if produto > 0:
    print("O produto é positivo.")
elif produto < 0:
    print("O produto é negativo.")
else:
    print("O produto é zero.")