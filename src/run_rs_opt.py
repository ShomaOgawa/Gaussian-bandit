import argparse

from arm.arm import NormalDistributionArm
from bandit_algorithm.bandit_core import BanditCore
from bandit_algorithm.ucb.rs_opt import rs_opt
from utils.data_processing import calc_mean_data


def main():
    parser = argparse.ArgumentParser(
        description='Bandit Experiment of RSopt')

    # setting of experiment（実験の設定）
    #add_argumentメソッドでコマンドライン引数の解析方法を追加していく。オプションに当たる場所
    parser.add_argument('--exp_num', type=int, default=100,
                        help='Number of experiments')
    parser.add_argument('--play_num', type=int, default=99999,
                        help='Number Playing arms in each experiment.')
    parser.add_argument('--not_run_exp', action='store_true',
                        help='Whether to run experiment')
    parser.add_argument('--save_log', action='store_true',
                        help='Whether to save log')
    parser.add_argument('--show_log', action='store_true',
                        help='Whether to show log')
    parser.add_argument('--summarize_log', action='store_true',
                        help='Whether to summarize log')
    parser.set_defaults(not_run_exp=False)
    parser.set_defaults(save_log=False)
    parser.set_defaults(show_log=False)
    parser.set_defaults(summarize_log=False)

    args = parser.parse_args()

    # define arms （腕の正規分布の報酬を指定、腕を増やすことも可能）
    arms = [NormalDistributionArm(1.0, 3.0),
            NormalDistributionArm(0.8, 2.0),
            NormalDistributionArm(0.5, 1.5),
            NormalDistributionArm(0.0, 0.3)]

    # define bandit algorithm（バンディットアルゴリズムの定義）
    algorithm = rs_opt(len(arms), args.save_log)
    arm_name = ''
    for i in range(len(arms)): #腕の数だけforを回す
        arm_name += arms[i].name()
    root_folder_name = '../data/' + arm_name + '/' + algorithm.__class__.__name__
    core = BanditCore(arms, algorithm, args)

    # run experiment(
    # 実験の実行）
    if not args.not_run_exp:
        print('----------Run Exp----------')#実験を繰り返して表示させる
        for i in range(args.exp_num):
            print('Run Exp' + str(i))
            # define bandit algorithm #（バンディットアルゴリズムを定める）
            folder_name = root_folder_name + '/Exp' + str(i)
            core.experiment(folder_name)
            print('Finish Exp' + str(i))
            print('')

    # calculate mean values of log（対数の平均値を計算する）
    if args.summarize_log:
        print('----------Calc Mean of Log----------')
        calc_mean_data(root_folder_name)


if __name__ == '__main__':
    main()
