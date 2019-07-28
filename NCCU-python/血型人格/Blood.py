# coding: utf-8
import time
print('血型-A、B、O、AB - 你知道你的血型人格特色嗎?')
print('離開請輸入bybe')
Blood = ''
while Blood !='bybe' :       
    Blood = input('輸入血型(A,B,O,AB):')
    if Blood =='A':
        print('在奇怪地方有原則；深思熟慮後才行動；不坦率；會為了別人勉強自己；')
        print('')
        time.sleep(2)
        print('想知道其他血型人格嗎?')
       
    elif Blood =='B':
        print('不擅長沉默；討厭閒著沒事；健忘；不想去察顏觀色')
        print('')
        time.sleep(2)
        print('想知道其他血型人格嗎?')
        
    elif Blood =='AB':
        print('熱血行動派；比起磨蹭更喜歡一股作氣；在奇怪的方面非常頑固；')
        print('')
        time.sleep(2)
        print('想知道其他血型人格嗎?')
        
    elif Blood =='O':
        print('容易小題大作；擅長照顧別人的心情；不會按照計畫行事；')
        print('')
        time.sleep(2)
        print('想知道其他血型人格嗎?')
        
    elif Blood == 'bybe':
        print('下次再連絡')
        
    else:
        print('發現新物種?!') 
        print(' ') 
        print('再給你一次機會!! ') 
