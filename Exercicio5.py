nota = float(input("Insira a nota:"))

if 0<= nota <=20:
    
    if nota >=10:
        print("Valida")
    else:
        print("Invalida")
else: 
    print("Nota Invalida, a nota precisa estar entre 0 e 20")