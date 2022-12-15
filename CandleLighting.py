def candleLighting(days:int) -> list[int]:
    if days == 1:
        return [10, 10, 10, 10, 10, 10, 10, 10, 10]
    else:
        candles = candleLighting(days - 1)
        upto = min(days - 1, 9)

        for i in range(upto):
            candles[i] = max(candles[i] - 1, 0)

        return candles

print(candleLighting(15))