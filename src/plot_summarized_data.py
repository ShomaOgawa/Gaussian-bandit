import argparse#コマンドライン引数の処理のためのモジュール

from utils.data_plotting import plot_summarized_data ##utilsフォルダのdata_plottingファイルのplot_summarized_dataクラス


def main():
    parser = argparse.ArgumentParser(description='Plot summarized data') #argparse.ArgumentParserクラスのインスタンスparserを作成している。

    # setting # setting　#add_argumentメソッドでコマンドライン引数の解析方法を追加していく。オプションに当たる場所
    parser.add_argument('--y_min', type=float, default=0.0,
                        help='Min value of y axis')
    parser.add_argument('--y_max', type=float, default=2000.0,
                        help='Max value of y axis')
    parser.add_argument('--folder_name',default='N(1.0,9.0)N(0.8,4.0)N(0.5,2.25)N(0.0,0.09)',
                        help='Folder name where logs of experiments are saved') #どの実験ファイルを使うか
    parser.add_argument('--file_name', default='regret',
                        help='File name to plot') #regretなどどのファイル名を参照するか

    args = parser.parse_args()

    folder_name = '../data/' + args.folder_name

    # summarize data
    plot_summarized_data(folder_name, args.file_name, args.y_min, args.y_max)


if __name__ == '__main__':
    main()
