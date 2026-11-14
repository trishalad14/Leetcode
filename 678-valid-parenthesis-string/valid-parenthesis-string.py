class Solution(object):
    def checkValidString(self, s):
        open_st=[]
        star=[]
        for i,ch in enumerate(s):
            if ch=='(':
                open_st.append(i)
            elif ch=='*':
                star.append(i)
            else:
                if open_st:
                    open_st.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while open_st and star:
            if open_st[-1]>star[-1]:
                return False
            open_st.pop()
            star.pop()
        return not open_st
            