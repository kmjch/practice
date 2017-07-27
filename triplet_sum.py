def tripletSum(x, a):

    """

    Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real interview.

    You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three elements for which the sum is exactly x.

    >>> tripletSum(15, [14, 1, 2, 3, 8, 15, 3])
    False

    >>> tripletSum(8, [1, 1, 2, 5, 3])
    True

    >>> tripletSum(182, [589, 343, 609, 61, 222, 759, 955, 889, 147, 691, 950, 844, 431, 621, 749, 68, 537, 784, 36, 227, 186, 39, 854, 630, 225, 749, 924, 360, 258, 767, 945, 956, 319, 727, 412, 26, 356, 2, 550, 497, 585, 516, 965, 343, 76, 914, 143, 197, 949, 73])
    False

    """

    if x == 0 or len(a) == 0:
        return False

    smaller_nums = [num for num in a if num < x - 1]

    if len(smaller_nums) < 3:
        return False

    if len(smaller_nums) == 3:
        return sum(smaller_nums) == x

    for i, n in enumerate(smaller_nums):
        for m in smaller_nums[i + 1:-1]:
            if x - n - m in smaller_nums:
                return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
