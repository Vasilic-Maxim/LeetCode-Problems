from typing import List


class Solution:
    """
    This solution is better than the first one because
    it uses less space due to not using the dictionary

    Time: O(n * log(n))
    Space: O(~2n) => O(n)
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        result = []
        for person in people:
            result.insert(person[1], person)
        return result
