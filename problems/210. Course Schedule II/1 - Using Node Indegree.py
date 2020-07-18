from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a relation between courses
        courses = defaultdict(set)
        dependencies = defaultdict(set)
        for course, dependency in prerequisites:
            courses[course].add(dependency)
            dependencies[dependency].add(course)

        # find independent courses what you can take right now
        opened_courses = deque(num for num in range(num_courses) if not courses[num])

        # take independent courses, free other courses
        taken_courses = []
        while opened_courses:
            course = opened_courses.pop()
            taken_courses.append(course)
            for dependency in dependencies[course]:
                courses[dependency].remove(course)
                if not courses[dependency]:
                    opened_courses.appendleft(dependency)

        return taken_courses if len(taken_courses) == num_courses else []
