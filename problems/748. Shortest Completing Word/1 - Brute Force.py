from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, license_plate: str, words: List[str]) -> str:
        counter = Counter(char.lower() for char in license_plate if char.isalpha())
        max_common, result = 0, None
        for word in words:
            common = sum((counter & Counter(word)).values())
            if common > max_common:
                result = word
                max_common = common
            elif common == max_common:
                if result is not None and len(result) > len(word):
                    result = word
        return result
