class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        nbr = n = len(students)
        refus = 0
        while refus < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                nbr -= 1
                refus = 0
            else: 
                student = students.pop(0)
                students.append(student)
                refus += 1
        return nbr 
        
                




        