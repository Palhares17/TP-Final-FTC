from collections import defaultdict

class APD:
    def __init__(self, estados, estado_inicial, estado_final, transicoes):
        self.estados = estados
        #atribui a lista de estados fornecida ao atributo 'estados' da instância

        self.estado_inicial = estado_inicial
        #armazena o estado inicial no atributo 'estado_inicial'

        self.estado_final = estado_final
        #armazena o estado final no atributo 'estado_final'

        self.transicoes = transicoes
        #atribui o dicionário de transições ao atributo 'transicoes' da instância

        self.estado_atual = estado_inicial

        self.pilha = []
        #inicializa a pilha como uma lista vazia

    def transitar(self, simbolo):
        if simbolo in self.transicoes[self.estado_atual]:
            prox_estado, desempilha, empilha = self.transicoes[self.estado_atual][simbolo]

            if desempilha != '&':
                if self.pilha and self.pilha[-1] == desempilha:
                    self.pilha.pop()
                else:
                    self.estado_atual = 'erro'
                    return self.estado_atual

            if empilha != '&':
                for char in empilha:
                    self.pilha.append(char)

            self.estado_atual = prox_estado
        else:
            print(f"Erro: Transição não encontrada")
            self.estado_atual = 'erro'

        if 'r' in self.pilha:
            print('A receita está vermelha demais!')
            print(f'\033[0;31mEstado Atual: {self.estado_atual}')
            print(f'Pilha: {self.pilha} \033[0m')
        if 'b' in self.pilha:
            print('A receita está azul demais!')
            print(f'\033[0;34mEstado Atual: {self.estado_atual}')
            print(f'Pilha: {self.pilha} \033[0m')
        if 'g' in self.pilha:
            print('A receita está verde demais!')
            print(f'\033[0;32mEstado Atual: {self.estado_atual}')
            print(f'Pilha: {self.pilha} \033[0m')
            
        return self.estado_atual

    def get_estado_atual(self):
        return self.estado_atual

    def leituraArq(file_path):
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        # Leitura dos estados, alfabeto, estado inicial e estado final
        estados = linhas[0].strip().split(':')[1].strip().split()
        alfabeto = linhas[1].strip().split(':')[1].strip().split()
        estado_inicial = linhas[2].strip().split(':')[1].strip()
        estado_final = linhas[3].strip().split(':')[1].strip()
        transicoes = defaultdict(dict)

        # Leitura das transições
        for linha in linhas[4:]:
            if linha.strip() == '---':
                break

            parte = linha.strip().split('->')
            if len(parte) != 2:
                print(f"Erro ao processar a linha: {linha}")
                continue  # Pula a linha com erro
            
            estado = parte[0].strip()
            transicoes_bruta = parte[1].strip().split('|')

            prox_estado = transicoes_bruta[0].strip()
            valor_entrada = transicoes_bruta[1].strip()
            desempilha = transicoes_bruta[2].strip()
            empilha = transicoes_bruta[3].strip()

            transicoes[estado][valor_entrada] = (prox_estado, desempilha, empilha)

        return APD(estados, estado_inicial, estado_final, transicoes)

