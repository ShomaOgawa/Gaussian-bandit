import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

colors = ['skyblue','steelblue','grey']

mu = [0,20,-20] # mean
sd = 10 # standard deviation

X = np.arange(-50,50,0.1)

fig = plt.figure(figsize=(6, 4), facecolor='white')
fig.suptitle('Normal Distribution')

ax = fig.add_subplot(111,xlabel='x', ylabel='')

for i,m in enumerate(mu):
  # ここで正規分布を作成
  Y = scipy.stats.norm.pdf(X, loc=m, scale=sd)
  ax.plot(X, Y, c=colors[i], label=f"μ={m}, σ={sd}", zorder=10)

ax.tick_params(bottom=False)

ax.set_xlim(-60,60)
ax.set_ylim(0,.06)
ax.grid(axis='x', c='gainsboro', zorder=9)
ax.grid(axis='y', c='gainsboro', zorder=9)
ax.legend(bbox_to_anchor=(.98,.98), loc='upper right', borderaxespad=0)
[ax.spines[side].set_visible(False) for side in ['right','top']]