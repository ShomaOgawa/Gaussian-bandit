#バンディットの中身
import matplotlib.pyplot as plt #おなじみmapplotlib
import os ##主にファイルやディレクトリ操作が可能で、ファイルの一覧やpathを取得できたり、新規にファイル・ディレクトリを作成することができる
import pandas as pd #おなじみpandas


class BanditCore(object):
    def __init__(self, arms, algorithm, args):
        self.arms = arms
        self.algorithm = algorithm
        self.play_num = args.play_num
        self.save_log = args.save_log
        self.show_log = args.show_log

    def experiment(self, folder_name):
        self.algorithm.initialize()

        regret = 0.0
        regrets = []

        # main loop
        t = 0
        while True:
            # select arm（腕を選択
            arm_id = self.algorithm.select_arm()
            # play arm and observe reward （報酬を取得）
            reward = self.arms[arm_id].play()
            # update parameter of bandit algorithm（バンディットアルゴリズムの更新パラメータ）
            self.algorithm.update_param(arm_id, reward)
            # update regret（regretをアップデート）
            regret += self.arms[0].mean - self.arms[arm_id].mean
            # stock log（ログをためる）
            regrets.append(regret)
            # output
            if t % 5000 == 0:
                s = 'iteration: ' + str(t) + ', selected arm: ' + str(arm_id) \
                    + ', regret: ' + str(regret)
                print(s)
            t += 1
            if t > self.play_num:
                break

        # plot log （グラフを表示する）
        if self.show_log:
            plt.plot(regrets)
            plt.grid()
            plt.xscale('log')
            plt.xlim(0, self.play_num)
            plt.ylim(0, 100)
            plt.show()

        # save log（regretをcsvファイルで保存）
        if self.save_log:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            regrets = pd.DataFrame(regrets)
            regrets.to_csv(folder_name + '/regret.csv')
            self.algorithm.save(folder_name)
