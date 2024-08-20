quantfotocopias = int(input("Digite a quantidade de fotocópias realizadas: "))

if quantfotocopias <= 10:
    custototal = quantfotocopias * 0.25
elif quantfotocopias <= 30:
    custototal = 10 * 0.25 + (quantfotocopias - 10) * 0.20
else:
    custototal = 10 * 0.25 + 20 * 0.20 + (quantfotocopias - 30) * 0.10
print(f"O custo total das fotocópias é R$ {custototal:.2f}.")