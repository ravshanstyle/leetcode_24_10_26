class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if not (s[i].isdigit()):
                res.append(s[i])
            else:
                res.pop()
        return "".join(res)