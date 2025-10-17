howmany = 10000000

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

x = []
y = []
for i in range(1, howmany + 1):
    steps = collatz_steps(i)
    x.append(i)
    y.append(steps)
    print(f"{i} → {steps} steps, 콜라츠 추측 성립")

print(f"\n1부터 {howmany}까지의 수 중 총 {len(x)}개의 수가 콜라츠 추측을 만족함")