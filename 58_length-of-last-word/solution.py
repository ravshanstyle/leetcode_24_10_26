class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       l= " ".join(
       s.split())
       ga = [i for i in l.split()]
       return len(ga[-1])