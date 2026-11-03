class Solution(object):
    def reverseVowels(self, s):
        vowels=set("aeiouAEIOU")
        char=list(s)
        left=0
        right=len(char)-1
        while left<right:
            if char[left] not in vowels:
                left+=1
            elif char[right] not in vowels:
                right-=1
            else:
                char[left],char[right]=char[right],char[left]
                left+=1
                right-=1
        return "".join(char)
    

        