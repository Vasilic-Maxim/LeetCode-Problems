from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, license_plate: str, words: List[str]) -> str:
        wanted = Counter(char.lower() for char in license_plate if char.isalpha())
        return min((word for word in words if not wanted - Counter(word)), key=len)
