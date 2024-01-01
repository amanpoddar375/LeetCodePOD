class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        content_children = 0
        g_index, s_index = 0, 0
        
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                content_children += 1
                g_index += 1
            s_index += 1
        
        return content_children
