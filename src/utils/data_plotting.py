import os
import matplotlib.pyplot as plt
import pandas as pd

def plot_each_data(folder_name, file_name, y_min, y_max, data=None, legend=None): #plot_each_data.pyから渡される。
    plt.rcParams['font.family'] = 'DejaVu Serif'
    if data is None:
        data = pd.read_csv(folder_name + '/' + file_name + '.csv')
    plt.plot(data)
    plt.grid()
    plt.xscale('log')
    #plt.xlim(0, len(data.index))
    plt.xlim(1,100000)
    plt.ylim(y_min, y_max)
    plt.xlabel("step",fontsize = 13)
    plt.ylabel("regret",fontsize = 13)
    if legend is not None:
        plt.legend(legend, loc='upper left',fontsize=13, frameon=False) #loc='lower right'or'upper left'
    plt.savefig(folder_name + '/' + file_name + '.png')
    plt.close()


def plot_summarized_data(folder_name, file_name, y_min, y_max): #plot_summarized_data.pyから渡される。
    files = os.listdir(folder_name) #指定したファイル・ディレクトリの一覧を確認する、listdir関数の引数に取得したいディレクトリのパスを指定。
    files = [file for file in files if file[-4:] != '.pdf' and file[:1] != '.']

    # summarize data（データをまとめる）
    df = [pd.read_csv(folder_name + '/' + file
                                + '/mean_' + file_name + '.csv')
          for file in files]
    df_concat = pd.DataFrame()
    for data in df:
        df_concat = pd.concat([df_concat, data], axis=1)

    # plot data
    plot_each_data(folder_name, 'summarized_maen_' + file_name, y_min, y_max,
                   df_concat, files)
