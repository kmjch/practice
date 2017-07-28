def compete_scores(a0, a1, a2, b0, b1, b2):
    # from HackerRank
    alice = 0
    bob = 0
    for a, b in zip([a0, a1, a2], [b0, b1, b2]):
        if a < b:
            bob += 1
        elif a > b:
            alice += 1
    return alice, bob


def birthdayCakeCandles(n, ar):
    # only the tallest candles are 
    # ar = array of heights of each candle
    return ar.count(max(ar))


def timeConversion(s):
    # 07:05:45PM -> 19:05:45
    if s[-2] == "A":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[:2] == "12":
            return s[:-2]
        return str(int(s[:2]) + 12) + s[2:-2]


def time_conversion(s):
    # 07:05:45PM -> 19:05:45
    if s[-2] == "A":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            pass
    else:
        if s[:2] == "12":
            pass
        else:
            return str(int(s[:2]) + 12) + s[2:-2]
    return s[:-2]
