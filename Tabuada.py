import msvcrt

print("Exercício - Tabuadas")

def validar_numero(mensagem):
    while True:
        try:
            print()
            valor = int(input(mensagem))
        except:
            print("Só é permitido números. Tente novamente!")
            print()
            continue
        if valor > 0:
            return valor
        print("Não é permitido valores negativos. Tente novamente!\n")

inicioTabuada = validar_numero("Digite o valor do início da tabuada: ")
finalTabuada = validar_numero("Digite o valor do final da tabuada: ")
inicioMultiplicador = validar_numero("Digite o valor do início do multiplicador: ")
finalMultiplicador = validar_numero("Digite o valor do final do multiplicador: ")

for i in range(inicioTabuada, finalTabuada + 1):
    print(f"--------------- TABUADA DO {i} ---------------\n")

    for j in range(inicioMultiplicador, finalMultiplicador + 1):
        calculo = i * j
        print(f"{i} x {j} = {calculo}".ljust(15))

    print()
    print("Pressione 'S' para continuar, qualquer outra tecla para sair.")

    tecla = msvcrt.getch().decode().upper()
    if tecla != "S":
        break