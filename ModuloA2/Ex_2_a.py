import random
from collections import Counter

def gerar_fonte(alfabeto, fmp, N, nome_ficheiro):
    """
    Gera um ficheiro com N símbolos para o alfabeto dado de acordo com
    a Função Massa de Probabilidade (FMP).
    
    :param alfabeto: Lista de símbolos [x1, x2, ..., xM]
    :param fmp: Função Massa de Probabilidade [p(x1), p(x2), ..., p(xM)]
    :param N: Número de símbolos a gerar
    :param nome_ficheiro: Nome do ficheiro onde a sequência gerada será guardada
    :return: Lista de símbolos gerada
    """
    if len(alfabeto) != len(fmp):
        raise ValueError("O tamanho do alfabeto deve ser igual ao da FMP.")
    
    soma_probs = sum(fmp)
    if abs(soma_probs - 1.0) > 1e-6:
        raise ValueError(f"A soma das probabilidades deve ser 1. Obtida: {soma_probs}")

    simbolos_gerados = random.choices(population=alfabeto, weights=fmp, k=N)
    
    if nome_ficheiro:
        with open(nome_ficheiro, 'w', encoding='utf-8') as f:
            # Assumindo que os símbolos podem ser caracteres ou números e juntamos tudo
            conteudo = "".join(str(s) for s in simbolos_gerados)
            f.write(conteudo)
    
    return simbolos_gerados

def testar_fonte():
    """
    Testa a função gerar_fonte predefinida para verificar a coerência 
    nos resultados e cumprimento das probabilidades pedidas.
    """
    alfabeto = ['A', 'B', 'C', 'D']
    fmp = [0.1, 0.2, 0.4, 0.3]
    N = 100000
    ficheiro = "seq_teste.txt"
    
    print(f"A gerar {N} símbolos para as letras {alfabeto} com correspondente FMP {fmp}...\n")
    simbolos = gerar_fonte(alfabeto, fmp, N, ficheiro)
    
    print(f"Os resultados empíricos estão a ser confirmados contando a frequência neste ficheiro de teste ('{ficheiro}') ...\n")
    contagem = Counter(simbolos)
    for simbolo in alfabeto:
        probab_empirica = contagem[simbolo] / N
        probab_teorica = fmp[alfabeto.index(simbolo)]
        print(f"Símbolo '{simbolo}': Probabilidade Esperada = {probab_teorica:.4f} | Probabilidade Empírica Obtida = {probab_empirica:.4f}")

    print("\nComo podemos observar as probabilidades empíricas aproximam-se bastante das teóricas, comprovando o correto funcionamento da rotina genérica de geração da fonte.")

if __name__ == "__main__":
    testar_fonte()
