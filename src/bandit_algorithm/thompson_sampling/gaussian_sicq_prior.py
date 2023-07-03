import numpy as np
import pandas as pd

from utils.random import scaled_inverse_chi_squared


class ThompsonSamplingGaussianSicqPrior(object):
    def __init__(self, N, save_log=False):
        self.N = N
        self.ks = np.ones(N) #その腕を引いた回数（最後に更新なので初期値は1ということ？）
        self.mus = np.zeros(N) #平均値
        self.vs = np.ones(N)
        self.sigmas = np.ones(N)
        self.save_log = save_log
        self.variances = [] #分散
        self.thetas = [] #期待値
        self.greedy_rate = 0 #greedy行動しているかしていないかの判別、初期は腕の本数全てを回るので0
        self.greedy_rates = [] #csvファイル保存用
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.j = 0 #greedy率を求める用
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か

    def initialize(self):
        self.ks = np.ones(self.N)
        self.mus = np.zeros(self.N) #平均値
        self.vs = np.ones(self.N) 
        self.sigmas = np.ones(self.N) #シグマ
        self.variances = [] #分散
        self.thetas = []
        self.greedy_rates = []
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.greedy_rate = 0
        self.j = 0
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か


    def select_arm(self):#estimate_armで得られた一番大きい値を返す（一番大きい値の腕を選択する）
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

    def estimate_mean(self): #腕の価値を求めている。
        # For each arm i=1,...,N, sample random value from sicq distribution（各アームi=1,...,Nについて、sicq分布からランダムな値をサンプリングする）
        variance = [scaled_inverse_chi_squared(self.vs[i], self.sigmas[i])
                    for i in range(self.N)]
        # For each arm i=1,...,N, sample random value from normal distribution（各アームi=1,...,Nについて、正規分布からランダムな値をサンプリングする）
        theta = [np.random.normal(self.mus[i],
                                  np.math.sqrt(variance[i] / self.ks[i]))
                 for i in range(self.N)]
        if self.save_log:
            self.thetas.append(theta)
            self.variances.append(variance)
        return theta

    def update_param(self, arm_id, reward):
        sigma = self.sigmas[arm_id]
        v = self.vs[arm_id]
        mu = self.mus[arm_id]
        k = self.ks[arm_id] #その腕を引いた回数
        d = reward - mu #得られた報酬とその腕の報酬平均の差
        # update parameter of sicq distribution　（sicq分布の更新パラメータ）
        self.sigmas[arm_id] = sigma * v / (v + 1.0) + d * d * k / (
                    (v + 1.0) * (k + 1.0))
        self.vs[arm_id] = v + 1.0
        # update parameter of normal distribution（更新パラメータ）
        self.mus[arm_id] = (mu * k + reward) / (k + 1.0)#正規分布の平均値更新、引いた数が多いほど、影響を与えづらい?
        self.ks[arm_id] = k + 1.0

    def save(self, folder_name): #csvファイル保存用
        if self.save_log:
            self.thetas = pd.DataFrame(self.thetas)
            self.thetas.to_csv(folder_name + '/theta.csv')
            self.variances = pd.DataFrame(self.variances)
            self.variances.to_csv(folder_name + '/variance.csv')
            self.greedy_rates = pd.DataFrame(self.greedy_rates) #greedy率グラフ化のために追加
            self.greedy_rates.to_csv(folder_name + '/greedy_rate.csv')#greedy率グラフ化のために追加
            self.accuracies = pd.DataFrame(self.accuracies) #accuracyグラフ化のために追加
            self.accuracies.to_csv(folder_name + '/accuracy.csv')#accuracyグラフ
