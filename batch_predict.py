import os
import sys
import glob
import numpy as np
import joblib

MODEL_PATH = 'svm_model.pkl'  # ここを修正しました

def extract_features(npy_path):
    # npyファイルからMFCC平均を読み込む例
    mfcc = np.load(npy_path)
    # 例: MFCCの13次元を平均
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean

def main(input_dir):
    if not os.path.exists(MODEL_PATH):
        print(f"モデルファイルが見つかりません: {MODEL_PATH}")
        sys.exit(1)

    model = joblib.load(MODEL_PATH)
    print(f"モデルを読み込みました: {MODEL_PATH}")

    npy_files = glob.glob(os.path.join(input_dir, '*.npy'))
    if len(npy_files) == 0:
        print(f"npyファイルが見つかりません: {input_dir}")
        sys.exit(1)

    results = []
    for npy_file in npy_files:
        features = extract_features(npy_file)
        features = features.reshape(1, -1)
        prediction = model.predict(features)[0]
        confidence = model.decision_function(features)[0]

        filename = os.path.basename(npy_file).replace('.npy', '')
        results.append((filename, prediction, confidence))

        print(f"{filename}: 判定={prediction}, 信頼度={confidence:.3f}")

    # CSVに保存
    import csv
    output_csv = 'batch_results.csv'
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['filename', 'prediction', 'confidence'])
        writer.writerows(results)

    print(f"判定結果を {output_csv} に保存しました。（UTF-8 BOM付き）")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("使い方: python batch_predict.py <npyファイルのあるディレクトリ>")
        sys.exit(1)
    main(sys.argv[1])
