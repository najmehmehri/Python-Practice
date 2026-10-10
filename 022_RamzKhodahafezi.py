def solve():
    t = int(input("t: "))
    
    for i in range(t):
        raw = input(f"Password {i+1}: ").strip()
        
        cleaned = raw.replace(" ", "")
        
        if len(cleaned) != 6 or not cleaned.isdigit():
            print("Impossible")
            continue
        
        digits = [int(ch) for ch in cleaned]
        
        sum_first = sum(digits[:3])
        sum_second = sum(digits[3:])
        
        if sum_first == sum_second:
            print("Possible")
        else:
            print("Impossible")

    input("\n Please press any key to Exit ...")

if __name__ == "__main__":
    solve()
