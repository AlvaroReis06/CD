from collections import Counter

def estatisticas_manual(v):
    if not v: return "Vetor vazio"
    
    v_min = min(v) 
    v_max = max(v) 
    v_media = sum(v) / len(v) 
    
    # Moda: conta a frequência de cada elemento
    contagem = Counter(v) 
    f_maxima = max(contagem.values())
    v_moda = [k for k, val in contagem.items() if val == f_maxima] 
    
    print(f"Min={v_min}, Max={v_max}, Média={v_media}, Moda={v_moda}")

#main

repeat = 3
for _ in range(repeat):
    vetor = list[int](input().split())  
    estatisticas_manual(vetor)

