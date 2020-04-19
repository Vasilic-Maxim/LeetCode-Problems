from typing import List


class Solution:
    def shortestToChar(self, string: str, target: str) -> List[int]:
        result = list(string)
        counter = float('inf')
        for pointer, char in enumerate(result):
            result[pointer] = counter

            if char == target:
                counter = counter_back = 0

                while pointer >= 0 and result[pointer] > counter_back:
                    result[pointer] = counter_back
                    counter_back += 1
                    pointer -= 1

            counter += 1
        return result
