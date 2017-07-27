#  Division -
#  Input 1, 2 -> 0.5
#  Input 2, 3 -> 0.(6)
#  Ex. 1/9 -> .(1)
#  Ex. 9/11 -> .(81)
#  Ex. 7/12 -> 0.58(3)
#  Where (x) means x repeating

from decimal import Decimal


def rep_division(x, y):

    """Return x divided by y, and if there are any repeating digits after the decimal, place parentheses around them.

    >>> rep_division(1, 2)
    '0.5'

    >>> rep_division(2, 3)
    '0.(6)'

    >>> rep_division(1, 9)
    '0.(1)'

    >>> rep_division(9, 11)
    '0.(81)'

    >>> rep_division(7, 12)
    '0.58(3)'

    """

    if y == 0:
        return "Undefined"

    elif x % y == 0:
        return x / y

    elif x % y != 0:
        x = Decimal(x)

    ans = str(x / y)

    # no repeating digits in the answer
    if len(set(ans)) == len(ans):
        return ans

    # there are repeating digits in the answer, we need to insert parentheses
    else:
        # before_dec: the part without parentheses, before the decimal
        before_dec = ans[:ans.index('.') + 1]
        tenths_i = len(before_dec)

        # take the set of all the digits after the decimal except for the last one because it may be rounded up to see which digits are unique
        set_digits = set(ans[tenths_i:-1])
        num_uniq_digs = len(set_digits)

        # if there's only 1 unique digit after the decimal, must be repeating
        if num_uniq_digs == 1:
            return before_dec + "(" + set_digits.pop() + ")"

        # all the digits in the set_digits are repeating
        elif ans[tenths_i:tenths_i + num_uniq_digs] == ans[tenths_i + num_uniq_digs:tenths_i + (2 * num_uniq_digs)]:

            # print "\nall the digits in the set_digits are repeating"
            return before_dec + "(" + ans[tenths_i:tenths_i + num_uniq_digs] + ")"

        # not all the digits in the set_digits are repeating, but there are some repeats
        else:
            repeat_nums = ""

            # look at five digits after the decimal

            for i, digit in enumerate(ans[tenths_i:tenths_i + 8]):

                if set_digits:

                    try:
                        set_digits.remove(digit)

                    # We have found a number in which there are some repeating digits, but not in a way that we can abstract with parentheses.
                    except KeyError:
                        return ans

                    removed_from_set = digit

                    # checking if the first number was unique, and it is not - saving so I could put parentheses around it
                    if removed_from_set in ans[tenths_i + i + 1:]:
                        repeat_nums += removed_from_set

                    # this number is unique, and it shouldn't have parentheses around it
                    else:
                        pass

            # print "\nrepeat_nums: ", repeat_nums
            return ans[: ans.index(repeat_nums)] + "(" + repeat_nums + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod()


def test_soln():
    for x in range(1, 15):
        for y in range(15, 0, -1):
            print "\n\nrep_division(%s, %s)" % (x, y)
            print "compare to: ", Decimal(x) / y
            print "rep_division soln: ", rep_division(x, y)
