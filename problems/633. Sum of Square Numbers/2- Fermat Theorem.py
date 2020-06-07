class Solution:
    """
    Time: O(n ** .5 * log(n))
    Space: O(1)
    """

    def judgeSquareSum(self, c: int) -> bool:
        factor = 2

        # scan each prime factor
        while factor * factor <= c:
            exponent_of_factor = 0

            # check whether " factor | c " or not
            if c % factor == 0:
                # get the exponent of current factor
                while c % factor == 0:
                    # accumulate the exponenet of prime factor
                    exponent_of_factor += 1
                    # update c
                    c = c // factor
                # Reject factor decomposition in the form: " (4k+3)^q | c ", where q is odd integer
                if factor % 4 == 3 and exponent_of_factor % 2 != 0:
                    return False
            # try next factor
            factor += 1
        # Reject number in the form: c = 4k+3 where k is non-negative integer
        return c % 4 != 3
