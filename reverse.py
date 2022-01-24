"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""



list= [3,2,5,7,[4,6,8],[4,6,1,3,2]]
list.reverse()
a = len(list)
for i in range(0,2):
    b = len(list[i])
    if 1!=b:
        list[i].reverse()

print(list)
