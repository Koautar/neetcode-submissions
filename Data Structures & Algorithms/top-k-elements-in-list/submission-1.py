from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = []
        # return a liste of tuple 
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # add juste the firdt element of every tuple for our case is the key 
        for key, value in sorted_items[:k]:
            top_k.append(key)
        return top_k

        