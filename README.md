# Gaussian-bandit

バンディット問題の中で連続値を取る複数の報酬源を比較するには報酬分布の形状を少ないサンプル数から評価していく必要がある。一般的には分散の直接推定を含んだ選択アルゴリズムが優れているのだが、人間のリスク判断に習ったアルゴリズムの RS では平均のみで分散推定せずに優れた成績が得られた。

本プログラムは、Gaussian 分布(正規分布)からなる報酬を用いた多腕バンディット問題に RS を適用したものである。　
<br>

## Usage

すべてのpythonファイルを実行するには、`src`フォルダに移動してください。

```
$ cd src
```

### Run Bandit problem Experiment


#### run RS-opt

RS-opt アルゴリズム（希求水準を最適値に設定）の実行

```
$ python run_rs_opt.py
```

#### run RS-dyn

RS-dyn アルゴリズム（希求水準を動的に設定）の実行

```
$ python run_rs_dyn.py
```

#### run Thompson Sampling using Gaussian Prior

報酬が平均が未知、分散が1の正規分布に従うと仮定した TS アルゴリズムの実行

```
$ python run_ts_gaussian.py
```

#### run Thompson Sampling using Gaussian Scaled Inverse Chi-Squared Prior

報酬が平均が未知、分散が未知の正規分布に従うと仮定した TS アルゴリズムの実行

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

出力例は次のとおりです。

```
$ python run_rs_opt.py
----------Run Exp----------
Run Exp0
iteration: 0, selected arm: 3, regret: 1.0
iteration: 5000, selected arm: 0, regret: 135.30000000000018
iteration: 10000, selected arm: 0, regret: 135.30000000000018
iteration: 15000, selected arm: 0, regret: 135.30000000000018
iteration: 20000, selected arm: 0, regret: 135.30000000000018
・
・
・
Finish Exp0
```
<br>

実験の設定を変更するにはいくつかのオプションがあります。

* exp_num： シミュレーションの実行回数。　デフォルトは 1。
* not_run_exp： 実験を実行するかどうか。　デフォルトは False。
* save_log： 出力をcsvファイルに保存するかどうか。　デフォルトは False。
* show_log： matplotlib.pyplot を使って出力をグラフ化するかどうか。　デフォルトは False。
* summarize_log： 出力の平均値を計算して csv ファイルに保存するかどうか。
  
<br>

オプションは以下のように使用できます。

```
$ python run_rs_opt.py --exp_num=100 --save_log --summarize_log
```
上記は、100シミュレーション実験を行いデータを保存し、得られたデータの平均をグラフで出力します

### Plot Output File
#### plot each output of each experiment in the specified folder

各実験の出力を指定したフォルダにプロット

```
$ python plot_each_data.py
```

プロットの設定を変更するオプションがいくつかある。

* y_min: y 軸の最小値。
* y_max: y 軸の最大値： y_max: y 軸の最大値。
* folder_name: 実験の出力が保存されるフォルダの名前 (フォルダ名: `<Arm Name>/<Algorithm Name>`)。
* file_name: プロットするcsvファイル名。

#### 指定したフォルダにある全ての実験結果の要約データをプロットする。

```
$ python plot_summarized_data.py
```

プロットの設定を変更するオプションがいくつかあります。

* y_min: y 軸の最小値。
* y_max: y 軸の最大値： y_max: y 軸の最大値。
* folder_name: 実験の出力を保存するフォルダの名前（フォルダ名：`<Arm Name>`）。
* file_name: プロットするcsvファイルの名前。

### データの保存場所

データは全て `data` に保存される。<br>
data フォルダがない場合は、`src` と同じ階層に作成される。 

<br><br>
## JSAI2023 にて口頭発表

[発表論文](https://drive.google.com/file/d/1v3ExVtRfidsZ-ITpQux5O9aSbvl38vgF/view?usp=drive_link)


<br><br>

### 参考URL

[サイト「【報酬が平均・分散が未知の正規分布に従うと仮定したThompson Sampling】〜多腕バンディット問題入門〜」](https://cafeunder.github.io/rosenblock-chainers-blog/2018/03/06/introduction-bandit.html)<br><br>
[github　「multi-armed-bandit」](https://github.com/bakanaouji/multi-armed-bandit)<br>
