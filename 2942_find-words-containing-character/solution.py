class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [num for num, i in enumerate(words) if x in i]