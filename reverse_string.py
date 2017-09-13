def reverse_string(string1):
    if len(string1) in [0, 1]:
        return string1
    else:
        # return string1[::-1]
        return "".join([string1[n] for n in range(len(string1) - 1, -1, -1)])
