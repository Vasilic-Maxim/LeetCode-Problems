from typing import List


class Solution:
    """
    n - len(form)
    m - len(str(num))

    Time: O(max(n, m))
    Space: O(max(n, m))
    """

    def addToArrayForm(self, form: List[int], num: int) -> List[int]:
        for i in range(len(form) - 1, -1, -1):
            num, form[i] = divmod(form[i] + num, 10)

            if not num:
                break

        return [int(x) for x in str(num)] + form if num else form
