"""1-Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı 
listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]"""



list= [3,2,5,7,[4,6,8],[4,6,1,3,2]]
list.reverse()
a = len(list)
for i in range(0,2):
    b = len(list[i])
    if 1!=b:
        list[i].reverse()

print(list)
