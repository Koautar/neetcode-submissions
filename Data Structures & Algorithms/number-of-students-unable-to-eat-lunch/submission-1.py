class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        nbr = n = len(students)
        refus = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while refus < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                nbr -= 1
                refus = 0
            else: 
                student = students.popleft()
                students.append(student)
                refus += 1
        return nbr 
        
                




        