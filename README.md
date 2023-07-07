# Gaussian-bandit

バンディット問題の中で連続値を取る複数の報酬源を比較するには報酬分布の形状を少ないサンプル数から評価していく必要がある。一般的には分散の直接推定を含んだ選択アルゴリズムが優れているのだが、人間のリスク判断に習ったアルゴリズムの RS では平均のみで分散推定せずに優れた成績が得られた。

本プログラムは、Gaussian 分布(正規分布)からなる報酬を用いた多腕バンディット問題に RS を適用したものである。　

## 使用方法

すべてのpythonファイルを実行するには、`src`フォルダに移動してください。

```
$ cd src
```

### バンディット実験の実行
#### ガウス事前分布を用いたトンプソンサンプリングの実行

```
$ python run_ts_gaussian.py
```

#### ガウス尺度逆カイ二乗事前分布を用いたトンプソンサンプリングの実行

```
$ python run_ts_gaussian_sicq.py
```

#### UCB1 の実行

```
$ python run_ucb1.py
```

#### ハイパーオプトの実行

```
$ python run_hyperopt.py
```

出力例は次のとおりです。

```
$ python run_ts_gaussian.py
----------実行 Exp----------
Exp0 を実行
反復： 0, 選択アーム: 1, 後悔: 1.0
反復 5000, 選択アーム: 0, 後悔: 120.0
反復 10000、選択アーム：0、後悔：120.0
反復： 15000、選択アーム：0、後悔：120.0
反復：20000、選択アーム：0、後悔：120.0
Exp0の終了
```

実験の設定を変更するにはいくつかのオプションがある。

* exp_num： 実験の実行回数。デフォルトは1。
* not_run_exp： 実験を実行するかどうか。デフォルトはFalse。
* save_log： 出力をcsvファイルに保存するかどうか。デフォルトは False。
* show_log： matplotlib.pyplot を使って出力をグラフ化するかどうか。デフォルトは False です。
* summary_log： 出力の平均値を計算して csv ファイルに保存するかどうか。

オプションは以下のように使用できます。

```
$ python run_ts_gaussian.py --exp_num=100 --save_log
```

### 出力ファイルのプロット
#### 各実験の出力を指定したフォルダにプロットします。

```
$ python plot_each_data.py
```

プロットの設定を変更するオプションがいくつかある。

* y_min: y 軸の最小値。デフォルトは 0.0 です。
* y_max: y 軸の最大値： y_max: y 軸の最大値。デフォルトは100.0。
* folder_name: 実験の出力が保存されるフォルダの名前 (フォルダ名: `<アーム名>/<アルゴリズム名>`)。デフォルトは "N(1.0,9.0)N(0.0,0.09)/ThompsonSamplingGaussianPrior"。
* file_name: プロットするcsvファイル名。デフォルトは "regret"。

#### 指定したフォルダにある全ての実験結果の要約データをプロットする。

```
$ python plot_summarized_data.py
```

プロットの設定を変更するオプションがいくつかあります。

* y_min: y 軸の最小値。デフォルトは 0.0 です。
* y_max: y 軸の最大値： y_max: y 軸の最大値。デフォルトは100.0。
* folder_name: 実験の出力を保存するフォルダの名前（フォルダ名：`<Arm Name>`）。デフォルトは "N(1.0,9.0)N(0.0,0.09)"。
* file_name: プロットするcsvファイルの名前。デフォルトは "regret"。






# 以降は参考プログラムのREADME

### 参考URL

[サイト「【報酬が平均・分散が未知の正規分布に従うと仮定したThompson Sampling】〜多腕バンディット問題入門〜」](https://cafeunder.github.io/rosenblock-chainers-blog/2018/03/06/introduction-bandit.html)<br><br>
[github　「multi-armed-bandit」](https://github.com/bakanaouji/multi-armed-bandit)<br>

## Usage

To run all python files, please move to the `src` folder.

```
$ cd src
```

### Run Bandit Experiment
#### run Thompson Sampling using Gaussian Prior

```
$ python run_ts_gaussian.py
```

#### run Thompson Sampling using Gaussian Scaled Inverse Chi-Squared Prior

```
$ python run_ts_gaussian_sicq.py
```

#### run UCB1

```
$ python run_ucb1.py
```

#### run Hyperopt

```
$ python run_hyperopt.py
```

The example output is

```
$ python run_ts_gaussian.py
----------Run Exp----------
Run Exp0
iteration: 0, selected arm:　1, regret: 1.0
iteration: 5000, selected arm:　0, regret: 120.0
iteration: 10000, selected arm:　0, regret: 120.0
iteration: 15000, selected arm:　0, regret: 120.0
iteration: 20000, selected arm:　0, regret: 120.0
Finish Exp0
```

There are several options to change setting of experiment.

* exp_num: Number of times to run experiment. Defaults to 1.
* not_run_exp: Whether to run experiment. Defaults to False.
* save_log: Whether to save output to csv file. Defaults to False.
* show_log: Whether to graph output using matplotlib.pyplot. Defaults to False.
* summarize_log: Whether to calculate mean values of output and save it to csv file.

Options can be used like follows

```
$ python run_ts_gaussian.py --exp_num=100 --save_log
```

### Plot Output File
#### plot each output of each experiment in the specified folder

```
$ python plot_each_data.py
```

There are several options to change setting of plotting.

* y_min: Min value of y axis. Defaults to 0.0.
* y_max: Max value of y axis. Defaults to 100.0.
* folder_name: Name of folder where outputs of experiment are saved (Name of folder: `<Arm Name>/<Algorithm Name>`). Defaults to "N(1.0,9.0)N(0.0,0.09)/ThompsonSamplingGaussianPrior".
* file_name: Name of csv file to plot. Defaults to "regret".

#### plot summarized data of output of all experiments in the specified folder.

```
$ python plot_summarized_data.py
```

There are several options to change setting of plotting.

* y_min: Min value of y axis. Defaults to 0.0.
* y_max: Max value of y axis. Defaults to 100.0.
* folder_name: Name of folder where outputs of experiment are saved (Name of folder: `<Arm Name>`). Defaults to "N(1.0,9.0)N(0.0,0.09)".
* file_name: Name of csv file to plot. Defaults to "regret".
