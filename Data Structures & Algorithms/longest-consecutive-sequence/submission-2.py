class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if i - 1 not in num_set:
                lenght = 1
                while i + 1 in num_set:
                    i += 1
                    lenght += 1
                if lenght > longest:
                    longest = lenght
        return longest
