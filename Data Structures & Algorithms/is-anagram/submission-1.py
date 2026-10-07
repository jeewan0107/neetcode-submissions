class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        dedup_s=list(set(s))
        dedup_t=list(set(t))
        td={}
        for i in dedup_s:
            sd[i]=s.count(i)
        for j in dedup_t:
            td[j]=t.count(j)
        if sd==td:
            return True
        else:
            return False