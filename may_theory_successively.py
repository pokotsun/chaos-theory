import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def logistic(a, initial_value=0.5):
    x = [initial_value]
    # 漸化式の結果を500回分リストにセット
    for i in range(500):
        x.append(a * x[-1] * (1 - x[-1]))
    return x[-200:]

def _update_plot(i, range_list):
    if i == (len(range_list) - 1):
        plt.cla() # 現在描画されているグラフを消去

    a = range_list[i]
    x = logistic(a)
    plt.plot([a] * len(x), x, "c.", markersize=0.3)
    #plt.title(f" Number Of Intersections = {len(set(x))}")
    plt.xlim([2, 4])
    plt.ylim([0, 1])
     

# Main関数
def main():
    # 2 ~ 4までを1000等分に区切ってそれぞれのaで計算してみる
    range_list = np.linspace(2, 4, 400) 
    fig = plt.figure()

    ani = animation.FuncAnimation(fig, _update_plot, fargs= (range_list,),
        interval = 1, frames=len(range_list))
    ani.save("logistic.gif", writer= "imagemagick")
    plt.show()

if __name__ == "__main__":
        main()
