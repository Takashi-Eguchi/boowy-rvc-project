import pandas as pd
import joblib
import numpy as np
import os
from sklearn.metrics import classification_report, confusion_matrix

# ==== 1. モデルと特徴量のロード ====
model = joblib.load("svm_model.pkl")  # 学習済みモデル

# ==== 2. 予測結果ファイルと正解ラベルの読み込み ====
pred_df = pd.read_csv("batch_results.csv")
label_df = pd.read_csv("labels.csv")

# ==== 3. ファイル名でマージ（結合） ====
merged = pd.merge(pred_df, label_df, on="filename", how="inner")

y_true = merged["label"]
y_pred = merged["prediction"]

# ==== 4. 精度評価 ====
print("=== 評価レポート ===")
print(classification_report(y_true, y_pred))

print("\n=== 混同行列 ===")
print(confusion_matrix(y_true, y_pred))

# ==== 5. 結果をCSVに保存 ====
merged.to_csv("evaluation_results.csv", index=False, encoding="utf-8-sig")
print("\n評価結果を evaluation_results.csv に保存しました。")
