class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0  # Başlangıç
        while i < len(flowerbed):
            # Eğer alan boşsa ve sol ve sağdaki alanlar da boşsa
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1  # Çiçek yerleştir
                n -= 1  # Dikilen çiçek sayısını azalt
                if n <= 0:  # Eğer yeterince çiçek dikildiyse
                    return True
            i += 1  # Eğer çiçek dikilmediyse, bir sonraki alana geç

        return n <= 0  # Yeterince çiçek dikildiyse True, yoksa False
