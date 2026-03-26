import math
from collections import Counter
import matplotlib.pyplot as plt

def analisar_fonte(caminho_ficheiro):
    """
    Analisa um ficheiro como uma fonte de símbolos (bytes).
    """
    try:
        with open(caminho_ficheiro, 'rb') as f:
            dados = f.read()
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{caminho_ficheiro}' não foi encontrado.")
        return

    total_simbolos = len(dados)
    if total_simbolos == 0:
        print("Ficheiro vazio.")
        return

    frequencias = Counter(dados)

    probabilidades = {simbolo: freq / total_simbolos for simbolo, freq in frequencias.items()}

    simbolo_mais_frequente = max(probabilidades, key=probabilidades.get)
    prob_max = probabilidades[simbolo_mais_frequente]
    
    info_propria = -math.log2(prob_max)

    print(f"--- Resultados para: {caminho_ficheiro} ---")
    
    simbolo_legivel = chr(simbolo_mais_frequente) if 32 <= simbolo_mais_frequente <= 126 else 'Não Imprimível'
    
    print(f"(i) Símbolo mais frequente: {simbolo_mais_frequente} (ASCII: '{simbolo_legivel}')")
    print(f"    Probabilidade: {prob_max:.6f}")
    print(f"    Informação Própria: {info_propria:.6f} bits")

    entropia = sum(-p * math.log2(p) for p in probabilidades.values())
    print(f"(ii) Entropia da fonte: {entropia:.6f} bits/símbolo\n")

    simbolos = list(frequencias.keys())
    contagens = list(frequencias.values())

    plt.figure(figsize=(10, 6))
    plt.bar(simbolos, contagens, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de Símbolos - {caminho_ficheiro.split("/")[-1]}')
    plt.xlabel('Símbolo (Valor do Byte: 0-255)')
    plt.ylabel('Frequência (Nº de Ocorrências)')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == '__main__':
    import sys
    import os
    
    # Executa a função passando o ficheiro como argumento no terminal
    # Exemplo: python Ex_a.py ficheiro.txt
    if len(sys.argv) > 1:
        analisar_fonte(sys.argv[1])
    else:
        print("-> Dica de uso no terminal: python Ex_a.py <caminho_ficheiro>")
        print("-> A rodar com um ficheiro de demonstração predefinido...\n")
        
        ficheiro_teste = "demo_ex1a.txt"
        if not os.path.exists(ficheiro_teste):
            with open(ficheiro_teste, "w", encoding='utf-8') as f:
                f.write("AABBCCCDDDD texto de exemplo para calcular entropia e frequencias!!")
        
        analisar_fonte(ficheiro_teste)
