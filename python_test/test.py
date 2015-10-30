import numpy as np
import matplotlib.pyplot as plt

# 外部データの読み込み
data = np.loadtxt("test_data",delimiter=",")

# 実データをrベクトルに
rx = data[:,0] # 列の取り出し
ry = data[:,1]

# 平均を計算
averx = np.average(rx)
avery = np.average(ry)

# rベクトルをxベクトルに変換(原点を中心にする)
xx = rx - averx
xy = ry - avery

# 分散共分散行列を計算
V = np.zeros((2,2))
V[0][0] = np.dot(rx-averx,rx-averx.T) / 30 # ベクトルと転置したベクトルの内積でシグマ計算を実現
V[0][1] = np.dot(rx-averx,ry-avery.T) / 30
V[1][0] = np.dot(ry-avery,rx-averx.T) / 30
V[1][1] = np.dot(ry-avery,ry-avery.T) / 30

# 分散共分散行列の固有値,固有ベクトルを計算
la, u = np.linalg.eig(V)

print(averx)
print(avery)
print(V)
print(la)
print(u)

# グラフに直線を書く準備
u1x = np.arange(-30,30,1) # -30から30まで1刻みのデータを作成
u1y = np.arange(-30,30,1)
u2x = np.arange(-30,30,1)
u2y = np.arange(-30,30,1)

# 固有ベクトル倍
u1x = u1x * u[0][0]
u1y = u1y * u[1][0]
u2x = u2x * u[0][1]
u2y = u2y * u[1][1]

# u1とu2が直交してないっぽく見えたから内積0になるかどうかで確認
u1 = u[:,0]
u2 = u[:,1]

print(np.dot(u1,u2))

# plt.plot(rx,ry,"bo") # 実データを青でプロット
plt.plot(u1x,u1y,"-r") # u1を赤でプロット
plt.plot(u2x,u2y,"-r") # u2を赤でプロット
plt.plot(xx,xy,"go") # 原点移動したデータを緑でプロット
plt.show()
