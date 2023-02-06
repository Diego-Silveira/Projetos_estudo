# sistema de fila de atendimento  de um banco utilizando listas:

ultimo = 10

fila = list(range(1,ultimo))

while True:
    print(f"Existem {len(fila)} clietes na fila.")
    print(f"Fila atual: {fila}")
    print(f"Digite f para adicionar um cliente ao final da fila. ")
    print("Digite r para realizar um atendimento  ou s para sair.")

    operacao = input("digite f,r ou s: ")

    if operacao == "f":
        fila.append(len(fila) + 1)
    elif operacao == "r":
        if len(fila) < 1:
            print(f"Não tem mais nimguém na fila para atender.")
            break
        else:
            fila.pop(0)
    elif operacao == "s":
        print("O programa será encerrado.")
        break

