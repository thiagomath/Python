def conta_numeros(n):
    p = 0
    for num in range(n+1):
        if num%2 == 0:
            p += 1
    print(p)


conta_numeros(10)
