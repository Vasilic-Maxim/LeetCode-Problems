from typing import List


class Solution:
    """
    m - len(emails)
    n - max(emails, key=len)
    Time: O(m * n)
    Space: O(m * n)
    """

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@", maxsplit=1)
            local = local.split("+", maxsplit=1)[0].replace(".", "")
            unique.add(f"{local}@{domain}")
        return len(unique)
