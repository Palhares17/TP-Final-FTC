from collections import defaultdict

class APD:
    def __init__(self, estados, estado_inicial, estado_final, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.transicoes = transicoes
        self.estado_atual = estado_inicial
        self.pilha = []

    def transitar(self, simbolo):
        if simbolo in self.transicoes[self.estado_atual]:
            prox_estado, desempilha, empilha = self.transicoes[self.estado_atual][simbolo]
            print(f'Próximo estado: {prox_estado}, Desempilha: {desempilha}, Empilha: {empilha}')
            print(f'Pilha antes da transição: {self.pilha}')

            if desempilha != '&':
                if self.pilha and self.pilha[-1] == desempilha:
                    self.pilha.pop()
                else:
                    print(f"Erro: Tentativa de desempilhar '{desempilha}', mas o topo da pilha é '{self.pilha[-1] if self.pilha else None}'")
                    self.estado_atual = 'erro'
                    return self.estado_atual

            if empilha != '&':
                self.pilha.append(empilha)

            self.estado_atual = prox_estado
        else:
            print(f"Erro: Transição não encontrada para símbolo '{simbolo}' no estado '{self.estado_atual}'")
            self.estado_atual = 'erro'

        print(f'Estado atual após a transição: {self.estado_atual}')
        print(f'Pilha depois da transição: {self.pilha}')
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
            estado = parte[0].strip()
            transicoes_bruta = parte[1].strip().split('|')

            prox_estado = transicoes_bruta[0].strip()
            valor_entrada = transicoes_bruta[1].strip()
            desempilha = transicoes_bruta[2].strip()
            empilha = transicoes_bruta[3].strip()

            transicoes[estado][valor_entrada] = (prox_estado, desempilha, empilha)

        return APD(estados, estado_inicial, estado_final, transicoes)

# Exemplo de uso do APD
maquina = APD.leituraArq('arquivo/APD.txt')

resposta = 's'
while resposta != 'n':
    resposta = input('Deseja adicionar um ingrediente? (s/n): ')
    if resposta == 'n':
        break
    simbolo = input('Adicione o ingrediente: ')

    estado_atual = maquina.transitar(simbolo)
    print(f'Estado atual: {estado_atual}')

    if estado_atual == 'erro':
        print('Erro na transição!')
        break
    else:
        print(f'Estado atual: {estado_atual}, Pilha: {maquina.pilha}')
