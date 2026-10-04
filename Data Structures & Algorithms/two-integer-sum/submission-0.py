class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val (n) . index 
        for i,n in enumerate (nums):
            goal = target - n
            if goal in hashmap:
                return [hashmap[goal],i]
            hashmap[n] = i