class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True]*(right+1)
        if right == 0 or left == 0 or right == 1 or left == 1 or left>right:
            return [-1,-1]
        prime[0] = prime[1] = False
        for i in range(1,right+1):
            if prime[i]:
                for j in range(i+i,right+1,i):
                    prime[j]=False
        primes = [num for num in range(1,right+1) if prime[num] and num>=left]
        if len(primes)<2:
            return [-1,-1]
        result = [primes[0] , primes[1]]
        min_dif = primes[1]-primes[0]
        for i in range(1,len(primes)-1):
            dif = primes[i+1]-primes[i]
            if dif<min_dif:
                min_dif = dif
                result = [primes[i] , primes[i+1]]
        return result


test = Solution()
print(test.closestPrimes(1,1000000))