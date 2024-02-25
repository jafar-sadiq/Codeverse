class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_org_len = len(nums)
        k = nums_org_len - nums.count(val)
        # nums = [num for num in nums if num != val] + ["_"] * (nums_org_len - k)
        for num in nums[:]:
            if num == val:
                nums.remove(num)
        nums.extend(["_"] * (nums_org_len - k))
        # print(nums)
        return k
