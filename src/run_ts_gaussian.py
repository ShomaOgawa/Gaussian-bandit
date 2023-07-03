#走らせるコード、報酬の平均は未知、分散が1と仮定したトンプソンサンプリング

import argparse #コマンドライン引数の処理のためのモジュール

from arm.arm import NormalDistributionArm #armファイルのarm.pyの中のclassをimportしている（呼び出している。）
#正規分布を作成するclass
from bandit_algorithm.bandit_core import BanditCore #おそらくここで、アルゴリズムファイルにアクセスして、classをimportしている。
#regretなどを取得して出力しているclass
from bandit_algorithm.thompson_sampling.gaussian_prior import \
    ThompsonSamplingGaussianPrior #おそらくここで、アルゴリズムファイルにアクセスして、classをimportしている。
    #実際に腕を回している場所&theta(θ)を取得し出力しているclass
from utils.data_processing import calc_mean_data #utilsファイルのdata_...の中のclassをimportしている。
##出力の平均値を計算して csv ファイルに保存するclass


def main():
    parser = argparse.ArgumentParser(
        description='Bandit Experiment of TS-Gaussian-Prior') #argparse.ArgumentParserクラスのインスタンスparserを作成している。
        #description - 引数のヘルプの前に表示されるテキスト (デフォルト: none)

    # setting of experiment（実験の設定）
    #add_argumentメソッドでコマンドライン引数の解析方法を追加していく。オプションに当たる場所
    parser.add_argument('--exp_num', type=int, default=100,
                        help='Number of experiments')#実験回数
    parser.add_argument('--play_num', type=int, default=99999,
                        help='Number Playing arms in each experiment.')#各実験のプレイアームの数（stepsの数）
    parser.add_argument('--not_run_exp', action='store_true',
                        help='Whether to run experiment')#実験を行うかどうか
                        #action - コマンドラインにこの引数があったときのアクション。
                        #'store_true', 'store_false' - これらは 'store_const' の、それぞれ True と False を格納する特別版になりる。
    parser.add_argument('--save_log', action='store_true',
                        help='Whether to save log')#ログを保存するかどうか
    parser.add_argument('--show_log', action='store_true',
                        help='Whether to show log')#ログを表示するかどうか
    parser.add_argument('--summarize_log', action='store_true',
                        help='Whether to summarize log')#ログをまとめるかどうか
    parser.set_defaults(not_run_exp=False) # set_defaults()を使うと与えられたコマンドライン引数の内容によらず追加の属性を決定することが可能
    parser.set_defaults(save_log=False)
    parser.set_defaults(show_log=False)
    parser.set_defaults(summarize_log=False)

    args = parser.parse_args() #parse_argsメソッドでPythonスクリプトに与えられたコマンドライン引数を解析する

    # define arms （腕を定める？）
    arms = [NormalDistributionArm(1.0, 3.0),
            NormalDistributionArm(0.8, 2.0),
            NormalDistributionArm(0.5, 1.5),
            NormalDistributionArm(0.0, 0.3)] #(期待値,分散)の初期設定？

    # define bandit algorithm（バンディットアルゴリズムの定義）
    algorithm = ThompsonSamplingGaussianPrior(len(arms), args.save_log) #ここで別ファイルのクラスを呼び出している。import参照
    arm_name = ''
    for i in range(len(arms)):#armsの数までforを回す。
        arm_name += arms[i].name()
    root_folder_name = '../data/' + arm_name + '/' + algorithm.__class__.__name__ #フォルダの作成とデータの格納場所指定？
    print(root_folder_name)
    core = BanditCore(arms, algorithm, args)

    # run experiment（実験の実行）
    if not args.not_run_exp:
        print('----------Run Exp----------')#実行結果を返して表示させている場所
        for i in range(args.exp_num):
            print('Run Exp' + str(i))
            # define bandit algorithm（バンディットアルゴリズムを定める）
            folder_name = root_folder_name + '/Exp' + str(i)
            core.experiment(folder_name)
            print('Finish Exp' + str(i))
            print('')

    # calculate mean values of log（対数の平均値を計算する）
    if args.summarize_log:
        print('----------Calc Mean of Log----------')
        calc_mean_data(root_folder_name)


if __name__ == '__main__':#main関数に飛んで実行している。最初に来る場所？
    main()
