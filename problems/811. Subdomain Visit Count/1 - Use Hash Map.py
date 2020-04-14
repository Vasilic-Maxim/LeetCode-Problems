from collections import defaultdict
from typing import List


class Solution:
    """
    n - len(cp_domains)
    m - len(max(cp_domains)) - max string len

    Time: O(n * m)
    Space: O(n) - each domain will contain 2-3 dots
    """

    def subdomainVisits(self, cp_domains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for cp_domain in cp_domains:
            visits, domain = cp_domain.split()
            visits = int(visits)
            domains[domain] += visits

            for i, char in enumerate(domain):
                if char == ".":
                    domains[domain[i + 1:]] += visits

        return [f"{visits} {domain_name}" for domain_name, visits in domains.items()]
