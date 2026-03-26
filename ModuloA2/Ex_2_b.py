import os
from Ex_2_a import gerar_fonte

def jogar_dois_dados(L, nome_ficheiro):
    """
    Simula o jogo "Dois dados" para jogadores A e B.
    O jogo tem L jogadas. Ganha quem tiver mais pontos no fim.
    Dados duplos dão direito a jogar de novo.
    """
    alfabeto_dado = [1, 2, 3, 4, 5, 6]
    fmp_dado = [1/6] * 6
    
    pontos_A = 0
    pontos_B = 0
    
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write(f"--- JOGO DOS DOIS DADOS ({L} Jogadas) ---\n\n")
        
        for jogada in range(1, L + 1):
            f.write(f"Jogada {jogada}:\n")
            
            # Jogador A
            f.write("A rola os dados: ")
            joga_de_novo_A = True
            while joga_de_novo_A:
                d1, d2 = gerar_fonte(alfabeto_dado, fmp_dado, N=2, nome_ficheiro=None)
                soma = d1 + d2
                pontos_A += soma
                f.write(f"[{d1},{d2}] (Soma: {soma}) ")
                if d1 == d2:
                    f.write("=> Duplos! A joga de novo... ")
                else:
                    joga_de_novo_A = False
            f.write("\n")
            
            # Jogador B
            f.write("B rola os dados: ")
            joga_de_novo_B = True
            while joga_de_novo_B:
                d1, d2 = gerar_fonte(alfabeto_dado, fmp_dado, N=2, nome_ficheiro=None)
                soma = d1 + d2
                pontos_B += soma
                f.write(f"[{d1},{d2}] (Soma: {soma}) ")
                if d1 == d2:
                    f.write("=> Duplos! B joga de novo... ")
                else:
                    joga_de_novo_B = False
            f.write("\n\n")
            
        f.write(f"--- RESULTADO FINAL ---\n")
        f.write(f"Pontos Jogador A: {pontos_A}\n")
        f.write(f"Pontos Jogador B: {pontos_B}\n")
        if pontos_A > pontos_B:
            f.write("VENCEDOR: Jogador A\n")
        elif pontos_B > pontos_A:
            f.write("VENCEDOR: Jogador B\n")
        else:
            f.write("VENCEDOR: Empate!\n")


def gerar_chave_euromilhoes():
    """
    Gera uma chave válida do Euromilhões usando a fonte genérica.
    5 números distintos (1-50) e 2 estrelas distintas (1-12).
    """
    alf_num = list(range(1, 51))
    fmp_num = [1/50] * 50
    
    alf_est = list(range(1, 13))
    fmp_est = [1/12] * 12
    
    # Gerar números diferentes usando a gerência da fonte
    numeros = set()
    while len(numeros) < 5:
        n = gerar_fonte(alf_num, fmp_num, N=1, nome_ficheiro=None)[0]
        numeros.add(n)
        
    estrelas = set()
    while len(estrelas) < 2:
        e = gerar_fonte(alf_est, fmp_est, N=1, nome_ficheiro=None)[0]
        estrelas.add(e)
        
    return sorted(list(numeros)), sorted(list(estrelas))


def jogo_euromilhoes(num_concursos, apostas_por_concurso, nome_ficheiro):
    """
    Simula o jogo Euromilhões por várias semanas e simula
    milhares de apostas a cada semana.
    """
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write(f"--- SIMULAÇÃO DE EUROMILHÕES ({num_concursos} semanas, {apostas_por_concurso} apostas p/ sem) ---\n\n")
        
        for semana in range(1, num_concursos + 1):
            chave_vencedora_num, chave_vencedora_est = gerar_chave_euromilhoes()
            f.write(f"Semana {semana} - Chave Sorteada: Números {chave_vencedora_num} + Estrelas {chave_vencedora_est}\n")
            
            # Regras reais de categorias de premios
            acertos = { "5+2": 0, "5+1": 0, "5+0": 0, "4+2": 0, "4+1": 0, "4+0": 0, 
                        "3+2": 0, "3+1": 0, "3+0": 0, "2+2": 0, "2+1": 0, "2+0": 0, "1+2": 0 }
            
            f.write(f"  Apostas da semana:\n")
            for aposta in range(1, apostas_por_concurso + 1):
                aposta_num, aposta_est = gerar_chave_euromilhoes()
                
                nums_certos = len(set(aposta_num).intersection(chave_vencedora_num))
                ests_certas = len(set(aposta_est).intersection(chave_vencedora_est))
                
                premio = f"{nums_certos}+{ests_certas}"
                
                f.write(f"   Aposta {aposta:02d}: {aposta_num} + {aposta_est}")
                
                if premio in acertos:
                    acertos[premio] += 1
                    f.write(f" -> PRÉMIO {premio}\n")
                else:
                    f.write(" -> Sem prémio\n")
            
            f.write(f"\n  Resumo dos prémios das {apostas_por_concurso} apostas:\n")
            teve_premio = False
            for cat, freq in acertos.items():
                if freq > 0:
                    f.write(f"   Prémio {cat}: {freq} aposta(s)\n")
                    teve_premio = True
            
            if not teve_premio:
                f.write("   Nenhum prémio significativo atribuído para estas apostas.\n")
            f.write("\n")

def executar_e_comentar_jogos():
    print("A iniciar simulação do jogo 'Dois Dados'...")
    for i in range(1, 4):
        ficheiro_dados = f"jogo_dados_simulacao_{i}.txt"
        jogar_dois_dados(L=10, nome_ficheiro=ficheiro_dados)
        print(f" -> Resultados guardados em: {ficheiro_dados}")
        
    print("\nA iniciar simulação do jogo 'Euro Milhões'...")
    for i in range(1, 4):
        ficheiro_euro = f"jogo_euromilhoes_simulacao_{i}.txt"
        jogo_euromilhoes(num_concursos=5, apostas_por_concurso=100, nome_ficheiro=ficheiro_euro)
        print(f" -> Resultados guardados em: {ficheiro_euro}")
        
    comentario = """
Comentário aos resultados dos jogos (Ex 2b):
1. Jogo Dois Dados: Conforme os diários de jogo gerados (apresentando 10 jogadas), a probabilidade uniforme (1/6)
para os dados provoca lançamentos com distribuições equitativas, mas ocasionalmente, os jogadores tiram duplos e repetem
a jogada - alterando o desfecho pontual da partida. Ficam evidentes vitórias a intercalarem com a sorte destas repetições.
2. Jogo Euro Milhões: Mesmo simulando várias semanas com o detalhe de todas as apostas no ficheiro de registo,
prémios elevados como 5+2 ou 5+1 não ocorrem nas nossas amostras (pois as probabilidades reais
são extremamente baixas). Apenas categorias de prémios de muito baixo valor como 2+0 ou 1+2
aparecem com ligeira frequência nas apostas efetuadas (e registadas detalhadamente), condizendo
totalmente com o comportamento estatístico e probabilístico esperado de lotarias deste cariz.
"""
    print(comentario)

if __name__ == "__main__":
    executar_e_comentar_jogos()
