from collections import defaultdict

class AFD:
    def __init__(self, estados, estado_inicial, transicoes):
        self.estados = estados 
        # atribui a lista de estados fornecida ao atributo 'estados' da instância

        self.estado_inicial = estado_inicial
        #armazena o estado inicial no atributo 'estado_inicial'

        self.transicoes = transicoes
        #atribui o dicionário de transições ao atributo 'transicoes' da instância

        self.estado_atual = estado_inicial
        #define o estado inicial da máquina como o estado atual

        self.estados_finais = None
        #inicializa o atributo 'estados_finais' como None

    def initialize(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):

        self.estados = estados
        #atribui a lista de estados fornecida ao atributo 'estados' da instância

        self.alfabeto = alfabeto

        self.transicoes = transicoes
        #atribui o dicionário de transições ao atributo 'transicoes' da instância

        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

        self.estado_atual = estado_inicial
        #define o estado inicial da máquina como o estado atual

    def transitar(self, simbolo):
        if simbolo in self.transicoes[self.estado_atual]:
            self.estado_atual = self.transicoes[self.estado_atual][simbolo]
            if self.estado_atual == 'erro':
                print('\n\nTransição mal-sucedida: estado de erro alcançado.\n\n')
            else:
                print('\n\nTransição bem-sucedida:', self.estado_atual)
            #print('Transição bem-sucedida:', self.estado_atual)
        else:
            self.estado_atual = 'erro'
        
        return self.estado_atual

    def getEstadoAtual(self):
        if self.estado_atual == 'F':
            print('receita criada')
        return self.estado_atual

    def leituraArq(file_path):
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        estados = linhas[0].strip().split(' ')[1:]
        transicoes = {}

        for estado in estados:
            transicoes[estado] = {}

        for linha in linhas[3:]:
            if linha.strip() == '---':
                break
            
            parte = linha.strip().split('->')
            estado = parte[0].strip()
            transition = parte[1].strip().split('|')
            prox_estado = transition[0].strip()
            valor_entrada = transition[1].strip()

            transicoes[estado][valor_entrada] = prox_estado

        return AFD(estados, 'I', transicoes)