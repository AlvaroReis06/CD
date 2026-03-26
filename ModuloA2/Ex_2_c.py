import string
import math
from Ex_2_a import gerar_fonte

def gerar_passwords(nivel, quantidade, nome_ficheiro):
    """
    Gera passwords consoante o nível de robustez ('baixo', 'medio', 'alto').
    """
    if nivel == 'baixo':
        alfabeto = list(string.ascii_lowercase)
        tamanho = 6
    elif nivel == 'medio':
        alfabeto = list(string.ascii_letters + string.digits)
        tamanho = 8
    elif nivel == 'alto':
        alfabeto = list(string.ascii_letters + string.digits + string.punctuation)
        tamanho = 12
    else:
        raise ValueError("Nivel invalido.")
        
    fmp = [1/len(alfabeto)] * len(alfabeto)
    
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        for _ in range(quantidade):
            pwd_caracteres = gerar_fonte(alfabeto, fmp, N=tamanho, nome_ficheiro=None)
            f.write("".join(str(c) for c in pwd_caracteres) + "\n")


def carregar_lista(nome_ficheiro):
    """
    Lê uma lista de um ficheiro de texto, ignorando linhas vazias.
    """
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8', errors='replace') as f:
            linhas = []
            for linha in f:
                linha = linha.strip()
                if not linha or linha.startswith("---") or linha.startswith("Distrito"):
                    continue
                linhas.append(linha)
            return linhas
    except FileNotFoundError:
        return ["Desconhecido"]

def extrair_localidade(linha_localidade):
    """
    Extrai a localidade do formato do ficheiro Localidades.txt
    'Aveiro    Águeda    Agadão    496    3 534'
    """
    if '    ' in linha_localidade:
        partes = [p.strip() for p in linha_localidade.split('    ') if p.strip()]
        if len(partes) >= 3:
            return partes[2]  # Devolve a Freguesia
    # fallback
    return linha_localidade.split()[0] if linha_localidade else "Desconhecido"

def gerar_tabela_pessoas(quantidade, nome_ficheiro):
    """
    Gera tabela de pessoas ('ID', 'Nome', 'Localidade', 'Profissão').
    O 1º dígito do ID segue a Lei de Benford.
    """
    nomes = carregar_lista("Nomes.txt")
    apelidos = carregar_lista("Apelidos.txt")
    profissoes = carregar_lista("Profissoes.txt")
    linhas_localidades = carregar_lista("Localidades.txt")
    
    localidades = [extrair_localidade(loc) for loc in linhas_localidades]
    if not localidades: localidades = ["Desconhecida"]

    alf_benford = list(range(1, 10))
    fmp_benford = [math.log10(1 + 1/d) for d in alf_benford]
    
    alf_dig = list(range(10))
    fmp_dig = [0.1] * 10
    
    # Preparar FMP uniformes para cada lista de palavras
    fmp_nomes = [1/len(nomes)] * len(nomes)
    fmp_apelidos = [1/len(apelidos)] * len(apelidos)
    fmp_profissoes = [1/len(profissoes)] * len(profissoes)
    fmp_localidades = [1/len(localidades)] * len(localidades)

    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write("ID,Nome,Localidade,Profissao\n")
        
        for _ in range(quantidade):
            # ID: 1 algarismo Benford + 7 algarismos uniformes
            d1 = gerar_fonte(alf_benford, fmp_benford, N=1, nome_ficheiro=None)[0]
            resto = gerar_fonte(alf_dig, fmp_dig, N=7, nome_ficheiro=None)
            str_id = str(d1) + "".join(str(d) for d in resto)
            
            nome = gerar_fonte(nomes, fmp_nomes, N=1, nome_ficheiro=None)[0]
            apelido = gerar_fonte(apelidos, fmp_apelidos, N=1, nome_ficheiro=None)[0]
            nome_completo = f"{nome} {apelido}"
            
            loc = gerar_fonte(localidades, fmp_localidades, N=1, nome_ficheiro=None)[0]
            prof = gerar_fonte(profissoes, fmp_profissoes, N=1, nome_ficheiro=None)[0]
            
            # Limpar possiveis virgulas nos campos para o CSV não quebrar
            nome_completo = nome_completo.replace(",", "")
            loc = loc.replace(",", "")
            prof = prof.replace(",", "")
            
            f.write(f"{str_id},{nome_completo},{loc},{prof}\n")

def executar_e_comentar_2c():
    print("A gerar ficheiros de passwords (1000 linhas cada)...")
    ficheiros_pwd = ["passwords_baixo.txt", "passwords_medio.txt", "passwords_alto.txt"]
    niveis = ["baixo", "medio", "alto"]
    
    for ficheiro, nivel in zip(ficheiros_pwd, niveis):
        gerar_passwords(nivel, quantidade=1000, nome_ficheiro=ficheiro)
        print(f" -> Guardado: {ficheiro} (Nível: {nivel})")
        
    print("\nA gerar ficheiros de Tabela Pessoas (1000 linhas cada)...")
    for i in range(1, 4):
        ficheiro_pessoas = f"pessoas_tabela_{i}.csv"
        gerar_tabela_pessoas(quantidade=1000, nome_ficheiro=ficheiro_pessoas)
        print(f" -> Guardado: {ficheiro_pessoas}")
        
    comentario = """
Comentário aos resultados (Ex 2c):
1. Passwords (1000 linhas por ficheiro):
- Nível 'baixo': A fonte uniforme usa as 26 letras minúsculas em 6 caracteres num total de ~308 milhões de hipóteses que, em ataques modernos, são quebradas de forma imediata face à entropia reduzida e ao curto limiar das opções.
- Nível 'médio': Utilizando 62 caracteres ao longo de 8 posições atinge >200 biliões de hipóteses, o que requer recursos elevados para quebrar mediante força-bruta não guiada.
- Nível 'alto': Os ~94 carateres normais da linguagem de formatação ASCII, aliados a 12 caracteres seguram uma entropia que garante a impossibilidade computacional na força-bruta atualmente.
2. Tabela Pessoas (Três ficheiros CSV c/ 1000 linhas cada):
Sendo analisáveis num espetro quantitativo os ficheiros mostram IDs gerados de 8 algarismos. Observa-se que na casa do ID da pessoa, a Lei de Benford aplica a sua regra com cerca de 30% incidência para IDs terminados em '1' na cabeça dos milhares de milhões, mitigando sequências artificiais tipicamente lineares. As cidades e localidades mostram também que as tabelas de atributos funcionam com extração afortunada.
"""
    print(comentario)

if __name__ == "__main__":
    executar_e_comentar_2c()
