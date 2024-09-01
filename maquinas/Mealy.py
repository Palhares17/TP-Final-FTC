class MaquinaMealy:
    def __init__(self, estados, estado_inicial, transicoes, saidas):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.transicoes = transicoes
        self.saidas = saidas
        self.estado_atual = estado_inicial

    def transitar(self, simbolo):
        if simbolo in self.transicoes[self.estado_atual]:
            prox_estado, saida = self.transicoes[self.estado_atual][simbolo]
            self.estado_atual = prox_estado
            print('Transição bem-sucedida:', (prox_estado, saida))
            return saida
        else:
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

        # Inicializando o dicionário de transições para cada estado
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

            # Verificando se o estado existe nos estados lidos
            if estado in transicoes:
                transicoes[estado][valor_entrada] = (prox_estado, saida)
            else:
                print(f"Erro: Estado '{estado}' não encontrado entre os estados lidos.")

        return MaquinaMealy(estados, 'I', transicoes, {})
