class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {} # letter . amount
        if len(s) == len(t):
            for i in s:
                if i not in hashmap:
                    hashmap[i] = 1
                else:
                    hashmap[i] = hashmap[i] + 1 #O(n)
            for i in t:
                if i in hashmap:
                    hashmap[i] = hashmap[i] - 1
                else:
                    return False #O(n)
            if all(x==0 for x in hashmap.values()): #O(k)
                return True 
        return False

        #O(n + n + k) = O(2n + k) = O(n)