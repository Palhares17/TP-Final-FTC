class MaquinaMoore:
    def __init__(self, estados, estado_inicial, transicoes, saidas):
        self.estados = estados #armazena estados possiveis da maquina
        self.estado_inicial = estado_inicial #define o estado inicial
        self.transicoes = transicoes #guarda as transições entre os estados
        self.saidas = saidas #contem as saidas relacionadas com cada estado
        self.estado_atual = estado_inicial #define o estado atual da machine
    #função p/ transitar
    def transitar(self, simbolo):
        #verificacao se simbolo esta nas transicoes a partir do estado atual
        if simbolo in self.transicoes[self.estado_atual]:
            prox_estado = self.transicoes[self.estado_atual][simbolo]
            self.estado_atual = prox_estado
            print(f"Transição para o estado {prox_estado} com a saída '{self.saidas[prox_estado]}'")
            return self.saidas[prox_estado] #retorna saida associada ao prox estado
        else:
            #se simbolo n estiver nas transições possiveis do estado atual, retorna erro
            self.estado_atual = 'erro'
            return 'Ingrediente inválido! A receita foi arruinada.'

    def getEstadoAtual(self):
        return self.estado_atual

    @staticmethod
    #funcao para leitura de arquivo
    def leituraArq(file_path):
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        estados = linhas[0].strip().split(' ')[1:]
        transicoes = {}
        saidas = {}

        #dicionário de trans. e saídas p/ cada estado
        for estado in estados:
            transicoes[estado] = {}

        for linha in linhas[2:]:
            if linha.strip() == '---':
                break

            parte = linha.strip().split('->')
            if len(parte) < 2:
                continue

            estado = parte[0].strip()
            transition = parte[1].strip().split('|')
            if len(transition) < 2:
                continue

            prox_estado = transition[0].strip()
            valor_entrada = transition[1].strip()

            transicoes[estado][valor_entrada] = prox_estado


        for linha in linhas[len(estados)+3:]: # leitura referente às saídas que estao relacionadas a cada estado
            if linha.strip() == '---':
                break

            estado, saida = linha.strip().split(':')
            estado = estado.strip()
            saida = saida.strip()
            saidas[estado] = saida

        return MaquinaMoore(estados, 'I', transicoes, saidas)

