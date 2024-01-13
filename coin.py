def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)
memo = {}
def minimum_coin(m,coins):
    if m in memo:
        return memo[m]
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            sub = m - coin
            if sub < 0:
                continue
            answer = min_ignore_none(answer,minimum_coin(sub,coins)+1)
    memo[m] = answer
    return answer
print(minimum_coin(150,[1,4,5]))