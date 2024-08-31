from maquinas.AFD import AFD
from maquinas.APD import APD
from maquinas.Mealy import MaquinaMealy
from maquinas.Moore import MaquinaMoore
from maquinas.Turing import MaquinaTuring

def menu():
    print('Deseja ler qual Máquina de estados:\n')
    print("1. Máquina AFD")
    print("2. Máquina AP")
    print("3. Máquina de Moore")
    print("4. Máquina de Mealy")
    print("5. Máquina MT")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        maquina = AFD.leituraArq('arquivo/AFD.txt')

        resposta = 's'
        while (resposta != 'n'):
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')
            maquina.transitar(simbolo)

            if maquina.getEstadoAtual():
                print('Estado: ', maquina.getEstadoAtual())
                
            if maquina.getEstadoAtual() == 'erro':
                print('Erro')
                break


    elif opcao == "2":
        maquina = APD.leituraArq('arquivo/APD.txt')

        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')

            estado_atual = maquina.transitar(simbolo)
            print(f'Estado atual: {estado_atual}')

            if estado_atual == 'erro':
                print('Erro na transição!')
                break
            else:
                print(f'Estado atual: {estado_atual}, Pilha: {maquina.pilha}')

    elif opcao == "3":
        maquina = MaquinaMoore.leituraArq('arquivo/Moore.txt')

        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')
            saida = maquina.transitar(simbolo)
            print(f'Estado Atual: {maquina.getEstadoAtual()} | saída: {saida}')
            
        
    elif opcao == "4":
        maquina = MaquinaMealy.leituraArq('arquivo/Mealy.txt')

        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')
            saida = maquina.transitar(simbolo)
            print(f'Estado Atual: {maquina.getEstadoAtual()} | saída: {saida}')

        
    elif opcao == "5":
        maquina = MaquinaTuring.leituraArq('arquivo/Turing.txt')

        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')
            maquina.adicionar_simbolo(simbolo)
        
        maquina.transitar()
        print(f'Resultado da fita: {maquina.getFita()}')
            
    elif opcao == "0":
        print("Programa encerrado.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        menu()  # Chama o menu novamente se a opção for inválida

menu()
