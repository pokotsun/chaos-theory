import numpy as np

from matplotlib import pyplot as plt
import matplotlib.cm as cm

class HopfieldNetwork():
    # 初期化: 学習データから重み行列を作成
    def __init__(self, train_list):
        self.dim = len(train_list[0]) # 次元数(覚えさせる画像のピクセル数)
        self.W = np.zeros((self.dim, self.dim)) # 全部0のdim x dim次元配列を生成 重み行列
        # train_list = [d * 2 - 1 for d in train_list] # (-1, 1)に変換
        for t in train_list:
            self.W += np.outer(t, t)

        for i in range(self.dim): # V(i,i)要素は0にする
            self.W[i, i] = 0



    # 更新: 入力値のリストに対し、出力値のリストを返す
    def predict(self, data_list, loop=10):
        return [self._predict(data, loop=loop) for data in data_list]

    # 個々の入力値に対してユニットの値が収束するまで
    # => エネルギーが変化しなくなるまで更新を行う
    def _predict(self, data, loop=10):
        e = self.energy(data)
        for i in range(loop):
            # dataとWの内積を取ったあと,
            # dataの符号を取る [5, -5, 4] => [1, -1, 1]とする
            data = np.sign(self.W.dot(data))
            e_new = self.energy(data)
            if e == e_new: # 想起結果が変わらなければその時点で値を返す
                return data
            else: # エネルギーを再代入して再想起させる
                e = e_new
        return data # とりあえず10回回したらうまく行ってようが行ってまいが値を返す

    # ユニットの状態からネットワークのエネルギーを計算
    def energy(self, data):
        return - (1/2) * (data.dot(self.W).dot(data))


    def plot_weight(self):
        # 重み行列をヒートマップとしてプロット
        fig, ax = plt.subplots(figsize=(5, 3))
        heatmap = ax.pcolor(self.W, cmap=cm.coolwarm)
        cbar = plt.colorbar(heatmap)

        ax.set_xlim(0, self.dim)
        ax.set_ylim(0, self.dim)
        ax.invert_yaxis()
        ax.xaxis.tick_top()
        return fig, ax

    # dataを画像化(2次元化)してaxにプロット
    def plot_data(self, ax, data, with_energy=False):
        dim = int(np.sqrt(len(data)))
        # このサンプルで扱う画像は縦横同じ長さのもののみ
        assert dim * dim == len(data), "イメージが期待する大きさではありません"

        img = (data.reshape(dim, dim) + 1) / 2 # dim x dimの配列に変換したあと(-1,1)を(0,1)に変換
        # print(f"img:{img}")
        ax.imshow(img, cmap=cm.Greys_r)
        if with_energy:
            e = np.round(self.energy(data), 1) # 小数点第一位で四捨五入
            ax.text(0.95, 0.05, e, color="r", ha="right", transform=ax.transAxes)
        return ax


""" ユーティリティ関数 """

# 入力にノイズを付与
def get_corrupted_input(input, corruption_level):
    corrupted = np.copy(input)
    inv = np.random.binomial(n=1, p=corruption_level, size=len(input))

    for i,v in enumerate(input):
        if inv[i]:
            corrupted[i] = -1 * v
            #corrupted[i] = int(not(v)) 
    return corrupted

# 元データ、テストデータ、推測値を描画
def plot(hn, data, test, predicted, figsize=(5,7)):
    fig, axes = plt.subplots(len(data), 3, figsize=figsize)
    for i, axrow in enumerate(axes):
        if i == 0:
            axrow[0].set_title("学習データ")
            axrow[1].set_title("入力データ")
            axrow[2].set_title("出力データ")

        hn.plot_data(axrow[0], data[i], with_energy=True)
        hn.plot_data(axrow[1], test[i], with_energy=True)
        hn.plot_data(axrow[2], predicted[i], with_energy=True)

        for ax in axrow:
            ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)

    return fig, axes

# Main関数
def main():
    print("Main Start")

    np.random.seed(1)
    data = [np.array([0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0,
                  0, 1, 1, 1, 0, 0, 1, 0, 1, 0]),
        np.array([1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0,
                  1, 0, 0, 1, 0, 1, 1, 1, 0, 0]),
        np.array([0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0, 0, 1, 1, 1, 0]),
        #np.array([1,1,1,1,0, 1,0,0,0,0, 1,1,1,1,0, 
        #        1,0,0,0,0, 1,1,1,1,0]),
        ]

    data = [d * 2 - 1 for d in data] # (-1, 1)に変換

    # Hopfield Network インスタンスの作成 と Wの学習 
    hn = HopfieldNetwork(data)

    # 画像に30%のノイズを付与し、テストデータとする
    test = [get_corrupted_input(d, 0.30) for d in data]
    #print(f"test_data:{test}")
    # HopField Networkからの出力
    predicted = hn.predict(test)

    fig, axes = plot(hn, data, test, predicted, figsize=(5, 5))
    # hn.plot_weight()
    plt.show()

if __name__=="__main__":
    main()

