class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0 
        for i in range(len(flowerbed)):
          if flowerbed[i]==0:
            if (i>0 and flowerbed[i+1]==0):
                continue 
            if (i<len(flowerbed)-1 and flowerbed[i-1]==0):
                continue 
        flowerbed[i]=1 
        count+=1 
        if(count>=n):
            return True 
        else:
            return False
