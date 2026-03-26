import os
import zipfile
import matplotlib.pyplot as plt
from unittest.mock import patch
from Ex_a import analisar_fonte

def extrair_e_analisar():
    zip_path = "TestFilesCD.zip"
    extract_dir = "TestFilesCD_extracted"
    
    # Extrair ficheiros
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            print(f"Ficheiros extraídos para a pasta '{extract_dir}'.")
    else:
        print(f"Pasta '{extract_dir}' já existe. A usar os ficheiros extraídos previamente.")
             
    print("\n--- Início da Análise dos Ficheiros ---")
    
    ficheiros_analisados = 0
    # Iterar sobre ficheiros
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Criar um mock para o plt.show para guardar a figura em vez de bloquear a execução
            def make_fake_show(pth):
                def fake_show(*args, **kwargs):
                    plot_filename = pth + "_hist.png"
                    plt.savefig(plot_filename)
                    plt.close()
                    print(f"    Histograma guardado em: {plot_filename}\n")
                return fake_show
                
            with patch("matplotlib.pyplot.show", side_effect=make_fake_show(file_path)):
                analisar_fonte(file_path)
            ficheiros_analisados += 1

    print(f"\nTotal de ficheiros analisados: {ficheiros_analisados}")

    print("\n--- Comentários Finais ---")
    comentario = """
Comentário aos resultados:
Ao analisar os ficheiros de 'TestFilesCD.zip', podemos observar variações na entropia e nos respetivos histogramas, dependendo do tipo do ficheiro:
1. Ficheiros de texto plano/código (como .c, .java, .txt, .kt, .htm): Tendem a ter uma distribuição não uniforme dos símbolos, concentrada nos carateres ASCII imprimíveis (espaços em branco e letras minúsculas são os mais frequentes), o que reflete uma redundância estrutural da linguagem, resultando num valor de entropia claramente abaixo dos 8 bits teóricos.
2. Ficheiros imagem / binários (como .jpg, .gif, .tif, .bmp): Ficheiros muito comprimidos como os JPEG, onde a informação original foi codificada de forma eficiente, aparentam uma quase perfeita equiprobabilidade de todos os 256 símbolos no histograma (entropia de ~7.9 bits/símbolo). Formatos de matriz de píxeis não comprimidos ou em paletas indexadas variam conforme o logótipo/fotografia, mas têm habitualmente valores de entropia mais altos do que o texto liso devido à elevada variação dos bytes para representar cores RGB.
Numa fase de compressão de dados, entropias altas requerem piores rácios de compressão face aos ficheiros de texto, que ainda mantêm elevada variabilidade na distribuição de probabilidades da respetiva fonte.
"""
    print(comentario)

if __name__ == "__main__":
    extrair_e_analisar()
