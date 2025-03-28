class Solution(object):
    def romanToInt(self,s):
        roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000, 
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }
        parsed_parts = []
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in roman_dict:
                parsed_parts.append(s[i:i+2])
                i += 2
            else:
                parsed_parts.append(s[i])
                i += 1
        total = sum(roman_dict[part] for part in parsed_parts)  
        return total  





