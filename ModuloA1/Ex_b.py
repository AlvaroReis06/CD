def minimomultiplocomum(a, b):
    if a == 0 or b == 0:
        return 0

    maior = max(abs(a), abs(b))
    mmc = maior

    while True:
        if mmc % a == 0 and mmc % b == 0:
            return mmc

        mmc += maior

#main
repeat = 3
for _ in range(repeat):
    a = int(input())
    b = int(input())
    print(f"O MMC entre {a} e {b} é: {minimomultiplocomum(a, b)}")