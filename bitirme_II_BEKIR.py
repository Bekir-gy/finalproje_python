# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:57:51 2021

@author: Lenovo
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
print("GRAFA GÖRE CONFLICT/ÇAKIŞIM MATRİS")
conflictMat= np.array( [ [1,1,0,0,0,0,0],
                        [0,0,1,1,0,0,0],
                        [0,1,1,0,1,0,0],
                        [1,0,0,0,1,1,0],
                        [0,0,0,0,0,1,1],
                        [0,0,0,1,0,0,1] ])

print(conflictMat)                   
print(conflictMat.shape)
confsat=conflictMat.shape[0]
confsut=conflictMat.shape[1]
print("çakışım matrisi satir sayısi: %d  çakışım matrisi sütun sayisi: %d" %(confsat,confsut))

print("-------------------------------")
print("---------BİTİŞİKLİK DÜĞÜMDEN DÜĞÜME----------------------")
adjm=(np.dot(conflictMat, conflictMat.T)>0).astype(int)
np.fill_diagonal(adjm,0)
print(adjm)
print(adjm.shape)

print("-------------KESMEE------------------")

K_Mat=np.array([ [0,0,0,1,0,0,1],
                 [0,0,0,0,0,1,1],      
                 [1,1,0,0,0,0,0],
                 [0,0,1,0,0,0,1],
                 [1,0,0,0,1,0,1] ])

print(K_Mat)                   
print(K_Mat.shape)

print("--------------kesme transpose-----------------")

K_Transpose=K_Mat.transpose()
print(K_Transpose)
print(K_Transpose.shape)

"""
işlemler
B*K^T
"""
print("-------------------------------")
print("------------b*k^T çarpım-------------------")
print("-------------------------------")
BKt_carp=(np.dot(conflictMat,K_Transpose))

print(BKt_carp)
print(BKt_carp.shape)


print("-------------------------------")
print("------------b*k^T çarpım sonucu satır toplamı-------------------")
print("-------------------------------")

satir1=BKt_carp.shape[0]
print("satır sayisi çıktısı",satir1)
sutun1=BKt_carp.shape[1]
print("sutun sayisi çıktısı",sutun1)
Mat_satirtoplam1=BKt_carp.sum(axis=1)
print("b*k^t matrisinin satirların toplamı:---> ",Mat_satirtoplam1)

print(" ")
print("------------düğüm derecesi matrisinin  satır toplamı bitişiklik üzerinden  -------------------")
print(" ")
Mat_satirtoplam2=adjm.sum(axis=1)
print("düğüm derecesi matrisinin d(vi) satır toplamı---> ",Mat_satirtoplam2)


print('''
      ------------------------------------
      BXK^T+d(v) sonucu
      
      ''')
      
      
graftop=np.add(Mat_satirtoplam1, Mat_satirtoplam2) 
satirgraf=graftop.shape[0]
print(graftop)   
print("satir sayisi", satirgraf)
print('''
      
      bağlantı derecesi yüksek düğüm
      
      ''')
bder=graftop[0]
bdugum=0

for i in range(satirgraf):
    if bder<graftop[i]:
        bder=graftop[i]
        bdugum=i
        
print("bağlantı derecesi yüksek düğüm --->",bdugum,
      "  dizi indisi olarak saymazsak bağlantı derecesi en yüksek düğüm---->", 
      bdugum+1)

print('''
      
      ilişkiler
      ÖNEMLİ NOT: Burada çizdirdiğim grafla ve normal kağıt üstü v.b bileşenlerle
      hesaplamalardaki gibi olması ve kafa karışıklığı olmaması ve anlaşılması için
      aiağıdaki döngülerde indisleri +1 olarak arttırdım.
      yukarıda bağlantı derecesi yüksek düğümü yazdırırkende belirttiğim gibi
      hem kod ortamında çıkan indis karşılığı(0 dan başlayarak) ve 
      normal kullanımda ve grafta karşılığı (1 den saymaya başlayarak).
      
      
      ''')

