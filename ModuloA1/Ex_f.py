def intersecao_vetores(v1, v2):
    # O operador '&' encontra os elementos que estão em AMBOS os conjuntos
    result = list(set(v1) & set(v2))
    
    if not result:
        print("Vetor vazio") 
        return []
    
    print(result)
    return result

#main

repeat = 3
for _ in range(repeat):
    vetor1 = list[int](input().split())    
    vetor2 = list[int](input().split())
    intersecao_vetores(vetor1, vetor2)
