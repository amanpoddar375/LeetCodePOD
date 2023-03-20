class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed.append(0)
        count = 0
        for i in range(len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
                if count == n:
                    return True
        return False

# TC : O(n), where n is the length of the flowerbed list, because we iterate over the list once.

# SC : O(1), as we use only constant amount of extra space. 
