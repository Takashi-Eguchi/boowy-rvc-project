#!/usr/bin/env python3
"""
誤判定音声などを解析して特徴量をまとめるツール。

デフォルト動作:
    misclassified_files/ 配下の .wav / .mp3 を全部解析。
    結果CSV: misclassified_features_summary.csv
    図: misclassified_analysis/<filename>_wave.png / _spec.png

任意のフォルダを解析したい場合:
    python analyze_features.py <音声フォルダパス>

依存: numpy, pandas, librosa, matplotlib
"""

import os
import sys
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib
matplotlib.use("Agg")  # GUIなし
import matplotlib.pyplot as plt

# ===== 設定 =====
DEFAULT_DIR = "./misclassified_files"
OUT_DIR = "./misclassified_analysis"
SUMMARY_CSV = "./misclassified_features_summary.csv"
N_MFCC = 13


def analyze_file(audio_path: str):
    """音声1本を読み込み特徴量辞書を返す。"""
    try:
        y, sr = librosa.load(audio_path, sr=None, mono=True)
    except Exception as e:
        return {"filename": os.path.basename(audio_path), "error": str(e)}

    duration = len(y) / sr if sr else 0.0

    # 基本特徴
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)  # (n_mfcc, frames)
    mfcc_mean = np.mean(mfcc, axis=1)  # (n_mfcc,)

    zcr = librosa.feature.zero_crossing_rate(y=y)
    zcr_mean = float(np.mean(zcr))

    spec_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_centroid_mean = float(np.mean(spec_centroid))

    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    spec_bw_mean = float(np.mean(spec_bw))

    spec_roll = librosa.feature.spectral_rolloff(y=y, sr=sr, roll_percent=0.85)
    spec_roll_mean = float(np.mean(spec_roll))

    rms = librosa.feature.rms(y=y)
    rms_mean = float(np.mean(rms))

    # 図保存
    base = os.path.splitext(os.path.basename(audio_path))[0]
    wave_png = os.path.join(OUT_DIR, f"{base}_wave.png")
    spec_png = os.path.join(OUT_DIR, f"{base}_spec.png")

    # 波形
    plt.figure(figsize=(10, 3))
    librosa.display.waveshow(y, sr=sr)
    plt.title(f"Waveform: {base}")
    plt.tight_layout()
    plt.savefig(wave_png, dpi=150)
    plt.close()

    # メルスペクトログラム（dB）
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_db = librosa.power_to_db(S, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel')
    plt.title(f"Mel-Spectrogram: {base}")
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.savefig(spec_png, dpi=150)
    plt.close()

    # 結果辞書
    data = {
        "filename": os.path.basename(audio_path),
        "sr": sr,
        "duration_sec": duration,
        "zcr_mean": zcr_mean,
        "spec_centroid_mean": spec_centroid_mean,
        "spec_bw_mean": spec_bw_mean,
        "spec_roll_mean": spec_roll_mean,
        "rms_mean": rms_mean,
    }
    # MFCC平均（列展開）
    for i, v in enumerate(mfcc_mean, start=1):
        data[f"mfcc{i}"] = float(v)

    return data


def main():
    # 解析対象ディレクトリ
    if len(sys.argv) == 2:
        target_dir = sys.argv[1]
    else:
        target_dir = DEFAULT_DIR

    if not os.path.isdir(target_dir):
        print(f"[ERROR] 解析対象ディレクトリが見つかりません: {target_dir}")
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    # 対象ファイル収集
    audio_files = [
        os.path.join(target_dir, f)
        for f in os.listdir(target_dir)
        if f.lower().endswith(('.wav', '.mp3'))
    ]

    if not audio_files:
        print(f"[WARN] 音声ファイルがありません: {target_dir}")
        sys.exit(0)

    print(f"[INFO] {len(audio_files)} ファイル解析開始: {target_dir}")

    rows = []
    for ap in audio_files:
        print(f"  -> {os.path.basename(ap)}")
        info = analyze_file(ap)
        rows.append(info)

    df = pd.DataFrame(rows)
    df.to_csv(SUMMARY_CSV, index=False, encoding="utf-8-sig")
    print(f"\n解析結果CSVを保存しました: {SUMMARY_CSV}")
    print(f"画像出力フォルダ: {OUT_DIR}")


if __name__ == "__main__":
    main()
