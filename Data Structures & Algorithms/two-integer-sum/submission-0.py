class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in x:
                return [x[a],i]
            x[nums[i]] = i