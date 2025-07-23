import pandas as pd

# 評価結果を読み込む
df = pd.read_csv("evaluation_results.csv")

# 除外したいファイル名（完全一致）
exclude_list = [
    "Plastic Bomb-vocals-C major-191bpm-440hz.wav"
]

# 誤判定の定義：correct列が False、かつファイル名が除外リストに含まれていない
misclassified = df[(df['correct'] == False) & (~df['filename'].isin(exclude_list))]

print(f"総件数: {len(df)}")
print(f"正解: {df['correct'].sum()}")
print(f"不正解: {len(df) - df['correct'].sum()}（除外対象含む）")
print(f"実際に処理する誤判定: {len(misclassified)}")

print("\n=== 誤判定一覧（除外済み） ===")
for _, row in misclassified.iterrows():
    print(f"- {row['filename']} | 予測={row['prediction']} / 正解={row['label']}")

# 'correct'列を再度保存（上書き用）
df.to_csv("evaluation_results.csv", index=False)

# 誤判定のみ保存（除外後）
misclassified.to_csv("misclassified_list.csv", index=False)
print("\n誤判定一覧を misclassified_list.csv に保存しました（除外済）")
