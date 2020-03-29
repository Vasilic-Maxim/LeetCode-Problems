class Solution:
    """
    Very nice solution which I found recently on forum. The idea is that we
    always have some space between current and new character. Space between
    the current character and the next different character becomes bigger
    with the growth of adjacent duplicates number.

    For example:
    [a]         -> [a]
    [a, a]      -> [a, 2]
    [a, a, a]   -> [a, 3, ...]

    When talking about time you would mention to your interviewer that inner
    loop will be called maximum n/2 times and it will take O(1) time for each
    iteration.

    Time: O(n)
    Space: O(1)
    """

    def compress(self, chars: list) -> int:
        if not chars or len(chars) == 0:
            return 0

        # currentIdx sticks with the character who's occurrences we're counting.
        # insertIdx is the next point of insertion in the compressed string.
        # scanIdx is how far we have looked for occurrences.
        current_idx, insert_idx, scan_idx = 0, 0, 1
        while scan_idx <= len(chars):
            if scan_idx == len(chars) or chars[scan_idx] != chars[current_idx]:
                chars[insert_idx] = chars[current_idx]
                insert_idx += 1
                occurrence = scan_idx - current_idx
                if occurrence > 1:
                    # This for loop will repeat maximum O(n/2) times in case then
                    # initial list contains pairs of chars adjacently arranged
                    for digit in str(occurrence):
                        chars[insert_idx] = digit
                        insert_idx += 1
                current_idx = scan_idx
            scan_idx += 1

        # If we want to modify list such as there will not be any additional
        # values we can use 'insertIdx' as end of slicing range.
        # return chars[:insertIdx]

        return insert_idx
