class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {} # Caracter . Frecuencia
        left = 0
        window = {} # Caracter . Frecuencia
        have = 0
        min_lenght = float("inf")
        for right in range(len(t)):
            if not s or not t:
                return ""
            if t[right] not in need:
                need[t[right]] = 1
            else:
                need[t[right]] += 1
            required = len(need)
        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            if s[right] in need:
                if window[s[right]] == need[s[right]]:
                    have += 1
            while have == required:
                window_lenght = right - left + 1
                if window_lenght < min_lenght:
                    min_lenght = window_lenght
                    start = left
                window[s[left]] -= 1
                if s[left] in need:
                    if window[s[left]] < need[s[left]]:
                        have -= 1
                left +=1
        if min_lenght == float("inf"):
            return ""
        else:
            return s[start : start + min_lenght]
                        
