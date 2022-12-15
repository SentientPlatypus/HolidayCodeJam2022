def candleLighting(days:int) -> list[int]:
    if days == 1:
        return [10, 10, 10, 10, 10, 10, 10, 10, 10]
    else:
        candles = candleLighting(days - 1)
        upto = days - 1

        

        for i in range(upto):
            candles[i] -=1
        return candles

print(candleLighting(3))