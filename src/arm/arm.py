import numpy as np #腕の報酬の正規分布を作成する場所


class NormalDistributionArm(object):
    def __init__(self, mean, sigma):
        self.mean = mean #平均値
        self.sigma = sigma #シグマ

    def play(self):
        return np.random.normal(self.mean, self.sigma) #平均meanと分散シグマを代入し、正規分布のrandomな値を出力

    def name(self):
        return 'N(' + str(self.mean) + ',' + str(self.sigma * self.sigma) + ')' #腕の名前を作成しフォルダに入力
