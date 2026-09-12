
class Soltuion:
    def isarmstrong(self , x:int)->bool:
        num = x
        result = 0
        digit = len(str(x))
        while num>0:
            num , last = divmod(num,10)
            result += last**digit
        return result==x

test = Soltuion()

print(test.isarmstrong(1634))
            