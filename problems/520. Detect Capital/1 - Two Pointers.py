class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(len(word) - 1):
            is_curr = 'A' <= word[i] <= 'Z'
            is_next = 'A' <= word[i + 1] <= 'Z'

            if (not is_curr and is_next) or (i and (is_curr and not is_next)):
                return False

        return True
