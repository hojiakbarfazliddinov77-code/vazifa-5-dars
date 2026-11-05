baholar = list(map(int, input().split()))

yuqori = list(filter(lambda b: b > 70, baholar))
print(yuqori)