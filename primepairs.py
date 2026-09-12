#LEETCODE 2761: PRIME PAIRS 

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        pairs = []
        isprime = [True]*n
        if n == 0 or n == 1:
            return []
        isprime[0] = isprime[1] = False
        for i in range(1,int(n**0.5)+1):
            if isprime[i]:
                for j in range(i+i , n , i):
                    isprime[j] = False
        for num in range(1,n):
            if isprime[num]:
                difference = n-num
                if isprime[difference] and num<=difference:
                    pairs.append([num,difference])
        return pairs

test = Solution()
print(test.findPrimePairs(10))