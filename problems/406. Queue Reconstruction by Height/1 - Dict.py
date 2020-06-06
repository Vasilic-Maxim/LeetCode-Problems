from typing import List


class Solution:
    """
    Time: O(n * log(n))
    Space: O(~3n) => O(n)
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_dict = {}
        for person in people:
            people_dict.setdefault(person[0], [])
            people_dict[person[0]].append(person[1])

        result = []
        for h in sorted(people_dict.keys(), reverse=True):
            for k in sorted(people_dict[h]):
                result.insert(k, [h, k])

        return result
