class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {} # Numero . freuencia
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        sorted_items = sorted(hashmap.items(),key=lambda x: x[1],reverse = True)

        return [x[0] for x in sorted_items[:k]]