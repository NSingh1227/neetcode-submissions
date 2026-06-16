class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = i
        for j in range(len(nums)):
            difference = target - nums[j]
            if(difference in hashmap and hashmap[difference] != j):
                return [j, hashmap[difference]]