#1~49 六個號碼的亂數+一個特別號
#1.完成後使用git add
#2.使用git commit -m "完成大樂透號碼預測"
#3.改成函式
#4.一次產生5組
import random  

def get_lotto(count):
    n = []
    for i in range(count):
        x = random.randint(1, 49)
        n.append(x)
    return n 

for i in range(10):
    print(get_lotto(6))




