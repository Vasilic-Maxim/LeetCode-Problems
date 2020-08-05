class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    __ANY_CHAR = '.'

    def __init__(self):
        self.__root = Node()

    def addWord(self, word: str) -> None:
        node = self.__root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]

        node.is_word = True

    def search(self, word: str) -> bool:
        return self.__dfs(word, 0, self.__root)

    def __dfs(self, word: str, idx: int, node: Node) -> bool:
        if idx == len(word):
            return node.is_word

        if word[idx] == self.__ANY_CHAR:
            return any(self.__dfs(word, idx + 1, member)
                       for member in node.children.values())
        if word[idx] in node.children:
            return self.__dfs(word, idx + 1, node.children[word[idx]])
        if self.__ANY_CHAR in node.children:
            return self.__dfs(word, idx + 1, node.children[self.__ANY_CHAR])
        return False
