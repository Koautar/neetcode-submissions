"""
LeetCode 1913 - Maximum Product Difference Between Two Pairs

Idée :
- Trier le tableau.
- Les deux plus grands nombres donnent le produit maximum.
- Les deux plus petits nombres donnent le produit minimum.
- Retourner :
    (max1 * max2) - (min1 * min2)

Complexité :
Time : O(n log n)
Space : O(1) ou O(n) selon l'algorithme de tri.
À retenir :
Quand un problème demande les plus grands et les plus petits éléments,
penser d'abord à :
1. Sorting
2. Single-Pass Min/Max Tracking
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]