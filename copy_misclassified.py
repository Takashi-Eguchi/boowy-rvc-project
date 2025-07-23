import os
import shutil
import pandas as pd

# 元音声ファイルのあるフォルダを指定（ここを環境に合わせて書き換え）
AUDIO_DIR = './1987_vocal_wav'

# 誤判定一覧CSVとコピー先フォルダ
MISCLASSIFIED_CSV = 'evaluation_results.csv'
COPY_DIR = './misclassified_files'

def main():
    # evaluation_results.csvを読み込む
    df = pd.read_csv(MISCLASSIFIED_CSV)

    # 'correct'列がなければエラー
    if 'correct' not in df.columns:
        print(f"{MISCLASSIFIED_CSV} に 'correct' 列がありません。inspect_misclassified.py を先に実行してください。")
        return

    # 誤判定（correct == False）のみ抽出
    misclassified = df[df['correct'] == False]

    # コピー先フォルダを作成（存在しなければ）
    os.makedirs(COPY_DIR, exist_ok=True)

    count = 0
    for idx, row in misclassified.iterrows():
        filename = row['filename']
        src_path = os.path.join(AUDIO_DIR, filename)
        dst_path = os.path.join(COPY_DIR, filename)

        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
            count += 1
        else:
            print(f"ファイルが見つかりません: {src_path}")

    print(f"誤判定 {count} 件を {COPY_DIR} にコピーしました。")
    misclassified.to_csv('misclassified_list.csv', index=False)
    print("誤判定一覧: misclassified_list.csv に保存済み")

if __name__ == '__main__':
    main()
