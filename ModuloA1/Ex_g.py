def reuniao_vetores(v1, v2):
    # O operador '|' junta os dois conjuntos e remove automaticamente duplicados
    result = list(set(v1) | set(v2)) 
    
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
    reuniao_vetores(vetor1, vetor2)
