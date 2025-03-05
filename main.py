import numpy as np
import matplotlib.pyplot as plt  #Bu modül, grafikler oluşturmak için kullanılır.
from scipy.optimize import linprog
import matplotlib
matplotlib.use('TkAgg')  # Matplotlib'in grafik arayüzü için TkAgg arka planını kullanmasını sağlar. Bu, grafiklerin düzgün bir şekilde görüntülenmesi için gereklidir.

# Hedef fonksiyonu (maksimize etmek için negatifini alıyoruz)
#linprog fonksiyonu minimizasyon yapar.bu yuzden bız negatıf alırız max degerı bulmak ıcın
c = [-5, -4]  # Kar marjları (Sebze ve Meyve)

# Kısıtlamalar
A = [[2, 1], [1, 2]]  # Kısıtlamaların katsayıları
b = [100, 80]  # Kısıtlamaların sağ tarafları

# Simplex algoritması ile çözüm
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# Sonuçları yazdır
print("Optimal Değerler:")
print("Sebze Miktarı:", res.x[0])
print("Meyve Miktarı:", res.x[1])
print("Maksimum Kar:", -res.fun)
# Grafik için kısıtlamaları çizme
x = np.linspace(0, 50, 200)

# Kısıtlamalar
y1 = (100 - 2 * x)  # 2A + B ≤ 100
y2 = (80 - x) / 2   # A + 2B ≤ 80

plt.figure(figsize=(10, 6))
# Matplotlib kütüphanesinin figure fonksiyonu, grafiğin boyutunu ayarlamak için kullanılır. Burada genişlik 10 inç, yükseklik 6 inç olarak ayarlanmıştır.

# Kısıtlamaları çiz
plt.plot(x, y1, label='2A + B ≤ 100', color='blue')
plt.plot(x, y2, label='A + 2B ≤ 80', color='orange')

# Eksenleri ve sınırları ayarla
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.xlabel('Sebze Miktarı (A)')
plt.ylabel('Meyve Miktarı (B)')

# Optimal çözümü işaretle
plt.plot(res.x[0], res.x[1], 'ro')  # Optimal nokta
plt.text(res.x[0], res.x[1], f'  Optimal Çözüm\n  A: {res.x[0]:.2f}, B: {res.x[1]:.2f}', fontsize=10)

# Grafik başlığı ve legend
plt.title('Doğrusal Programlama Problemi')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.grid()
plt.fill_between(x, 0, np.minimum(y1, y2), where=(y1 >= 0) & (y2 >= 0), color='gray', alpha=0.5)
plt.legend()
plt.show()
