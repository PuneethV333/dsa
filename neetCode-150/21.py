def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0 for _ in temperatures]

    for i in range(len(temperatures)):
        nextMax = 0
        for j in range(i + 1, len(temperatures)):
            print(temperatures[j], temperatures[i])
            nextMax += 1
            if temperatures[j] > temperatures[i]:
                res[i] = nextMax
                break

    return res


print(dailyTemperatures([22, 21, 20]))
