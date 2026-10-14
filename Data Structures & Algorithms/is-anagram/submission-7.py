class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {} # Caracter . frecuencia
        if len(s) != len(t):
            return False 
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        for c in t:
            if c in hashmap:
                hashmap[c] -= 1
            else:
                return False
        if all(value == 0 for value in hashmap.values()):
            return True
            
        return False