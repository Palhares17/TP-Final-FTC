from collections import defaultdict

class AutomatoFinitoDeterministico:
    def __init__(self, estados, estado_inicial, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.transicoes = transicoes
        self.estado_atual = estado_inicial
        self.estados_finais = None

    def initialize(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.estado_atual = estado_inicial

    def process_input(self, simbolo):
        estado_atual = self.estado_inicial

        for s in simbolo:
            if (estado_atual, s) in self.transicoes:
                 estado_atual = self.transicoes[(estado_atual, s)][0]
            else:

                estado_atual = 'ERRO'
            break

        return estado_atual

    def is_accepting_state(self, estado):
         return estado in self.estados_finais

    def get_current_state(self):
        return self.estado_atual

    def read_afd(file_path):
        with open('arquivo/AFD.txt', 'r') as file:
            linhas = file.readlines()

        e = linhas[0].strip().split(' ')[1:]
        transicoes = {}

        for estado in e:
            transicoes[estado] = {}

    # Dicionário para armazenar as instâncias de ClasseEstado
        estados = []

        for linha in linhas[3:]:
            if linha.strip() == '---':
                break
            
            parts = linha.strip().split('->')
            estado = parts[0].strip()
            transition = parts[1].strip().split('|')
            prox_estado = transition[0].strip()
            valor_entrada = transition[1].strip()

            transicoes[estado][valor_entrada] = prox_estado

            for i in transicoes:
                print(transicoes[i])

        return AutomatoFinitoDeterministico(e, estado, transicoes)


maquina = AutomatoFinitoDeterministico.read_afd('arquivo/AFD.txt')