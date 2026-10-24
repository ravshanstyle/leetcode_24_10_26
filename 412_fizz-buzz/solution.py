class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1,n+1):
            lst.append(str(i))
            if i % 5 == 0 and i % 3 == 0:
                lst[-1] = "FizzBuzz"
            elif i % 3 == 0:
                lst[-1] = "Fizz"
                
            elif i % 5 == 0:
                lst[-1] = "Buzz"
                
        return lst