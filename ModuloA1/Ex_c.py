
def prog_arit(u,r,N):
    term = u
    
    for i in range(N):
        print(f"Termo {i+1}: {term}")
        term += r
        
#MAIN

repeat = 3
for _ in range(repeat):
    u = int(input("Digite o primeiro termo (u): "))
    r = int(input("Digite a razão (r): "))       
    N = int(input("Digite o número de termos (N): "))
    prog_arit(u, r, N)
