import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    a = [0] * n
    for i in range(n):
        a[i] = int(data[idx]); idx += 1

    INF = 10**18
    d = np.full((n, n), INF, dtype=np.int64)
    np.fill_diagonal(d, 0)

    for _ in range(m):
        v = int(data[idx]) - 1; idx += 1
        u = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        if w < d[v, u]:
            d[v, u] = w
            d[u, v] = w

    for k in range(n):
        np.minimum(d, d[:, k, None] + d[None, k, :], out=d)

    a_np = np.array(a, dtype=np.int64)
    cost = a_np[:, None] * d  

    for k in range(n):
        np.minimum(cost, cost[:, k, None] + cost[None, k, :], out=cost)

    out = []
    for i in range(n):
        out.append(' '.join(map(str, cost[i])))
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()
