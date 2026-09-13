from collections import Counter

class Solution:
    def countStudents(
        self, 
        students: List[int], 
        sandwiches: List[int]
    ) -> int:
        student_counter = Counter(students)
        
        for sandwich in sandwiches:
            if student_counter[sandwich] > 0:
                student_counter[sandwich] -= 1
            else:
                print(student_counter)
                return sum(student_counter.values())
        
        return 0

        