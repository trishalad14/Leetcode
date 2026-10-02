class Solution(object):
    def heightChecker(self, heights):
        n=len(heights)
        original=heights[:]
        expected=[]
        for i in range(n-1):
            swapped=True
            for j in range(n-1-i):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    swapped=True
            if swapped==False:
                break
        expected=heights[:]
        count=0
        for k in range(n):
            if expected[k]==original[k]:
                count==0
            else:
                count+=1
        return count
    




        