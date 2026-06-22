from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greatest = []

        for i in range(len(nums1)):
            found = False

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:

                    for gre in range(j + 1, len(nums2)):
                        if nums2[gre] > nums2[j]:
                            greatest.append(nums2[gre])
                            found = True
                            break

                    if not found:
                        greatest.append(-1)

                    break

        return greatest