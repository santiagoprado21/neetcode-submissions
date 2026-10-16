class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #Caracter . frecuencia
        left = 0
        max_length = 0
        max_frequency = 0
        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            max_frequency = max(max_frequency,count[s[right]])
            while right - left + 1 - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length,right-left+1)
        return max_length