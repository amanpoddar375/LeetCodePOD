class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        n = len(potions)
        for spell in spells:
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if spell * potions[mid] >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            pairs.append(n - l)
        return pair

# TC : (nlogm), where n is the length of the spells list and m is the length of the potions list
# SC : O(1)
