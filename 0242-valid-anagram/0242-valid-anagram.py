class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        list_s = {}
        list_t = {}
        for i in s:
            if i not in list_s:
                list_s[i] = 0
            else:
                list_s[i] +=1
        for i in t:
            if i not in list_t:
                list_t[i] = 0
            else:
                list_t[i] +=1
        return list_s == list_t 
            