class Solution:

    def encode(self, strs: List[str]) -> str:
        sres = []
        for s in strs:
            sres.append(str(len(s)))
            sres.append('#')
            sres.append(s)
        return "".join(sres)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            j = i
            while s[j] != '#':
                j+=1
            nextlen = int(s[i:j])
            i=j+1   # jump over '#'
            j=i+nextlen
            res.append(s[i:j])
            i=j

        return res
