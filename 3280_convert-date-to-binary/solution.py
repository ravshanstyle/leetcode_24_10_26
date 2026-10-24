class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(f"{int(a):b}" for a in date.split("-"))