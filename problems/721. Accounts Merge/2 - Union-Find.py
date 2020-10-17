from typing import List


class WeightedUF:
    def __init__(self, n: int):
        self.__ids = list(range(n))
        self.__size = [1] * n
        self.__count = n

    def union(self, p: int, q: int):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:
            return

        if self.__size[parent_p] > self.__size[parent_q]:
            self.__ids[parent_q] = parent_p
            self.__size[parent_p] += self.__size[parent_q]
        else:
            self.__ids[parent_p] = parent_q
            self.__size[parent_q] += self.__size[parent_p]

        self.__count -= 1

    def find(self, p: int) -> int:
        ids = self.__ids
        while ids[p] != p:
            ids[p] = ids[ids[p]]
            p = ids[p]
        return p

    def count(self) -> int:
        return self.__count


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts_ids = {}
        ids = []
        emails_ids = {}
        for i, [_, *account_emails] in enumerate(accounts):
            for email in account_emails:
                if email not in accounts_ids:
                    accounts_ids[email] = i
                    ids.append(email)
                    emails_ids[email] = len(emails_ids)

        # create connections
        n = len(accounts_ids)
        uf = WeightedUF(n)
        for [_, first_email, *account_emails] in accounts:
            for email in account_emails:
                uf.union(emails_ids[first_email], emails_ids[email])

        # group emails
        result = [[] for _ in range(uf.count())]
        roots_id = {}
        for j in range(n):
            parent_id = uf.find(j)
            group_id = roots_id.setdefault(parent_id, len(roots_id))
            result[group_id].append(ids[j])

        # add names
        for k in range(uf.count()):
            result[k].sort()
            account_id = accounts_ids[result[k][0]]
            result[k].insert(0, accounts[account_id][0])

        return result
