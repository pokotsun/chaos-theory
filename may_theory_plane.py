import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

# xを変更して表示してみる
def logistic(a=4, initial_value=0.5):
    rtn = [initial_value]
    # 漸化式の結果を5000回分リストにセット
    for i in range(5000):
        rtn.append(a * rtn[-1] * (1 - rtn[-1]))
    return rtn 

# logistic関数が起こす一点集中の性質を表すリストを返す
def _logistic_pattern(a=4, initial_value=0.4, iterate_num=100):
    rtn = []
    logistic = lambda x: a * x * (1 - x)
    x1 = x2 = initial_value 
    y1 = y2 = 0.0
    for i in range(iterate_num):
        if not(i % 2): # 偶数だった時 -> y方向にlogistic関数に寄る時
            x1 = x2
            y1 = y2
            y2 = logistic(x2)
            
        else: # 奇数だった時 -> x方向に y = x に寄る時
            x1 = x2
            x2 = y2
            y1 = y2
        rtn.append({"x_points": [x1, x2], "y_points": [y1, y2]})

    return rtn


# Main関数
def main():
    fig = plt.figure()

    #a = 4
    #initial_value = 0.4
    print("y = ax(1-x)のaの値は?")
    try: 
        a = float(input())
    except ValueError:
        a = 4

    print("xの初期値は?")
    try:
        initial_value = float(input())
    except ValueError:
       initial_value = 0.4 

    print(f"a = {a}, Xの初期値は{initial_value}になりました。")
    result_list = logistic(a=a, initial_value=initial_value)
    x_list = result_list[:-1]
    y_list = result_list[1:]

    # ロジスティック関数を描画
    p1, = plt.plot(x_list, y_list, "r.", markersize=0.3)
    p2, = plt.plot([0, 2], [0, 2], "g-", lw=2)
    plt.legend([p1, p2], ["logistic", "y = x"])
    
    plt.xlim([0, 2.0])
    plt.ylim([0, 2.0])
    plt.title(f"a = {a}, initial value={initial_value}")


    plt.show()

if __name__ == "__main__":
        main()
