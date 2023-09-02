#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        taken = False
        students.append(-1) #Represents the end of the queue
        while len(students) > 1:
            if students[0] == -1:
                if not taken:
                    return len(students) - 1 #Remove the end marker
                taken = False
                students.pop(0)
                students.append(-1)    
            elif sandwiches[0] == students[0]:
                taken = True
                students.pop(0)
                sandwiches.pop(0)
            else:
                s = students.pop(0)
                students.append(s)
        return 0

