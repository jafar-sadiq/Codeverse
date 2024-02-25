class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_list = nums1[:m]+nums2[:n]
        for index in range(m+n):
            smallest = min(merged_list)
            nums1[index] = smallest
            merged_list.remove(smallest)
