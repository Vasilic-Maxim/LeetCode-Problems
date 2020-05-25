from typing import List


class Solution:
    def __init__(self):
        self.codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(map(self.transform, words)))

    def transform(self, word: str):
        return "".join([self.codes[ord(char) - ord('a')] for char in word])
