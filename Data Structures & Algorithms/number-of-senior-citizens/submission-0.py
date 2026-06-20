class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_person = 0 
        for age in details :
            if int(age[11:13]) > 60:
                num_person += 1
        return num_person
        