class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permute(res, nums):
            if len(nums) == 0:
                ans.append(res)    
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                permute(res+[nums[i]], nums[:i]+nums[i+1:])
        nums.sort()
        permute([], nums)
        return ans