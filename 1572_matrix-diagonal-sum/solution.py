class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        mid = n//2
        for i in range(n):
            ans += mat[i][i]

            ans += mat[n-1-i][i]
        if n % 2 != 0:
            ans -= mat[mid][mid]
        return ans
