from collections import defaultdict

def possibleSums(coins, quantity):
    sums = {}
    N = len(coins)

    count = defaultdict(lambda: 0)
    for c, q in zip(coins, quantity):
        count[c] += q

    single_coins = list(count.keys())

    def solution(count, coins, sums, index, value):
        for j in range(1, count[coins[index]]+1):
            s = value + (coins[index] * j)
            sums[s] = True

            for k in range(index+1, len(coins)):
                solution(count, coins, sums, k, s)

    for index in range(len(single_coins)):
        solution(count, single_coins, sums, index, 0)

    return len(sums)

coins = [5, 46, 27, 17, 54, 10, 14, 54, 40, 44, 22, 61, 19, 20, 68, 40, 2, 31]
quantity = [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]

# coins = [17, 27, 22, 18, 9, 58, 50, 85, 67, 50, 42, 11, 60, 39, 23, 37, 28, 91, 81]
# quantity = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(possibleSums(coins, quantity))
