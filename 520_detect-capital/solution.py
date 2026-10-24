class Solution:
    def detectCapitalUse(self, word: str) -> bool:
         
        if word == word.title() or word == word.lower() or word == word.upper():        
            return True
        else: 
            return False 