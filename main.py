from maquinas.AFD import AFD
from maquinas.APD import APD
from maquinas.Mealy import MaquinaMealy
from maquinas.Moore import MaquinaMoore
from maquinas.Turing import MaquinaTuring

print("""
$$$$$$$$\\ $$\\   $$\\ $$$$$$$$\\       $$\\      $$\\ $$$$$$\\ $$$$$$$$\\  $$$$$$\\  $$\\   $$\\ $$$$$$$$\\ $$$$$$$\\  
\\__$$  __|$$ |  $$ |$$  _____|      $$ | $\\  $$ |\\_$$  _|\\__$$  __|$$  __$$\\ $$ |  $$ |$$  _____|$$  __$$\\ 
   $$ |   $$ |  $$ |$$ |            $$ |$$$\\ $$ |  $$ |     $$ |   $$ /  \\__|$$ |  $$ |$$ |      $$ |  $$ |
   $$ |   $$$$$$$$ |$$$$$\\          $$ $$ $$\\$$ |  $$ |     $$ |   $$ |      $$$$$$$$ |$$$$$\\    $$$$$$$  |
   $$ |   $$  __$$ |$$  __|         $$$$  _$$$$ |  $$ |     $$ |   $$ |      $$  __$$ |$$  __|   $$  __$$< 
   $$ |   $$ |  $$ |$$ |            $$$  / \\$$$ |  $$ |     $$ |   $$ |  $$\\ $$ |  $$ |$$ |      $$ |  $$ |
   $$ |   $$ |  $$ |$$$$$$$$\\       $$  /   \\$$ |$$$$$$\\    $$ |   \\$$$$$$  |$$ |  $$ |$$$$$$$$\\ $$ |  $$ |
   \\__|   \\__|  \\__|\\________|      \\__/     \\__|\\______|   \\__|    \\______/ \\__|  \\__|\\________|\\__|  \\__|

___  ____ ___ _ ____ _  _    ____ ____ ____ ____ ___ ____ ____ 
|__] |  |  |  | |  | |\\ |    |    |__/ |___ |__|  |  |  | |__/ 
|    |__|  |  | |__| | \\|    |___ |  \\ |___ |  |  |  |__| |  \\

""")


ingredientes = {
    "ac": "Acônito",
    "ce": "Cogumelos de Esgoto",
    "dl": "Dente de Leão",
    "da": "Destilado de Anão",
    "et": "Essência das Trevas",
    "el": "Essência de luz",
    "sc": "Sangue de Carniçal",
    "ve": "Verbena",
    "va": "Veneno de Aracnas"
}

