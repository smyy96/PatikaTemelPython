"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""


flatten = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste = []

def cevir(flatten):
    for i in flatten:
        if type(i) == list: 
            cevir(i)
        else: 
            liste.append(i)
    return liste

