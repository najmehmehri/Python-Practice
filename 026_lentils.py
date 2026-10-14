def solve():
    n, k = map(int, input().split())
    
    ans = max(0, 2 * k - n - 1)
    
    print(ans)

if __name__ == "__main__":
    solve()
