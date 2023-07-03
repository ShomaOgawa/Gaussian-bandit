#出力の平均値を計算して csv ファイルに保存するコード
import os #主にファイルやディレクトリ操作が可能で、ファイルの一覧やpathを取得できたり、新規にファイル・ディレクトリを作成することができる
import pandas as pd


def calc_mean_data(folder_name):
    files = os.listdir(folder_name) #folder_name内のディレクトリ、ファイル参照
    files = [file for file in files if file[:3] == 'Exp'] #フォルダ名の前から3つがEXPならfilesリストに入れる。fileはforのi適な
    N = len(files) #filesの個数（sim数）をNに代入

    file_names = os.listdir(folder_name + '/Exp0')
    file_names = [file_name for file_name in file_names
                  if file_name[-4:] == '.csv']

    for file_name in file_names:
        df = [pd.read_csv(folder_name + '/Exp' + str(i) + '/'
                                    + file_name) for i in range(N)]
        mean = df[0]
        for i in range(1, N):
            mean = mean + df[i]
        mean = mean / N
        mean.to_csv(folder_name + '/mean_' + file_name)
        print("Save" + folder_name + '/mean_' + file_name)
