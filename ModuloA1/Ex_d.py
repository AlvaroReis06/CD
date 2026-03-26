import math

def resolve_equacao(a, b, c):
    print(f"{a}x^2 + {b}x + {c} = 0")
    delta = b**2 - 4*a*c   
    if delta < 0:
        print("A equação não possui raízes reais.")
        return None
    elif delta == 0:
        x = -b / (2*a)
        print(x)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(x1, x2)
        return x1, x2
    

#main
repeat = 3
for _ in range(repeat):
    a = float(input("x^2: "))
    b = float(input("x: "))
    c = float(input("termo independente: "))
    resolve_equacao(a, b, c)
 
