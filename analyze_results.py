import pandas as pd

# CSV読み込み（列名の空白を削除して安全に扱う）
df = pd.read_csv('./batch_results.csv')
df.columns = df.columns.str.strip()

# 判定結果の確認
print("列名:", df.columns)
print("prediction列の中身の一部:\n", df['prediction'].head())

# ボーカルと判定されたファイルだけ抽出（predictionが1のもの）
vocals_df = df[df['prediction'] == 1]

print(f"ボーカル判定ファイル数: {len(vocals_df)}")

# ここで必要に応じて解析・集計・可視化などの処理を追加してください
