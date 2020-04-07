class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        idx = len(s) - 1
        while idx >= 0:
            code = s[idx - 2:idx] if s[idx] == "#" else s[idx]
            result.append(chr(ord('a') + int(code) - 1))
            idx -= 3 if s[idx] == "#" else 1

        result.reverse()
        return "".join(result)
