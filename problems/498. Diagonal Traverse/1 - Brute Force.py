class Solution:
    """
    Time: O(m*n)
    Space: O(1) - we do not count the 'result' list because it is mentioned in
    requirements. No additional space is used.
    """

    def findDiagonalOrder(self, matrix: list) -> list:
        result = []

        if not matrix or not matrix[0]:
            return result

        for i in range(1, len(matrix) + len(matrix[0])):
            if i % 2:  # odd
                y = min(i, len(matrix)) - 1
                x = i - y - 1

                while y >= 0 and x < len(matrix[0]):
                    result.append(matrix[y][x])
                    x += 1
                    y -= 1
            else:
                x = min(i, len(matrix[0])) - 1
                y = i - x - 1

                while x >= 0 and y < len(matrix):
                    result.append(matrix[y][x])
                    y += 1
                    x -= 1

        return result
