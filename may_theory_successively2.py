import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# xを変更して表示してみる
def logistic(a=4, initial_value=0.5):
    x = [initial_value]
    # 漸化式の結果を500回分リストにセット
    for i in range(100):
        x.append(a * x[-1] * (1 - x[-1]))
    return x

def _update_plot(i, x_list, y_list):

    x1 = x2 = y1 = y2 = 0.0
    if i % 4 == 0: # i = 偶数の時 -> ロジスティック関数にxで寄る時
        if i == 0: # 最初の時
            x1 = x2 = x_list[i]
            y1 = 0.0
            y2 = y_list[i] 
        else: 
            x1 = y1 = x2 = x_list[i - 1]
            y2 = y_list[i - 1]
    elif i % 4 == 1:
        x1 = x_list[i - 1]
        x2 = y1 = y2 = x_list[i]
    elif i %4 == 2:
        x1 = y1 = x2 = x_list[i - 1]
        y2 = y_list[i - 1]
    else:
        x1 = x_list[i - 2]
        x2 = y1 = y2 = x_list[i - 1]

    #else: # i = 奇数の時 -> y = xの関数にyで寄る時
    #    x1 = x_list[i - 2]
    #    x2 = y1 = y2 = x_list[i - 1]

    plt.plot([x1, x2], [y1, y2], 'r-', lw=1)
    plt.title(f" Number Of Intersections ({x1}, {y1}) to ({x2}, {y2})")
    plt.xlim([0, 1.5])
    plt.ylim([0, 1.5])
     

# Main関数
def main():
    fig = plt.figure()

    result_list = logistic(initial_value=0.4)
    print(f"result_list = {result_list}")
    x_list = result_list[:-1]
    y_list = result_list[1:]

    plt.plot(x_list, y_list, "r.", markersize=0.3)
    plt.plot([0, 1], [0, 1], "g-", lw=2)
    ani = animation.FuncAnimation(fig, _update_plot, fargs= (x_list, y_list),
        interval = 2000, frames=len(x_list))
    plt.show()

if __name__ == "__main__":
        main()
