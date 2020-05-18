class Solution:
    """
    n - len(s1)
    m - len(s2)
    Time: O(n + m)
    Space: O(1)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1, counter_s2 = {}, {}

        for char in s1:
            counter_s1[char] = counter_s1.get(char, 0) + 1

        slow = 0
        for fast, char in enumerate(s2):
            if char in counter_s1:
                counter_s2[char] = counter_s2.get(char, 0) + 1

                while counter_s2[char] > counter_s1[char]:
                    counter_s2[s2[slow]] -= 1
                    slow += 1

                if fast - slow + 1 == len(s1):
                    return True
            else:
                counter_s2.clear()
                slow = fast + 1
        return False
