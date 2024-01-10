def solve(N):
    ans = -1
    factors = []
    simplified = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 24, 42]
    if N % 2 != 0:
        return ans
    for i in range(15):
        if N % simplified[i] == 0:
            factors.append(N // simplified[i])
    for a in range(len(factors)):
        for b in range(len(factors)):
            for c in range(len(factors)):
                for d in range(len(factors)):
                    if factors[a] + factors[b] + factors[c] + factors[d] == N:
                        if factors[a] * factors[b] * factors[c] * factors[d] > ans:
                            ans = factors[a] * factors[b] * factors[c] * factors[d]
    return ans
test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    print(solve(N))
