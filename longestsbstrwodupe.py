#LEETCODE 3: LONGEST SUBSTRING WITHOUT DUPLICATES

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 1
        if not s:
            return 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l+=1
            w = (r-l)+1
            longest = max(w,longest)
            seen.add(s[r])
            r+=1
        return longest