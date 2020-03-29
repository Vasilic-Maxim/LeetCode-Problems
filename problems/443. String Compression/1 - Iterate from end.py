class Solution:
    def compress(self, chars: list) -> int:
        if len(chars) <= 1:
            return len(chars)

        counter = 0
        pointer = len(chars) - 1
        while pointer:
            counter += 1

            if chars[pointer] == chars[pointer - 1]:
                chars.pop(pointer)

                if not pointer - 1 and counter >= 1:
                    chars[pointer:pointer] = list(str(counter + 1))
            else:
                if counter > 1:
                    chars[pointer + 1:pointer + 1] = list(str(counter))

                counter = 0

            pointer -= 1

        return len(chars)
