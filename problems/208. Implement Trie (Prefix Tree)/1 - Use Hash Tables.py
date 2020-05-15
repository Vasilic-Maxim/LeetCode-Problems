from typing import Any


class Trie:

    def __init__(self):
        self.data: dict[Any] = {"the_end": False}

    def insert(self, word: str) -> None:
        current = self.data
        for char in word:
            current.setdefault(char, {"the_end": False})
            current = current[char]
        current["the_end"] = True

    def search(self, word: str) -> bool:
        current = self.data
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return current["the_end"]

    def startsWith(self, prefix: str) -> bool:
        current = self.data
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True
