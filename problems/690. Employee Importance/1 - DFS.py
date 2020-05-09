from typing import List


class Employee:
    def __init__(self, employee_id: int, importance: int, subordinates: List[int]):
        self.id = employee_id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def getImportance(self, employees: List[Employee], employee_id: int) -> int:
        database = {e.id: e for e in employees}
        return self.dfs(database, employee_id)

    def dfs(self, database: dict, employee_id: int) -> int:
        importance = database[employee_id].importance
        for subordinate_id in database[employee_id].subordinates:
            importance += self.dfs(database, subordinate_id)
        return importance
