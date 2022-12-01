class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = set('aeiouAEIOU')
        a = Counter(s[:len(s)//2])
        b = Counter(s[len(s)//2:])
        
        return (sum(a[i] for i in v) == sum(b[i] for i in v))
        
        #return (sum(i in v for i in s[:len(s)//2]) == sum(i in v for i in s[len(s)//2:]))