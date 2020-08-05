from typing import Dict


class Node:
    def __init__(self):
        self.members: Dict[str:Node] = {}
        self.is_word = False


class WordDictionary:
    __ANY_CHAR = '.'

    def __init__(self):
        self.__root = Node()

    def addWord(self, word: str) -> None:
        dictionary = self.__root
        for char in word:
            if char not in dictionary.members:
                dictionary.members[char] = Node()
            dictionary = dictionary.members[char]

        dictionary.is_word = True

    def search(self, word: str) -> bool:
        stack = [(self.__root, 0)]
        n = len(word)
        while stack:
            node, idx = stack.pop()

            # you reached the end of the word
            if idx == n:
                if node.is_word:
                    return True
                else:
                    continue

            char = word[idx]
            # current character is a special-character,
            # so it can match any character
            if char == self.__ANY_CHAR:
                stack.extend(((child, idx + 1) for child in node.children.values()))

            # a non-special-character that is a member
            elif char in node.children:
                stack.append((node.children[char], idx + 1))

            # last chance to math a character, use a
            # special one
            elif self.__ANY_CHAR in node.children:
                stack.append((node.children[self.__ANY_CHAR], idx + 1))

        # hopeless, surrender...
        else:
            return False


s = WordDictionary()
s.addWord("ran")
s.addWord("rune")
s.addWord("runner")
s.addWord("runs")
s.addWord("add")
s.addWord("adds")
s.addWord("adder")
s.addWord("addee")
print(s.search("r.n"), True)
print(s.search("ru.n.e"), False)
print(s.search("add"), True)
print(s.search("add."), True)
print(s.search("adde."), True)
print(s.search(".an."), False)
print(s.search("...s"), True)
print(s.search("....e."), True)
print(s.search("......."), False)
print(s.search("..n.r"), False)
