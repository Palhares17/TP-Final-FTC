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
            print('Transição:', (prox_estado, saida))
            return saida
        else:
            self.estado_atual = 'erro'
            print('Transição falhou: Ingrediente inválido! A receita foi arruinada.')
            return 'Ingrediente inválido! A receita foi arruinada.'

    def getEstadoAtual(self):
        return self.estado_atual

    def leituraArq(file_path):
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        estados = linhas[0].strip().split(' ')[1:]
        transicoes = {}
        saidas = {}

        for estado in estados:
            transicoes[estado] = {}
            saidas[estado] = {}

        print("Estados lidos:", estados)

        for linha in linhas[3:]:
            if linha.strip() == '---':
                break

            parte = linha.strip().split('->')
            estado = parte[0].strip()
            transition = parte[1].strip().split('|')
            prox_estado = transition[0].strip()
            valor_entrada = transition[1].strip()
            saida = transition[2].strip()

            transicoes[estado][valor_entrada] = (prox_estado, saida)
            saidas[estado][valor_entrada] = saida

        return MaquinaMealy(estados, 'I', transicoes, saidas)

maquina = MaquinaMealy.leituraArq('arquivo/Mealy.txt')

resposta = 's'
while resposta != 'n':
    resposta = input('Deseja adicionar um ingrediente? (s/n): ')
    if resposta == 'n':
        break
    simbolo = input('Adicione o ingrediente: ')
    saida = maquina.transitar(simbolo)

    if maquina.getEstadoAtual() != 'erro':
        print('Ação:', saida)
        print('Estado Atual:', maquina.getEstadoAtual())
    else:
        print('Erro:', saida)
        break