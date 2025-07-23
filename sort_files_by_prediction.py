import os
import shutil
import pandas as pd

# 判定結果CSVファイルパス
csv_path = './batch_results.csv'

# 音声ファイルの元フォルダ（判定時のファイルパスの親フォルダ）
source_folder = './1987_vocal_wav'

# コピー先フォルダ（なければ作る）
vocals_folder = './sorted_output/vocals'
nonvocals_folder = './sorted_output/nonvocals'

os.makedirs(vocals_folder, exist_ok=True)
os.makedirs(nonvocals_folder, exist_ok=True)

# CSV読み込み
df = pd.read_csv(csv_path)

for _, row in df.iterrows():
    filename = row['filename']
    prediction = row['prediction']

    src_path = os.path.join(source_folder, filename)
    if not os.path.exists(src_path):
        print(f"ファイルが見つかりません: {src_path}")
        continue

    # 判定によりコピー先を決定
    if int(prediction) == 1:
        dst_path = os.path.join(vocals_folder, filename)
    else:
        dst_path = os.path.join(nonvocals_folder, filename)

    # コピー実行
    shutil.copy2(src_path, dst_path)
    print(f"コピーしました: {src_path} -> {dst_path}")

print("分類コピーが完了しました。")
