class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Kapama parantezleri ile açma parantezlerini eşleştiren sözlük
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping.values():  # Açılış parantezi ise
                stack.append(char)
            elif char in mapping:  # Kapanış parantezi ise
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                # Geçersiz karakter durumu, gerekirse
                return False
        return not stack
