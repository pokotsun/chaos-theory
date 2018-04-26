import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def logistic(a, initial_value=0.5):
    x = [initial_value]
    # 漸化式の結果を500回分リストにセット
    for i in range(500):
        x.append(a * x[-1] * (1 - x[-1]))
    return x[-100:]

# Main関数
def main():
    # 2 ~ 4までを1000等分に区切ってそれぞれのaで計算してみる
    range_list = np.linspace(2, 4, 100) 
    fig = plt.figure()
    ims = []
    x_list = []
    for (i, a) in enumerate(range_list): 
        x = logistic(a)
        
        im = plt.plot([a] * len(x), x, "c.", markersize=0.5)
        # グラフを描画していく
        #plot(x軸, y軸, 描画したいデータ, str"色plotの形", opt)
        #plt.subplot(2, 1, 1)
        #plt.plot([a] * len(x), x, "c.", markersize=0.5)
        #plt.title("$f(x+1) = ax(1 - x)$")
        #plt.subplot(2, 1, 2)
        #im = plt.plot([a] * len(x), x, "c.", markersize=0.5)
        #plt.title("logistic function")
        ims.append(im) # グラフを配列 imsに追加

    ani = animation.ArtistAnimation(fig, ims, interval=50)
    plt.show()

if __name__ == "__main__":
        main()
