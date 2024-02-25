class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        for num in set(nums):
            curr_count = nums.count(num)
            if curr_count > len(nums)/2 and curr_count > max_count:
                max_count, res = curr_count, num
                print(res, max_count)
        return res
