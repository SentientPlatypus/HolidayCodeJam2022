def candleLighting(days:int) -> list[int]:
    if days == 1:
        return [10, 10, 10, 10, 10, 10, 10, 10, 10]
    else:
        candles = candleLighting(days - 1)

        ## if the day is greater than 10, iterate up to index 9
        upto = min(days - 1, 9)

        ##iterate up to the correct index
        for i in range(upto):

            ##If candles[i] - 1 is less than 0, make it 0
            candles[i] = max(candles[i] - 1, 0)

        return candles

print(candleLighting(15))