for sut in range(confsut):
    if conflictMat[bdugum][sut]==1:
        print("%d.satir da 1 olan sütunlar= %d" %(bdugum+1,sut+1))
        conflictMat[bdugum][sut]=0 #burası baskın kümeyi sfırlar
        
        for sat in range(confsat) :
            if sat == bdugum: continue
            else:
             if conflictMat[sat][sut]==1:
                print("anahtar düğümle ilişkisi olan düğümler ",sat+1 )
                print("%d ----> %d " %(bdugum+1,sat+1) )
                conflictMat[sat][sut]=0 #burası bağlantılı ayrıtı sıfırlar
    else:
        sut+=1  
        
print(".        baskın küme: %d" %(bdugum+1))
print("-       ------------------------" )  
       
print('''
      
      
          conflict çakışım matris sonraki hali
          (anahtar düğüm ve ilişkili oldukları ayrıtın bağı kesilmesi)
      
      ''')
print(conflictMat)
print('''
      
      
      
      
      
      ----------------------------
      
      
      
      
      
      
      ''')


#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------

print("------------b*k^T çarpım-------------------")
print("-------------------------------")
BKt_carp=(np.dot(conflictMat,K_Transpose))
print(BKt_carp)
print(BKt_carp.shape) 



print("-------------------------------")
print("------------b*k^T çarpım sonucu satır toplamı-------------------")
print("-------------------------------")

satir1=BKt_carp.shape[0]
print("satır sayisi çıktısı",satir1)
sutun1=BKt_carp.shape[1]
print("sutun sayisi çıktısı",sutun1)
Mat_satirtoplam1=BKt_carp.sum(axis=1)
print("b*k^t matrisinin satirların toplamı:---> ",Mat_satirtoplam1)

print('''
      ------------------------------------
      BXK^T+d(v) sonucu
      
      ''')
      
      
graftop=np.add(Mat_satirtoplam1, Mat_satirtoplam2) 
satirgraf=graftop.shape[0]
print(graftop)   
print("satir sayisi", satirgraf)
print('''
      
      bağlantı derecesi yüksek düğüm
      
      ''')
bder=graftop[0]
bdugum=0


for i in range(satirgraf):
    if bder<graftop[i]:
        bder=graftop[i]
        bdugum=i
        
print("bağlantı derecesi yüksek düğüm --->",bdugum,
      "  dizi indisi olarak saymazsak bağlantı derecesi en yüksek düğüm---->", 
      bdugum+1)

print('''
      
      ilişkiler
      ÖNEMLİ NOT: Burada çizdirdiğim grafla ve normal kağıt üstü v.b bileşenlerle
      hesaplamalardaki gibi olması ve kafa karışıklığı olmaması ve anlaşılması için
      aiağıdaki döngülerde indisleri +1 olarak arttırdım.
      yukarıda bağlantı derecesi yüksek düğümü yazdırırkende belirttiğim gibi
      hem kod ortamında çıkan indis karşılığı(0 dan başlayarak) ve 
      normal kullanımda ve grafta karşılığı (1 den saymaya başlayarak).
      
      
      ''')

for sut in range(confsut):
    if conflictMat[bdugum][sut]==1:
        print("%d.satir da 1 olan sütunlar= %d" %(bdugum+1,sut+1))
        conflictMat[bdugum][sut]=0 #burası baskın kümeyi sfırlar
        
        for sat in range(confsat) :
            if sat == bdugum: continue
            else:
             if conflictMat[sat][sut]==1:
                print("anahtar düğümle ilişkisi olan düğümler ",sat+1 )
                print("%d ----> %d " %(bdugum+1,sat+1) )
                conflictMat[sat][sut]=0 #burası bağlantılı ayrıtı sıfırlar
    else:
        sut+=1  
        
print(".        baskın küme: %d" %(bdugum+1))
print("-       ------------------------" )  


print('''
      
      
          conflict / çakışım matris sonraki hali
          (anahtar düğüm ve ilişkili oldukları ayrıtın bağı kesilmesi)
      
      ''')
print(conflictMat)










#YAPILANI GRAF OLARAK GÖSTERİM


G = nx.Graph() 
E = [('3', '4', 5), ('3', '1', 2), ('3', '2', 3), ('1', '4', 1), ('4', '5', 6), ('2', '6', 4), ('6', '5', 7)]
G.add_weighted_edges_from(E)

pos=nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, font_weight='bold')

edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)

plt.show()


