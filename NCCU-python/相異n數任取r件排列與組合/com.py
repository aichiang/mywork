# coding: utf-8
from IPython.display import display, HTML, Markdown
from itertools import permutations, combinations
display(Markdown("$$1.計算 n件相異物取r件組合  = \{C_{r}}^{s}\$$"))

s = int(input('輸入相異物個數s ='))
r = int(input('輸入取件個數r ='))
hamm =(combinations(range(1, s+1),r))
ch1 = int(input('只想要結果輸『1』,想看所有排列結果輸『2 』:'))
if ch1 == 1:
    print(f'{s}件相異物取{r}件排列個數為: {len(list(hamm))}')
if ch1 ==2:
    per = []
    for per0 in hamm:
        per1 =''
        for i in range(len(per0)):
            per1 = per1 +str(per0[i])
        per.append(int(per1))
    print(per)
    print(f'{s}件相異物取{r}件排列個數為: {len(list(per))}')
    
