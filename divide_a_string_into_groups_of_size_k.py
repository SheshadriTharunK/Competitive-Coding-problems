class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        i=0
        l=[]
        o=''
        while(i<len(s)):
                o+=s[i:i+k]
                if len(o)==k:
                    l.append(o)
                    i+=k
                else:
                
                    o+=fill*(k-len(o))
                    l.append(o)
                    i+=k
                o=''
        return l