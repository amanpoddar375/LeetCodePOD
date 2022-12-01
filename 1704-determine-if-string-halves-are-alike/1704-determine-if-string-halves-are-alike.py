class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = set('aeiouAEIOU')
        a = (s[:len(s)//2])
        b = (s[len(s)//2:])
        
        return (sum(i in v for i in a) == sum(i in v for i in b))
        #return (sum(a[i] for i in v) == sum(b[i] for i in v))
        
        #return (sum(i in v for i in s[:len(s)//2]) == sum(i in v for i in s[len(s)//2:]))