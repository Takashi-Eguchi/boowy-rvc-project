import os
import sys
import shutil
import csv
import numpy as np
import librosa
import joblib

# =========================
#  設定
# =========================
MODEL_PATH = 'svm_model.pkl'
N_MFCC = 13  # 学習時と合わせる


def load_model(path: str):
    if not os.path.exists(path):
        print(f"[ERROR] モデルが見つかりません: {path}")
        sys.exit(1)
    return joblib.load(path)


def extract_mfcc_mean(audio_path: str, n_mfcc: int = N_MFCC) -> np.ndarray:
    """音声からMFCC平均ベクトルを作成して返す"""
    y, sr = librosa.load(audio_path, sr=None, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)

    # 念のため次元調整（足りなければゼロで埋め、超過なら切り詰め）
    if mfcc.shape[0] > n_mfcc:
        mfcc = mfcc[:n_mfcc, :]
    elif mfcc.shape[0] < n_mfcc:
        pad = n_mfcc - mfcc.shape[0]
        mfcc = np.pad(mfcc, ((0, pad), (0, 0)), mode='constant')

    return np.mean(mfcc, axis=1)  # (n_mfcc,)


def predict_label(model, mfcc_mean_vec: np.ndarray):
    """予測クラス(int)と確信度(float)を返す"""
    X = mfcc_mean_vec.reshape(1, -1)
    pred = int(model.predict(X)[0])
    if hasattr(model, "decision_function"):
        conf = float(model.decision_function(X)[0])
    else:
        conf = 0.0
    return pred, conf


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def main():
    # -------------------------
    # 引数チェック
    # -------------------------
    if len(sys.argv) != 3:
        print("使い方: python batch_predict_and_copy.py 入力フォルダ 出力フォルダ")
        print("例: python batch_predict_and_copy.py ./1987_full_wav ./sorted_output")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.isdir(input_dir):
        print(f"[ERROR] 入力フォルダが存在しません: {input_dir}")
        sys.exit(1)

    # 出力サブフォルダ
    vocals_out = os.path.join(output_dir, "vocals")
    nonvocals_out = os.path.join(output_dir, "nonvocals")
    ensure_dir(vocals_out)
    ensure_dir(nonvocals_out)

    # モデル読み込み
    model = load_model(MODEL_PATH)

    # 対象ファイル（wav/mp3）
    audio_files = [
        f for f in os.listdir(input_dir)
        if f.lower().endswith(('.wav', '.mp3'))
    ]

    if not audio_files:
        print(f"[WARN] {input_dir} に音声ファイル(.wav/.mp3)がありません。")
        sys.exit(0)

    results = []

    # -------------------------
    # 判定ループ
    # -------------------------
    for fname in audio_files:
        src_path = os.path.join(input_dir, fname)
        try:
            mfcc_mean = extract_mfcc_mean(src_path)
            pred, conf = predict_label(model, mfcc_mean)
        except Exception as e:
            print(f"[ERROR] 判定失敗: {fname} :: {e}")
            results.append([fname, "ERROR", "", str(e)])
            continue

        # ラベル文字列
        label_str = "ボーカル音声" if pred == 1 else "その他"

        # コピー先決定
        dst_dir = vocals_out if pred == 1 else nonvocals_out
        dst_path = os.path.join(dst_dir, fname)

        try:
            shutil.copy2(src_path, dst_path)
        except Exception as e:
            print(f"[ERROR] コピー失敗: {fname} :: {e}")
            results.append([fname, label_str, conf, f"copy error:{e}"])
            continue

        print(f"{fname} → {label_str}（確信度: {conf:.4f}）コピー先: {dst_path}")
        results.append([fname, label_str, conf, "ok"])

    # -------------------------
    # CSV 保存（UTF-8 BOM）
    # -------------------------
    ensure_dir(output_dir)
    csv_path = os.path.join(output_dir, "predict_results.csv")
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, dialect='excel-tab')  # Excelで列ズレしにくいTSV風
        writer.writerow(["filename", "prediction", "confidence", "status"])
        writer.writerows(results)

    print(f"\n判定＆コピー結果を保存しました: {csv_path}")
    print(f"ボーカル → {vocals_out}")
    print(f"その他   → {nonvocals_out}")


if __name__ == "__main__":
    main()
