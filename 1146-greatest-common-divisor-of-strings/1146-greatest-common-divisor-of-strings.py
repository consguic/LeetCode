class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        ortak_uzunluk = 0
        a , b = len(str1), len(str2)
        while b:
            a , b = b, a % b
        return str2[0:a]
        