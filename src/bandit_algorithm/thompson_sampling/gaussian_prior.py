import numpy as np #pythonの拡張モジュールnumpyをinport。npで使えるように指定（儀式）。
import pandas as pd #pythonの拡張モジュールpandasをinport。pdで使えるように指定（儀式）。


class ThompsonSamplingGaussianPrior(object): #classを生成。後で呼び出してメソッドを使うため(defとかのやつ)
    def __init__(self, N, save_log=False): #initメソッド。classが呼び出された時に自動で呼び出され、初期化してくれる特別なメソッド
        self.N = N
        self.ks = np.zeros(N) #その腕を引いた回数　#np.zeros(N)　第一引数に新しく作りたい配列のshapeを指定すれば、簡単に配列が作成できる。今回はNを指定。例でN=5の時はarray([0., 0., 0., 0., 0.])みたいな
        self.mus = np.zeros(N) #平均値
        self.save_log = save_log
        self.thetas = [] #csvファイル用
        self.greedy_rate = 0 #greedy行動しているかしていないかの判別、初期は腕の本数全てを回るので0
        self.greedy_rates = [] #csvファイル保存用
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.j = 0 #greedy率を求める用
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か
        


    def initialize(self): #2シュミレーション以降のための初期化関数。シミュレーションの最後に呼び出されるはず。
        self.ks = np.zeros(self.N)
        self.mus = np.zeros(self.N)
        self.thetas = []
        self.greedy_rates = []
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.greedy_rate = 0
        self.j = 0
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か

    def select_arm(self): #estimate_mean関数の最大値を返す関数。下のメソッドだね。下を呼び出して、返り値の最大数をこのメソッドで返している。
        arm_id = 0
        arm_id = np.argmax(self.estimate_mean())

        self.j = np.argmax(self.mus)
        if self.j == arm_id:
            greedy_rate = 1
        else: 
            greedy_rate = 0

        if arm_id == 0:
            accuracy = 1
        else:
            accuracy = 0

        if self.save_log:
            self.greedy_rates.append(greedy_rate) #greedy率グラフ化のために追加
            self.accuracies.append(accuracy) #正確性グラフ化のために追加

        return arm_id #選択された腕を返す

    def estimate_mean(self): #腕の価値を求めている
        # For each arm i=1,...,N, sample random value from normal distribution（各アームi=1,...,Nについて、正規分布からランダムな値をサンプリングする。（直訳））
        theta = [np.random.normal(self.mus[i],
                                  np.math.sqrt(1.0 / (self.ks[i] + 1.0))) #正規分布に従った乱数を生成。（平均, 標準偏差, size）#math.sqrt=ルート計算（平方根）+1.0により、forの0からに対応している？
                 for i in range(self.N)] #for文　rangeにより0~self.Nまで1ずつ増やして繰り返す。現在の回数はiに該当し、上記のself.mus[i]などに作用している
        if self.save_log:
            self.thetas.append(theta) #リストthetasの末尾に要素を追加: append()
        return theta

    def update_param(self, arm_id, reward): #アップデートしている場所
        # update parameter of normal distribution（正規分布のパラメータを更新する（直訳））
        self.mus[arm_id] = (self.mus[arm_id] * (self.ks[arm_id] + 1.0)
                            + reward) / (self.ks[arm_id] + 2.0) #musはタプルだからarm_idでインデックスで要素を指定している。
        self.ks[arm_id] += 1.0 #腕の引いた回数+1

    def save(self, folder_name):
        if self.save_log:
            self.thetas = pd.DataFrame(self.thetas) #thetasを2次元配列型にしている。(DFは（values,columns,index = データの値,列名,行名))
            self.thetas.to_csv(folder_name + '/theta.csv') #第一引数にパスを指定し、csvファイルを出力
            self.greedy_rates = pd.DataFrame(self.greedy_rates) #greedy率グラフ化のために追加
            self.greedy_rates.to_csv(folder_name + '/greedy_rate.csv')#greedy率グラフ化のために追加
            self.accuracies = pd.DataFrame(self.accuracies) #accuracyグラフ化のために追加
            self.accuracies.to_csv(folder_name + '/accuracy.csv')#accuracyグラフ

