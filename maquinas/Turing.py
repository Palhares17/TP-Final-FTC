class MaquinaTuring:
    def __init__(self, estados, estado_inicial, transicoes):
        
        self.estados = estados 
        #atribui a lista de estados fornecida ao atributo "estados" da instancia
        self.estado_atual = estado_inicial
        #define o estado inicial da maquina como o estado atual
        self.estado_inicial = estado_inicial
        #armazena o estado inicial
        self.transicoes = transicoes
        #atribui o dicionario de transicoes ao atributo 'transicoes' da instancia
        self.fita = []
        #inicializa a fita como uma lista vazia

    def adicionar_simbolo(self, simbolo):
        self.fita.append(simbolo)

    def transitar(self):
        posicao_cabecote = 0

        while True:
            simbolo_atual = self.fita[posicao_cabecote]
            
            # Verifica se há transição para o símbolo atual
            if simbolo_atual not in self.transicoes[self.estado_atual]:
                break

            transicao = self.transicoes[self.estado_atual][simbolo_atual]

            if transicao is None:
                break

            novo_simbolo, movimentacao_cabecote, prox_estado = transicao

            self.fita[posicao_cabecote] = novo_simbolo
            self.estado_atual = prox_estado

            if movimentacao_cabecote == 'E':
                posicao_cabecote -= 1
            elif movimentacao_cabecote == 'D':
                posicao_cabecote += 1

            if posicao_cabecote < 0:
                self.fita.insert(0, '_')
                posicao_cabecote = 0
            elif posicao_cabecote == len(self.fita):
                self.fita.append('_')

    def getEstadoAtual(self):
        return self.estado_atual
    
    def getFita(self):
        return ''.join(self.fita)

    @staticmethod
    def leituraArq(file_path):
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        estados = linhas[0].strip().split(' ')[1:]
        transicoes = {}

        for estado in estados:
            transicoes[estado] = {}

        #ler as transições
        for linha in linhas[1:]:
            if '->' not in linha:
                continue

            parte = linha.strip().split('->')
            estado_atual = parte[0].strip()
            partes_transicao = parte[1].strip().split('|')

            if len(partes_transicao) != 4:
                continue

            simbolo_entrada = partes_transicao[0].strip()
            simbolo_saida = partes_transicao[1].strip()
            direcao = partes_transicao[2].strip()
            proximo_estado = partes_transicao[3].strip()

            transicoes[estado_atual][simbolo_entrada] = (simbolo_saida, direcao, proximo_estado)

        return MaquinaTuring(estados, estados[0], transicoes)

