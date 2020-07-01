from collections import defaultdict, OrderedDict
from typing import List, Dict


class Solution:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self):
        self.board = self.rows = self.cols = None
        self.visited: Dict[tuple, list] = defaultdict(list)
        self.found_words = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # check if one of the inputs is empty
        if not board or not words:
            return []

        # create a trie with words from the input
        dictionary = self.create_dictionary(words)

        # set global variables
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        # self.visited = defaultdict(list)
        # self.found_words = set()

        # search for initial letters of words on board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in dictionary:
                    self.explore(i, j, dictionary)

        return list(self.found_words)

    def create_dictionary(self, words: List[str]) -> dict:
        dictionary = {}
        for word in words:
            node = dictionary
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True
        return dictionary

    def explore(self, i: int, j: int, dictionary: dict, path=None) -> None:
        # be sure that we track our path
        if path is None:
            path = OrderedDict()

        coordinate = (i, j)
        if coordinate in path:
            return

        # check if there is no match at all
        char = self.board[i][j]
        if char not in dictionary:
            return

        path[coordinate] = char
        dictionary = dictionary[char]

        # found the end of the word
        if '#' in dictionary:
            self.found_words.add(''.join(path.values()))
            # return

        # explore adjacent cells
        for di, dj in self.directions:
            ni, nj = i + di, j + dj

            # out of board
            if 0 <= ni < self.rows and 0 <= nj < self.cols:
                self.explore(ni, nj, dictionary, path)

        # retreat
        del path[coordinate]
