import re
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return list(filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words))
