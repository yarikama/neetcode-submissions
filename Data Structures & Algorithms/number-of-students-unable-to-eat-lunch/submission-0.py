from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        sandwiches_queue = deque(sandwiches)

        min_len = len(students)

        i = 0
        while i < min_len:
            if student_queue[0] == sandwiches_queue[0]:
                student_queue.popleft()
                sandwiches_queue.popleft()
                i = 0
                min_len -= 1
            else:
                student_queue.rotate(-1)
                i += 1

        return min_len