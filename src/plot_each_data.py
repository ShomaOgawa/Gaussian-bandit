import argparse #コマンドライン引数の処理のためのモジュール

import os #主にファイルやディレクトリ操作が可能で、ファイルの一覧やpathを取得できたり、新規にファイル・ディレクトリを作成することができる。

from utils.data_plotting import plot_each_data #utilsフォルダのdata_plottingファイルのplot_each_dataクラス


def main():
    parser = argparse.ArgumentParser(description='Plot each data')

    # setting　#add_argumentメソッドでコマンドライン引数の解析方法を追加していく。オプションに当たる場所
    parser.add_argument('--y_min', type=float, default=0.0,
                        help='Min value of y axis') #y_min: y 軸の最小値。
    parser.add_argument('--y_max', type=float, default=100.0,
                        help='Max value of y axis') #y_max: y 軸の最大値
    parser.add_argument('--folder_name',
                        default='N(1.0,9.0)N(0.8,4.0)N(0.5,2.25)N(0.0,0.09)'
                                '/rs_test_dyn',
                        help='Folder name where logs of experiments are saved') #folder_name: 実験の出力が保存されるフォルダーの名前
    parser.add_argument('--file_name', default='regret',
                        help='File name to plot') #file_name: プロットする csv ファイルの名前

    args = parser.parse_args()

    folder_name = '../data/' + args.folder_name #dataファルの中のfolder_nameにアクセス

    # summarize data
    print('----------Plot Data----------')
    files = os.listdir(folder_name)
    files = [file for file in files
             if file[-4:] != '.csv' and files[-4:] != '.pdf'
             and file[:1] != '.']
    for file in files:
        print('Plot Data : ' + folder_name + '/' + file + '/'
              + args.file_name + '.csv')
        plot_each_data(folder_name + '/' + file, args.file_name,
                       args.y_min, args.y_max)


if __name__ == '__main__':
    main()
