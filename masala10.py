n = int(input())
narxlar = list(map(int, input().split()))

tanlangan = filter(lambda x: x >= 15000, narxlar)
chegirmali = list(map(lambda x: x - 3000, tanlangan))
print(chegirmali)