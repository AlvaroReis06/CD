def mult_of_6(num):
    lim = num**2    
    start = min(num, lim)
    final = max(num, lim)
    
    print(f"\nNúmeros múltiplos de 6 em {start} e {final}:")
    
    for i in range(start, final+1):
        if i % 6 == 0:
            print(i)
        


#main
repeat = 3
for _ in range(repeat):
    number= int(input("Escolhe um número:"))
    mult_of_6(number)
