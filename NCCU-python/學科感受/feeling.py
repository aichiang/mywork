# coding: utf-8
from  random import randint, choices, sample
sub ='''國文
英文
數學
化學
物理
音樂
歷史
地理
生物
童軍
地科
電腦
選修
不討喜
老師
重補修
補考
謝謝再聯絡
學生
一般人
打斷重練
腦殘
空白
喜歡
沉迷
沉醉
著魔
厭世'''
def feeling():
    D=sub.split('\n')
    n = randint(4,5)
    for i in range(n):
        m = randint(5,11)
        w = sample(D,m)
        print('')
        print(' '.join(w))
feeling()
