class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_t = {}
        char_s = {}

        for c in s:
            char_s[c] = char_s.get(c, 0) + 1
        for c in t:
            char_t[c] = char_t.get(c, 0) + 1

        return char_s == char_t