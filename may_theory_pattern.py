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

# アニメーション描画関数
def _update_plot(i, logistic_points):
    x_points = logistic_points[i]["x_points"]
    y_points = logistic_points[i]["y_points"]

    plt.plot(x_points, y_points, 'r-', lw=1)
    #plt.title(f" Number Of Intersections ({x1}, {y1}) to ({x2}, {y2})")
    plt.xlim([0, 1.5])
    plt.ylim([0, 1.5])
     

# Main関数
def main():
    fig = plt.figure()

    #a = 4
    #initial_value = 0.4
    print("y = ax(1-x)のaの値は?")
    a = float(input())
    print("xの初期値は?")
    initial_value = float(input())
    #a = sys.argv[1] or 4
    #initial_value = sys.argv[2] or 0.4
    result_list = logistic(a=a, initial_value=initial_value)
    x_list = result_list[:-1]
    y_list = result_list[1:]

    # ロジスティック関数を描画
    plt.plot(x_list, y_list, "r.", markersize=0.3)
    plt.plot([0, 2], [0, 2], "g-", lw=2)
    plt.title(f"a = {a}, initial value={initial_value}")

    logistic_points = _logistic_pattern(a=a, initial_value=initial_value, iterate_num=200)

    ani = animation.FuncAnimation(fig, _update_plot, fargs= (logistic_points,),
        interval = 500, frames=len(logistic_points))
    ani.save(f"logistic_period_a{a}_initvalue{initial_value}.gif", writer="imagemagick")
    #plt.show()

if __name__ == "__main__":
        main()
