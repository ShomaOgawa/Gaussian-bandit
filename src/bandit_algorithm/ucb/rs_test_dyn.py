import numpy as np
import pandas as pd


class rs_test_dyn(object):
    def __init__(self, N, save_log=False):#initメソッド。classが呼び出された時に自動で呼び出され、初期化してくれる特別なメソッド
        self.N = N #腕の本数
        self.means = np.zeros(N) #各腕の期待値の格納場所、腕の本数分確保
        self.ks = np.zeros(N) #それぞれ腕の試行の回数
        self.g = 0 #全体の試行回数カウント
        self.save_log = save_log
        self.scores = [] #csvファイル保存用
        self.greedy_rates = [] #csvファイル保存用
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.aleph_dyn = 0.0 #aleph_dynの初期値
        self.aleph_dyn_b = 0.001 #self.aleph_dyn の更新に用いる初期値。今回の論文は0.001、先行研究と同じ（加藤さんのやつ）
        self.j = 0 #greedy率を求める用
        self.greedy_rate = 0 #greedy行動しているかしていないかの判別、初期は腕の本数全てを回るので0
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か

    def initialize(self):#2シュミレーション以降のための初期化関数。シミュレーションの最後に呼び出されるはず。
        self.means = np.zeros(self.N)
        self.ks = np.zeros(self.N)
        self.g = 0
        self.scores = []
        self.greedy_rates = []
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.aleph_dyn = 0.0 #aleph_dynの初期値
        self.greedy_rate = 0
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か

    def select_arm(self):#腕の選択をしている場所
        arm_id = -1
        for i in range(self.N):
            if self.ks[i] == 0: #一回も引いたことなかったら
                arm_id = i #その腕を引く returnへ
        if arm_id < 0:#2度目以降の腕選択

            score = (self.ks/self.g) * (self.means - self.aleph_dyn) #aleph_dynを用いたscore算出用
            arm_id = np.argmax(score) #RS腕選択用
            self.aleph_dyn = self.aleph_dyn + (self.aleph_dyn_b * (max(self.means) - self.aleph_dyn)) #aleph_dyn更新用 max(self.means) か self.means[arm_id]、今回の論文はmax

            #greedy率を求めるために、今回選んだ腕は今得られている中で一番期待値が高い腕なのかを計算
            self.j = np.argmax(self.means)
            if self.j == arm_id:
                greedy_rate = 1
            else: 
                greedy_rate = 0

            if arm_id == 0:
                accuracy = 1
            else:
                accuracy = 0

        else:
            score = np.zeros(self.N) #腕を引いたのが初回なので、0を格納
            greedy_rate = 0

            if arm_id == 0:
                accuracy = 1
            else:
                accuracy = 0
            
        if self.save_log:
            self.scores.append(score)#scoreのデータを格納して保存
            self.greedy_rates.append(greedy_rate) #greedy率グラフ化のために追加
            self.accuracies.append(accuracy) #正確性グラフ化のために追加
        return arm_id #選択された腕を返す

    def update_param(self, arm_id, reward): #その腕の期待値を更新
        self.means[arm_id] = (self.means[arm_id] * self.ks[arm_id] + reward) / (
                self.ks[arm_id] + 1.0) #学習率考慮込み?用変更
        self.ks[arm_id] += 1.0 #腕の弾いた回数+1
        self.g += 1 #全体回数+1

    def save(self, folder_name): #1simのscoreとgreedy_rateをcsvで保存
        if self.save_log:
            self.scores = pd.DataFrame(self.scores)
            self.scores.to_csv(folder_name + '/score.csv')
            self.greedy_rates = pd.DataFrame(self.greedy_rates) #greedy率グラフ化のために追加
            self.greedy_rates.to_csv(folder_name + '/greedy_rate.csv')#greedy率グラフ化のために追加
            self.accuracies = pd.DataFrame(self.accuracies) #accuracyグラフ化のために追加
            self.accuracies.to_csv(folder_name + '/accuracy.csv')#accuracyグラフ
