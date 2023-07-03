import numpy as np
import pandas as pd

class UCB1(object):
    def __init__(self, N, save_log=False):
        self.N = N
        self.means = np.zeros(N) #各腕の期待値の格納場所
        self.ks = np.zeros(N) #それぞれ腕の試行の回数
        self.g = 0 #全体の試行回数カウント
        self.save_log = save_log
        self.scores = [] #csvファイル保存用
        self.greedy_rates = [] #csvファイル保存用
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.j = 0 #greedy率を求める用
        self.greedy_rate = 0 #greedy行動しているかしていないかの判別、初期は腕の本数全てを回るので0
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か

    def initialize(self):
        self.means = np.zeros(self.N)
        self.ks = np.zeros(self.N)
        self.g = 0
        self.scores = []
        self.greedy_rates = []
        self.accuracies = [] #csvファイル保存用 #accuracy
        self.greedy_rate = 0
        self.accuracy = -1 #正確性（選んだ選択肢が正しいものであったか、否か

    def select_arm(self):
        arm_id = -1
        for i in range(self.N):
            if self.ks[i] == 0:
                arm_id = i
        if arm_id < 0:
            score = self.means + np.sqrt(2.0 * np.log(self.g) / self.ks)#scoreの部分のrsに書き換える。#self.g =全体の試行回数 means =期待値
            arm_id = np.argmax(score)

            self.j = np.argmax(self.means) #greedy_rate計測用
            if self.j == arm_id:
                greedy_rate = 1
            else: 
                greedy_rate = 0

            if arm_id == 0:
                accuracy = 1
            else:
                accuracy = 0

        else:
            score = np.zeros(self.N)
            greedy_rate = 0

            if arm_id == 0:
                accuracy = 1
            else:
                accuracy = 0
        
        if self.save_log:
            self.scores.append(score)
            self.greedy_rates.append(greedy_rate) #greedy率グラフ化のために追加
            self.accuracies.append(accuracy) #正確性グラフ化のために追加
        return arm_id

    def update_param(self, arm_id, reward):
        self.means[arm_id] = (self.means[arm_id] * self.ks[arm_id] + reward) / (
                self.ks[arm_id] + 1.0)
        self.ks[arm_id] += 1.0 #引いた腕の試行回数+1
        self.g += 1 #全体の試行回数+1

    def save(self, folder_name):
        if self.save_log:
            self.scores = pd.DataFrame(self.scores)
            self.scores.to_csv(folder_name + '/score.csv')
            self.greedy_rates = pd.DataFrame(self.greedy_rates) #greedy率グラフ化のために追加
            self.greedy_rates.to_csv(folder_name + '/greedy_rate.csv')#greedy率グラフ化のために追加
            self.accuracies = pd.DataFrame(self.accuracies) #accuracyグラフ化のために追加
            self.accuracies.to_csv(folder_name + '/accuracy.csv')#accuracyグラフ

