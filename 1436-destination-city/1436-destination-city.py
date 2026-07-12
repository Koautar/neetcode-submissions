class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = set()
        for depart , arrive in paths:
            departures.add(depart)
        for depart , arrive in paths: 
            if arrive not in departures:
                return arrive 
        