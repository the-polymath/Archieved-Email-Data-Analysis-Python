lst = [2, 4, 6, 8, 10]
def rmk(a, k):
    n = len(a)
    res = lambda a, i: a[0:(i)] + a[(k+i):n]
    result = [res(a, i) for i in range(n - k + 1)]
    print(result)

rmk(lst, 3)
