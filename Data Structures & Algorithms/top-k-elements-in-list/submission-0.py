from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = []
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for key, value in sorted_items[:k]:
            top_k.append(key)
        return top_k

        