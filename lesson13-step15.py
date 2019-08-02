def C (n, k):
    if k == 0: return 1
    if k > n: return 0
    return C(n - 1, k) + C(n - 1, k - 1)
n1, k1 = map(int, input().split())
print (C(n1,k1))