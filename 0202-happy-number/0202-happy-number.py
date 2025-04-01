class Solution(object):
    def isHappy(self, n):
        seen = set()  # Daha önce gördüğümüz sayıları tutmak için set
        while n != 1 and n not in seen:
            seen.add(n)  # Daha önce gördüğümüz sayıyı ekle
            toplam = 0  # Her döngüde toplamı sıfırlıyoruz
            for i in str(n):
                toplam += int(i) ** 2  # Basamakların karelerini topla
            n = toplam  # n'yi yeni toplamla güncelle
        return n == 1  # Eğer n == 1 ise mutlu sayıdır

        