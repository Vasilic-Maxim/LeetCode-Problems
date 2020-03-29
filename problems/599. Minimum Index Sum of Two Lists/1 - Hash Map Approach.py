class Solution:
    """
    n = len(list1)
    m = len(list2)
    Time: O(n + m)
    Space: O(n + min(n, m))

    NOTE: min(n, m) is used for 'response' list. Let's assume that:
    list1 = [0,1,2,3,4]
    list2 = [4,3,2,1,0]

    In this case result = [1,2,3,4,5] because the minimum sum of indices will be 4 and
    this sum matches all the pairs from bath lists.
    """

    def findRestaurant(self, list1: list, list2: list) -> list:
        counted = {name: idx for idx, name in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for i, name in enumerate(list2):
            if name in counted:
                if counted[name] + i < min_sum:
                    result = [name]
                    min_sum = counted[name] + i
                elif counted[name] + i == min_sum:
                    result.append(name)

        return result
