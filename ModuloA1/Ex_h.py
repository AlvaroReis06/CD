

def inv_file(nome_entrada, nome_saida):
    with open(nome_entrada, 'r') as f:
        linhas = f.read()
    
    # Inverte a ordem das linhas
    linhas_invertidas = linhas[::-1]
    
    with open(nome_saida, 'w') as f:
        f.writelines(linhas_invertidas)
        
#main
repeat = 3
for _ in range(repeat):
    inv_file('g.txt', 'l2.txt')







        