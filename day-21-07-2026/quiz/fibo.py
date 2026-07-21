def fibo(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    series = [0, 1]
    for i in range(2, n):
        next_term = series[-1]+series[-2]
        series.append(next_term)
    return series
print(fibo(10))
