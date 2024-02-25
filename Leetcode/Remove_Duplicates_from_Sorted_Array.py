class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(set(nums))
        dup_nums = nums[:]
        for idx in range(len(dup_nums)-1):
            if dup_nums[idx] == dup_nums[idx+1]:
                # print(f"popping {idx}")
                nums.remove(dup_nums[idx])
        # print(nums)
        return k
