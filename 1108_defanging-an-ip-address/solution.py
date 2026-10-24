class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret = ""
        for i in address:
            
            if i==".":
                i = "[.]"
            ret += i
        return ret