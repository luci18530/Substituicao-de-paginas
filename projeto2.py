def fifo(quadros_memoria, referencias):
    memoria = []
    faltas = 0
    for pagina in referencias:
        # Verifica se a página não está na memória
        if pagina not in memoria:
            # Se ainda houver espaço na memória, adiciona a página
            if len(memoria) < quadros_memoria:
                memoria.append(pagina)
            else:
                # Se a memória estiver cheia, remove a página mais antiga e adiciona a nova
                memoria.pop(0)
                memoria.append(pagina)
            faltas += 1
    return faltas

def otm(quadros_memoria, referencias):
    memoria = []
    faltas = 0
    for i in range(len(referencias)):
        pagina = referencias[i]
        if pagina not in memoria:
            if len(memoria) < quadros_memoria:
                memoria.append(pagina)
            else:
                # Calcula o uso futuro de cada página na memória para determinar qual remover
                usos_futuros = [0] * quadros_memoria
                for j in range(quadros_memoria):
                    if memoria[j] in referencias[i+1:]:
                        usos_futuros[j] = referencias[i+1:].index(memoria[j])
                    else:
                        usos_futuros[j] = float('inf')
                memoria.pop(usos_futuros.index(max(usos_futuros)))
                memoria.append(pagina)
            faltas += 1
    return faltas

def lru(quadros_memoria, referencias):
    memoria = []
    faltas = 0
    for pagina in referencias:
        if pagina not in memoria:
            if len(memoria) < quadros_memoria:
                memoria.append(pagina)
            else:
                # Se a memória estiver cheia, remove a página menos recentemente usada
                memoria.pop(0)
                memoria.append(pagina)
            faltas += 1
        else:
            # Atualiza a ordem das páginas na memória
            memoria.remove(pagina)
            memoria.append(pagina)
    return faltas

def main():
    with open('teste.txt', 'r') as f:
        linhas = f.readlines()
    quadros_memoria = int(linhas[0])
    referencias = [int(linha.strip()) for linha in linhas[1:]]
    
    faltas_fifo = fifo(quadros_memoria, referencias)
    faltas_otm = otm(quadros_memoria, referencias)
    faltas_lru = lru(quadros_memoria, referencias)
    
    print('FIFO', faltas_fifo)
    print('OTM', faltas_otm)
    print('LRU', faltas_lru)

if __name__ == "__main__":
    main()
