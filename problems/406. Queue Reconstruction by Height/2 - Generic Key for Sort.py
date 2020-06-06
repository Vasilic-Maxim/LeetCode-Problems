from typing import List


class Solution:
    """
    Data used:
    1100 - there can be maximum 1100 people in a queue

    This solution is better than the first one because
    it uses less space due to not using the dictionary

    Time: O(n * log(n))
    Space: O(~2n) => O(n)
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=self.generate_key, reverse=True)
        result = []
        for person in people:
            result.insert(person[1], person)
        return result

    def generate_key(self, person: List[int]) -> float:
        """ Returns a generic key to sort the list properly """
        h, k = person
        return float(f"{h}.{1100 - k}")
