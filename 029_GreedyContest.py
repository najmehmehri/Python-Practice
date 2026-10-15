def solve():
    n = int(input())
    weights = list(map(int, input().split()))
    briber = input().strip()   # "romina" یا "ali"
    
    # مرتب‌سازی نزولی: هر دو بازیکن به صورت حریصانه سنگین‌ترین را برمی‌دارند
    weights.sort(reverse=True)
    
    romina_team = []
    ali_team = []
    
    idx = 0
    turn = "romina"
    take = 1  # اولین نوبت: رومینا فقط ۱ نفر
    
    while idx < n:
        cnt = min(take, n - idx)
        if turn == "romina":
            romina_team.extend(weights[idx:idx + cnt])
            turn = "ali"
        else:
            ali_team.extend(weights[idx:idx + cnt])
            turn = "romina"
        idx += cnt
        take = 2  # از نوبت‌های بعدی هر کدام ۲ نفر برمی‌دارند
    
    romina_sum = sum(romina_team)
    ali_sum = sum(ali_team)
    
    # تیمی که باید از آن رشوه گرفته شود = تیم حریفِ رشوه‌دهنده
    if briber == "romina":
        opponent = sorted(ali_team, reverse=True)
        my_sum = romina_sum
        opp_sum = ali_sum
    else:
        opponent = sorted(romina_team, reverse=True)
        my_sum = ali_sum
        opp_sum = romina_sum
    
    # از سنگین‌ترین عضو حریف شروع به حذف (رشوه) می‌کنیم
    bribed = []
    i = 0
    while opp_sum >= my_sum and i < len(opponent):
        bribed.append(opponent[i])
        opp_sum -= opponent[i]
        i += 1
    
    print(len(bribed))
    if bribed:
        print(*bribed)

if __name__ == "__main__":
    solve()
