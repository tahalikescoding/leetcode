#LEETCODE 1456: Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set("aeiouAEIOU")
        count = 0 
        best = float("-inf")
        l = 0 
        if not s or len(s)<k:
            return 0
        for r in range(len(s)):
            if r-l == k :
                best = max(count,best)
                if s[l] in vowel:
                    count-=1
                l+=1
            if s[r] in vowel:
                count+=1
        return max(best,count)