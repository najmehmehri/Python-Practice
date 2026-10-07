def solve():
    raw_input = input()
    s = raw_input.strip().lower()[:20]
    
    if 'm' in s:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    solve()
