class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        for char in s:
            ms[char] = ms.get(char, 0) + 1
        for char in t:
            mt[char] = mt.get(char, 0) + 1
        return mt == ms