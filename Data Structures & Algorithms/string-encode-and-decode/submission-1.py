class Solution:

    def encode(self, strs: List[str]) -> str:
        sres = []
        for s in strs:
            sres.append(str(len(s)))
            sres.append('#')
            sres.append(s)
        return "".join(sres)

    def decode(self, s: str) -> List[str]:
        nextlen = ""
        nextword = ""
        res = []
        i = 0

        while i<len(s):
            c=s[i]
            print(c)
            if c!='#':
                nextlen+=c
            else:
                slen = int(nextlen)
                for _ in range(slen):
                    i+=1
                    c=s[i]
                    nextword+=c
                res.append(nextword)
                nextlen=""
                nextword=""
            i+=1
        return res
