class ClasseEstado:
    def __init__(self, estados, proxEstado, ingrediente):
        self.nome = estados
        self.ingrediente = ingrediente
        self.proxEstado = proxEstado
    
    def imprimir(self):
        print(f'Estado: {self.nome}, Ingrediente: {self.ingrediente}, Próximo Estado: {self.proxEstado}')
    

def leituraArquivo():
    with open('arquivo/AFD.txt', 'r') as file:
        linhas = file.readlines()

    estados = linhas[0].strip().split(' ')[1:]
    transicoes = {}

    for estado in estados:
        transicoes[estado] = {}

    # Dicionário para armazenar as instâncias de ClasseEstado
    estados_instancias = []

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
        estados_instancias.append(instancia_estado)

    # Imprimir todas as instâncias criadas
    for instancia in estados_instancias:
        instancia.imprimir()

# Chamar a função para leitura e processamento do arquivo
leituraArquivo()
