class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if n == 0:
            return True
        for i in range(l):
            if flowerbed[i] == 0:
                l_empty = (i == 0) or (flowerbed[i-1] == 0)
                r_empty = (i == l-1) or (flowerbed[i+1] == 0)
                if r_empty and l_empty:
                    flowerbed[i] = 1
                    n = n-1
                if n <= 0:
                    return True
        return False