def menu():
    print('Deseja ler qual Máquina de estados:\n')
    print("1. Máquina AFD")
    print("2. Máquina AP")
    print("3. Máquina de Moore")
    print("4. Máquina de Mealy")
    print("5. Máquina MT")


    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        maquina = AFD.leituraArq('arquivo/AFD.txt')

        print("Bem vindo a Maquina de Autômato Finito\n\n")

        print("### Receita para ser criada\n")
        print("\nPapafigo\n")
        print("Buffs: Imuniza contra venenos depois de utilizado e neutraliza os efeitos dos já em ação por 60 segundos.\n")
        print("\t1x Destilado Anão\n\t4x Dente de Leão\n\t1x Essência de Luz\n")

        print("Ingredientes disponíveis:\n")
        for codigo, nome in ingredientes.items():
            print(f"{codigo}: {nome}")

        print("\n")

        resposta = 's'
        resultado = '\033[1m' + '\nErro na poção. Sequencia nao condiz com a receita!\033[0m' + '\n' * 4
        while (resposta != 'n'):
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                print(resultado)
                break
            simbolo = input('\nAdicione o ingrediente: ')

            estado_atual = maquina.transitar(simbolo)

            if estado_atual == 'erro':
                resultado = '\033[1m' + '\nErro na poção. Sequencia nao condiz com a receita!\033[0m' + '\n' * 4

            elif estado_atual == 'F':
                resultado = '\033[1m' + '\nReceita de PAPAFIGO criada!\033[0m' + '\n' * 4
                print('\033[1m' + '\nReceita de PAPAFIGO criada!\033[0m' + '\n' * 4)

        


    elif opcao == "2":
        maquina = APD.leituraArq('arquivo/APD.txt')

        print("Bem vindo a Maquina de Pilha\n\n")

        print("### Receita para ser criada\n")
        print("\nLua Cheia\n")
        print("Buffs: Aumenta a vitalidade máxima em 300 pontos por 60 segundos.")
        print("\t1x Destilado Anão\n\t2x Acônito\n\t1x Essência das Trevas\n")

        print("Ingredientes disponíveis:\n")
        for codigo, nome in ingredientes.items():
            print(f"{codigo}: {nome}")

        print("\n")

        resposta = 's'
        resultado = '\033[1m' + '\nErro na poção. Sequencia nao condiz com a receita!\033[0m' + '\n' * 4
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                print(resultado)
                break
            simbolo = input('Adicione o ingrediente: ')

            estado_atual = maquina.transitar(simbolo)

            if estado_atual == 'erro':
                resultado = '\033[1m' + '\nErro na poção. Sequencia nao condiz com a receita!\033[0m' + '\n' * 4

            elif estado_atual == 'F':
                resultado = '\033[1m' + '\nReceita de LUA CHEIA criada!\033[0m' + '\n' * 4
                print('\033[1m' + '\nReceita de LUA CHEIA criada!\033[0m' + '\n' * 4)

        
        
    
    elif opcao == "3":
        maquina = MaquinaMoore.leituraArq('arquivo/Moore.txt')

        print("Bem vindo a Maquina de Moore\n\n")

        print("### Receita para ser criada\n")
        print("\nCoruja do Mato\n")
        print("Buffs: Acelera recuperação de Estamina. 5% de regeneração de estamina em combate por 30 segundos.\n")
        print("\t1x Destilado Anão\n\t2x Verbena\n\t2x Veneno de Aracnas\n")

        print("Ingredientes disponíveis:\n")
        for codigo, nome in ingredientes.items():
            print(f"{codigo}: {nome}")

        print("\n")


        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')
            saida = maquina.transitar(simbolo)
            print(f'\033[1mEstado Atual: {maquina.getEstadoAtual()} | saída: {saida}\033[0m' + '\n' * 2)
        

        
    elif opcao == "4":
        maquina = MaquinaMealy.leituraArq('arquivo/Mealy.txt')

        print("Bem vindo a Maquina de Mealy\n\n")

        print("### Receita para ser criada\n")
        print("\nSangue Preto\n")
        print("Buffs: O sangue do Bruxo causa 15% do dano causado por vampiros e necrófagos por 30 segundos.\n")
        print("\t1x Destilado Anão\n\t2x Cogumelos de Esgoto\n\t2x Sangue de Carniçal\n")

        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar um ingrediente? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adicione o ingrediente: ')
            saida = maquina.transitar(simbolo)
            print(f'\033[1mEstado Atual: {maquina.getEstadoAtual()} | saída: {saida}\033[0m' + '\n' * 2)
        


        
    elif opcao == "5":
        maquina = MaquinaTuring.leituraArq('arquivo/Turing.txt')

        print("Bem vindo a Maquina de turing\n\n")

        print("Soma mais um ao número binário")
        resposta = 's'
        while resposta != 'n':
            resposta = input('Deseja adicionar mais um bit? (s/n): ')
            if resposta == 'n':
                break
            simbolo = input('Adione o bit: ')
            maquina.adicionar_simbolo(simbolo)
        
        maquina.transitar()
        print(f'\n\nResultado da fita: {maquina.getFita()}' + '\n' * 2)

            
    else:
        print("\033[1m" + "Opção inválida. Por favor, escolha uma opção válida.\033[0m" + '\n' * 4)    
    
    menu()  # Chama o menu novamente se a opção for inválida

menu()
