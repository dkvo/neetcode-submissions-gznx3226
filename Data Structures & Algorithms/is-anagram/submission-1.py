class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for c in s:
            if c not in char_map:
                char_map[c] = 1
            else:
                char_map[c] += 1
        
        for c in t:
            if c not in char_map:
                char_map[c] = 1
            else:
                char_map[c] -= 1
        for c in char_map:
            if char_map[c] != 0:
                return False
        return True