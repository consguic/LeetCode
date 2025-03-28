class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        sayi = 0
        i = 0

        while i < len(s):  # Manuel olarak index artırıyoruz
            if i < len(s) - 1 and s[i] == "I" and s[i+1] in ["V", "X"]:
                sayi += 4 if s[i+1] == "V" else 9
                i += 2  # 2 harf işlediğimiz için i'yi 2 artır
            elif i < len(s) - 1 and s[i] == "X" and s[i+1] in ["L", "C"]:
                sayi += 40 if s[i+1] == "L" else 90
                i += 2
            elif i < len(s) - 1 and s[i] == "C" and s[i+1] in ["D", "M"]:
                sayi += 400 if s[i+1] == "D" else 900
                i += 2
            else:
                sayi += roman_dict[s[i]]
                i += 1  # Tek harf işlediysek sadece 1 artır

        return sayi

