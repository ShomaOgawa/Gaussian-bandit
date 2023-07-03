import argparse

from arm.arm import NormalDistributionArm
from bandit_algorithm.hyperopt.hyperopt import HyperOpt
from hyperopt import hp
from utils.data_processing import calc_mean_data


def main():
    parser = argparse.ArgumentParser(
        description='Bandit Experiment of HyperOpt')

    # setting of experiment
    parser.add_argument('--exp_num', type=int, default=1,
                        help='Number of experiments')
    parser.add_argument('--play_num', type=int, default=20000,
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

    # define arms
    arms = [NormalDistributionArm(1.0, 3.0),
            NormalDistributionArm(0.0, 0.3)]

    # define hyper parameters
    hyper_params = {
        'arm': hp.choice('arm', [i for i in range(len(arms))])
    }

    # define bandit algorithm
    algorithm = HyperOpt(arms, hyper_params, args.play_num, args.save_log, args.show_log)
    arm_name = ''
    for i in range(len(arms)):
        arm_name += arms[i].name()
    root_folder_name = '../data/' + arm_name + '/' + algorithm.__class__.__name__

    # run experiment
    if not args.not_run_exp:
        print('----------Run Exp----------')
        for i in range(args.exp_num):
            print('Run Exp' + str(i))
            # define bandit algorithm
            folder_name = root_folder_name + '/Exp' + str(i)
            algorithm.experiment(folder_name)
            print('Finish Exp' + str(i))
            print('')

    # calculate mean values of log
    if args.summarize_log:
        print('----------Calc Mean of Log----------')
        calc_mean_data(root_folder_name)


if __name__ == '__main__':
    main()
