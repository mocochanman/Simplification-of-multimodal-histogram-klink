# Simplification-of-multimodal-histogram-klink

### This is an academic R&D code.
A reduced peak approximation algorithm that computes an approximation function with an arbitrary number of peaks for data with multiple peaks is applied to the input of a two-way LSTM-based time series prediction network.

This program performs only the peak number reduction approximation process.

For the algorithm, refer to the conference presentation.

[情報処理学会第85回全国大会 ピーク数減少近似アルゴリズムを用いた時系列予測](https://www.ipsj.or.jp/event/taikai/85/ipsj_web2023/data/pdf/6U-08.html)

# Use
## klink.py
### input > file name（ファイル名）, k:peak（ピーク数）

ex.)Some input histogram f

<img width="452" alt="スクリーンショット 2024-03-05 10 46 19" src="https://github.com/mocochanman/Simplification-of-multimodal-histogram-klink/assets/76963769/4da9a4a8-e5df-4e88-a9a1-a2370e9972fb">


### output > epsilon, num of peak, L2-norm, figure
ex.)Some input histogram f and its k-peak approximate histogram φ(k = 2)

<img width="466" alt="スクリーンショット 2024-03-05 10 42 40" src="https://github.com/mocochanman/Simplification-of-multimodal-histogram-klink/assets/76963769/0c163039-77b7-428e-a0f5-0d2f3443cdc9">


### please save the data as csv and work in the same directory.
