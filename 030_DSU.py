import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    parent = list(range(n + 1))

    def find(i):
        root = i
        while root != parent[root]:
            root = parent[root]
        curr = i
        while curr != root:
            nxt_node = parent[curr]
            parent[curr] = root
            curr = nxt_node
        return root

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    nxt = list(range(n + 2))

    def find_nxt(i):
        root = i
        while root != nxt[root]:
            root = nxt[root]
        curr = i
        while curr != root:
            nxt_node = nxt[curr]
            nxt[curr] = root
            curr = nxt_node
        return root

    out = []
    idx = 2
    for _ in range(q):
        type_op = int(input_data[idx])
        x = int(input_data[idx + 1])
        y = int(input_data[idx + 2])
        idx += 3

        if type_op == 1:
            union(x, y)
        elif type_op == 2:
            curr = find_nxt(x)
            while curr < y:
                union(curr, curr + 1)
                nxt[curr] = find_nxt(curr + 1)
                curr = nxt[curr]
        else:  # type_op == 3
            if find(x) == find(y):
                out.append("YES")
            else:
                out.append("NO")

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
