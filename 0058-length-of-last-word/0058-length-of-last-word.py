class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()  # Başındaki ve sonundaki boşlukları temizle
        words = s.split()  # Kelimelere ayır
        return len(words[-1]) 
                
            
            
            
            
            