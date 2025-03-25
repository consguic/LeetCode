class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        new_word = ""
        while i < max(len(word1),len(word2)):
            new_word += word1[i:i+1] + word2[i:i+1]
            i +=1
        return new_word


    



        