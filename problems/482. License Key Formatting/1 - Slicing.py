class Solution:
    def licenseKeyFormatting(self, licence: str, k: int) -> str:
        alphanums = [char.upper() for char in licence if char.isalnum()]
        result = []

        reminder = len(alphanums) % k
        if reminder:
            result.append("".join(alphanums[:reminder]))

        for i in range(reminder, len(alphanums), k):
            result.append("".join(alphanums[i:i + k]))

        return "-".join(result)
