from collections import deque
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
        queue = deque([employee_id])
        total_importance = 0
        while len(queue):
            employee = database[queue.popleft()]
            total_importance += employee.importance
            queue.extend(employee.subordinates)
        return total_importance
