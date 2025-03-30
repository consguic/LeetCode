class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        kelime  =""
        for i in ransomNote:
            if i in magazine:
                magazine =  magazine.replace(i,"",1)
                kelime +=i
        return kelime == ransomNote

        