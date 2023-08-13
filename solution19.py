class Solution:
    def function(self,result, nums, idx):
        if idx == len(nums):
            result.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[i],nums[idx] = nums[idx],nums[i]
            self.function(result, nums, idx + 1)
            nums[i],nums[idx] = nums[idx],nums[i]
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.function(result, nums[:], 0)
        return result
        