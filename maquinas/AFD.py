def leituraAFD(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    estados = linhas[0].strip().split(' ')[1:]
    
    print(estados)

leituraAFD('arquivo/AFD.txt')