class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[-1]:
            for i in range(len(nums)):
                if nums[i] == target or nums[i] > target:
                    return i
        else:
            return len(nums)
            