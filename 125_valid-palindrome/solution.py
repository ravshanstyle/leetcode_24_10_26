class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(lambda char: char.isalnum(), s.lower()))
        return  clean == clean[::-1]