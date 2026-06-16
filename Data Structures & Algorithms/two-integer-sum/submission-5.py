class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            difference = target - val
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[val] = i