class ClasseEstado:
    def __init__(self, estados, proxEstado, ingrediente):
        self.nome = estados
        self.ingrediente = ingrediente
        self.proxEstado = proxEstado
    
    def imprimir(self):
        print(self.nome, self.ingrediente, self.proxEstado)

    def validacao(self, ing):
        if self.proxEstado == 'erro':
            print('Deu erro')
            return
        else:
            if self.ingrendiente == ing:
                return True
            else:
                self.proxEstado = 'erro'

def leituraArquivo():
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

        # Criar instância de ClasseEstado e adicionar à lista
        instancia_estado = ClasseEstado(estado, prox_estado, valor_entrada)
        estados.append(instancia_estado)

    # # Imprimir todas as instâncias criadas
    for instancia in estados:
        print('Transicao: ')
        instancia.imprimir()
        print('\n')

# Chamar a função para leitura e processamento do arquivo
leituraArquivo()
