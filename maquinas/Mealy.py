class MaquinaMealy:
    def __init__(self, estados, estado_inicial, transicoes, saidas):
        self.estados = estados 
        #armazena os estados possiveis da maquina

        self.estado_inicial = estado_inicial 
        #define estado inicial 

        self.transicoes = transicoes 
        #guarda as transições entre os estado

        self.saidas = saidas 
        #contem as saidas associadas a cada transicao

        self.estado_atual = estado_inicial 
        #define o estado atual da maquina
    
    def transitar(self, simbolo):

        #verifica se o símbolo está nas transições possíveis a partir do estado atual
        if simbolo in self.transicoes[self.estado_atual]:
            prox_estado, saida = self.transicoes[self.estado_atual][simbolo]
            self.estado_atual = prox_estado
            print('Transição bem-sucedida:', (prox_estado, saida))
            return saida
        else:
            #se o simbolo nao estiver nas transicoes possiveis do estado atual, define como erro
            self.estado_atual = 'erro'
            return 'Ingrediente inválido! A receita foi arruinada.'

    def getEstadoAtual(self):
        return self.estado_atual

    @staticmethod
    def leituraArq(file_path):
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        estados = linhas[0].strip().split(' ')[1:]
        transicoes = {}

        #inicializando o dicionário de transições para cada estado
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
            if len(transition) < 3:
                continue

            prox_estado = transition[0].strip()
            valor_entrada = transition[1].strip()
            saida = transition[2].strip()

            #verificando se o estado existe nos estados lidos
            if estado in transicoes:
                transicoes[estado][valor_entrada] = (prox_estado, saida)
            else:
                print(f"Erro: Estado '{estado}' não encontrado entre os estados lidos.")

        return MaquinaMealy(estados, 'I', transicoes, {})
