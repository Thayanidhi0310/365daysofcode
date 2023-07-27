class Solution:
    def sortVowels(self, s: str) -> str:
        a="aeiouAEIOU"
        x=sorted([i for i in s if i in a])
        i=0
        j=0
        y=""
        while j<len(s):
            if s[j] in a:
                y+=x[i]
                i+=1
            else:
                y+=s[j]
            j+=1
        return y