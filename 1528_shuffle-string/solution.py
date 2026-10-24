class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d=""
        for i in range(len(s)):
            for j in range(len(s)):
                if indices[j] == i:
                    d += s[j]
        return d