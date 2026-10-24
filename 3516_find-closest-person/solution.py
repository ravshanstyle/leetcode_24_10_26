class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
    #   2 7 4
        a1 = abs(x-z)
        b1 = abs(z-y)
        return 1 if a1<b1 else 2 if a1>b1 else 0