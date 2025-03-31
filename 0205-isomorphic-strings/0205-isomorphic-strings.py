class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False  # Farklı uzunluktaysa direkt false

        mapping_s_t = {}  # s -> t eşlemesi
        mapping_t_s = {}  # t -> s eşlemesi

        for char_s, char_t in zip(s, t):
            # Eğer s'deki karakter önceden eşleştirildiyse, ama yanlış bir eşleşme varsa
            if char_s in mapping_s_t and mapping_s_t[char_s] != char_t:
                return False
            if char_t in mapping_t_s and mapping_t_s[char_t] != char_s:
                return False

            # Yeni eşleşme oluştur
            mapping_s_t[char_s] = char_t
            mapping_t_s[char_t] = char_s

        return True
            