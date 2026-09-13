class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        fd = []
        for num in nums:
            total = 0
            nod = 0
            for i in range(1,int(num**0.5)+1):
                if num%i==0:
                    total+=i
                    nod+=1
                    if i!=num//i:
                        total+= num//i
                        nod+=1
            if nod==4:
                fd.append(total)
        if not fd:
            return 0
        return sum(fd)