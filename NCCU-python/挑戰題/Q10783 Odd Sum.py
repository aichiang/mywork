# coding: utf-8
spam = int(input("測試組數："))
s1 = 0
s2 = 0
L = []
for i in range(spam):
    s =(input("輸入範圍:")).split()
    L.append(s)
for P in L:
    s1 =0
    for j in range(int(P[0]),int(P[1])+1):
        if j %2 != 0 :
            s1 += j
    print(f"{P[0]}和{P[1]}之間所有奇數的和:{s1}")
        
            
   
