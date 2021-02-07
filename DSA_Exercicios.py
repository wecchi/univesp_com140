nao_primos = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primos = [x for x in range(2, 50) if x not in nao_primos]
print(primos[15])