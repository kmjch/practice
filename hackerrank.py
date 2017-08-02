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
    # only the tallest candles are blown out
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


def plus_minus(n, arr):
    pos = 0
    neg = 0
    zer = 0
    n = float(n)
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zer += 1
    return str(pos/n) + "\n" + str(neg/n) + "\n" + str(zer/n)


def diagonal_difference(n, matrix):
    left_to_right = [(a, a) for a in range(n)]
    right_to_left = [(a, b) for a, b in zip(range(n - 1, -1, -1), range(n))]
    left_to_right_sum, right_to_left_sum = 0, 0
    for index, row_num in left_to_right:
        left_to_right_sum += matrix[row_num][index]
    for index, row_num in right_to_left:
        right_to_left_sum += matrix[row_num][index]
    return abs(left_to_right_sum - right_to_left_sum)


def staircase(n):
    spaces = n - 1
    string = "#"
    output = ""
    while spaces > 0:  # 1
        print " " * spaces + string  # " #####"
        string += "#"  # "######"
        spaces -= 1  # 0
    return "#" * n


def mini_max_sum(arr):
    arr.sort()
    max_num = sum(arr[1:])
    min_num = sum(arr[:-1])
    return str(min_num) + " " + str(max_num)


def grading_students(grades):
    
