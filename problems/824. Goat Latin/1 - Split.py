class Solution:
    """
    Time: O(n ** 2)
    Space: O(n ** 2)
    """

    def toGoatLatin(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        def convert(word):
            if word[0] not in vowels:
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(w) + 'a' * (i + 1) for i, w in enumerate(s.split()))
