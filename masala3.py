def daraja(son, n=2):
    return son ** n

qiymatlar = input().split()
son = int(qiymatlar[0])

if len(qiymatlar) > 1:
    print(daraja(son, int(qiymatlar[1])))
else:
    print(daraja(son))